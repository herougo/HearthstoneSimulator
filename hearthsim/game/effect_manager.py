import collections
from hearthsim.utils.hash_generation import (generate_random_hash, NULL_HASH, PLAYER0_HASH, PLAYER1_HASH)
from hearthsim.utils.linked_list import LinkedList, LinkedListNode
from hearthsim.utils.utils import shift_text_lines_by_tab


class EffectManagerNodePlan:
    '''
    If start, execute, or send_event need to push or pop effects, they return
    this object. TimeLimitedEffect, for example, takes that plan and modifies it
    and returns it further up the recursive call. EffectManagerNode handles the
    final result and takes according actions.
    '''

    def __init__(self, to_add=None, to_remove=None, update_stats=None):
        # update_stats
        if not update_stats:
            update_stats = set()
        self.to_add = to_add or []
        self.to_remove = to_remove or []
        self.update_stats = update_stats
        if not isinstance(self.to_add, list):
            raise ValueError('EffectManagerNodePlan needs to_add to be a list')
        if not isinstance(self.to_remove, list):
            raise ValueError('EffectManagerNodePlan needs to_remove to be a list')

    def perform(self, effect_manager):
        for em_node in self.to_add:
            effect_manager.add_effect(em_node)
        for em_node in self.to_remove:
            effect_manager.pop_effect(em_node)
        if self.update_stats:
            for card_slot in self.update_stats:
                card_slot.update_stats()

    def update(self, new_plan):
        if new_plan:
            self.to_add.extend(new_plan.to_add)
            self.to_remove.extend(new_plan.to_remove)
            self.update_stats = self.update_stats | new_plan.update_stats

    def is_empty(self):
        return (not self.to_add) and (not self.to_remove) and (not self.update_stats)


class EffectManagerNode:
    def __init__(self, effect, affected_slot, origin_slot, silenceable, hash=None):
        self.effect = effect.copy()
        self.affected_slot = affected_slot  # what the effect affects
        self.origin_slot = origin_slot  # where the effect came from
        self.silenceable = silenceable
        self._hash = hash or generate_random_hash()

    def start(self, game, effect_manager):
        plan = self.effect.start(game, self)
        if plan:
            plan.perform(effect_manager)

    def stop(self, game, effect_manager):
        plan = self.effect.stop(game, self)
        if plan:
            plan.perform(effect_manager)

    def execute(self, game, effect_manager):
        plan = self.effect.execute(game, self)
        if plan:
            plan.perform(effect_manager)

    def send_event(self, event, game, effect_manager, event_slot):
        plan = self.effect.send_event(event, game, self, event_slot)
        if plan:
            plan.perform(effect_manager)

    def __str__(self):
        return f'EffectManagerNode(effect={self.effect}, hash={self._hash})'

    def __eq__(self, other):
        return hash(self) == hash(other)

    def __lt__(self, other):
        return hash(self) < hash(other)

    def __ne__(self, other):
        return not self.__eq__(other)

    def __hash__(self):
        return self._hash


class EffectManagerNodeList:
    def __init__(self):
        self._linked_list = LinkedList()
        self._em_node_to_ll_node = {}

    def append(self, em_node):
        node = LinkedListNode(em_node)
        self._em_node_to_ll_node[em_node] = node
        self._linked_list.add_node_before(None, node)
        assert em_node in self._em_node_to_ll_node

    def remove(self, em_node):
        ll_node = self._em_node_to_ll_node.get(em_node, None)
        self._linked_list.remove_node(ll_node)
        del self._em_node_to_ll_node[em_node]

    def __iter__(self):
        for node in self._linked_list:
            yield node.val

    def __len__(self):
        return len(self._linked_list)

    def __str__(self):
        return ', '.join(([str(node) for node in self]))


class EventCardSlotToEMNodeListDictionary:
    # Maps event to a dictionary mapping card slot to an EffectManagerNodeList. This also handles PLAYER0_HASH and
    # NULL_HASH
    def __init__(self):
        self._slot_specific_data = {}
        self._player_and_null_data = {}

    def add(self, event, em_node):
        slot = em_node.affected_slot
        if event not in self._slot_specific_data:
            self._slot_specific_data[event] = {}
            self._player_and_null_data[event] = {
                NULL_HASH: EffectManagerNodeList(),
                PLAYER0_HASH: EffectManagerNodeList(),
                PLAYER1_HASH: EffectManagerNodeList()
            }
        if em_node.effect.requires_slot_match_for_event:
            slot_to_em_node_list = self._slot_specific_data[event]
            if slot not in slot_to_em_node_list:
                self._slot_specific_data[event][slot] = EffectManagerNodeList()
            self._slot_specific_data[event][slot].append(em_node)
        elif em_node.effect.requires_slot_player_match_for_event:
            player = em_node.affected_slot.player
            self._player_and_null_data[event][player].append(em_node)
        else:
            self._player_and_null_data[event][NULL_HASH].append(em_node)

    def remove(self, event, em_node):
        if em_node.effect.requires_slot_match_for_event:
            slot = em_node.affected_slot
            self._slot_specific_data[event][slot].remove(em_node)
        elif em_node.effect.requires_slot_player_match_for_event:
            self._player_and_null_data[event][em_node.affected_slot.player].remove(em_node)
        else:
            self._player_and_null_data[event][NULL_HASH].remove(em_node)

    def iter_em_nodes(self, event, event_slot=None):
        mapping_to_em_node_list = self._player_and_null_data.get(event, None)
        if mapping_to_em_node_list:
            for em_node in mapping_to_em_node_list[NULL_HASH]:
                yield em_node
            if event_slot:
                em_node_list = mapping_to_em_node_list.get(event_slot.player, None)
                if em_node_list:
                    for em_node in em_node_list:
                        yield em_node
                em_node_list = self._slot_specific_data[event].get(event_slot, None)
                if em_node_list:
                    for em_node in em_node_list:
                        yield em_node

    def __str__(self):
        lines = []
        for k1, hash_to_em_node_list in self._player_and_null_data.items():
            lines.append(f'{k}:')
            for k2, v in hash_to_em_node_list.items():
                lines.append(f'\t{k2}: {v}')
        return '\n'.join(lines)


class EffectManager:
    def __init__(self, game):
        self._em_nodes = set()
        self._em_node_to_events = collections.defaultdict(list)
        self._event_to_effect_node_list = EventCardSlotToEMNodeListDictionary()
        self._slot_to_em_node_list = collections.defaultdict(EffectManagerNodeList)
        self._game = game

    def add_effect(self, em_node):
        slot = em_node.affected_slot

        self._em_nodes.add(em_node)
        for received_event in em_node.effect.events_received:
            self._em_node_to_events[em_node].append(received_event)
            self._event_to_effect_node_list.add(received_event, em_node)

        em_node.start(self._game, self)

        self._slot_to_em_node_list[slot].append(em_node)

    def iter_em_nodes_by_slot(self, slot):
        for em_node in self._em_node_to_events.get(slot, []):
            yield em_node

    def pop_effect(self, em_node):
        slot = em_node.affected_slot
        em_node.stop(self._game, self)
        for event in self._em_node_to_events[em_node]:
            self._event_to_effect_node_list.remove(event, em_node)

        self._slot_to_em_node_list[em_node].remove(em_node)
        self._em_nodes.remove(em_node)
        del self._em_node_to_events[em_node]

    def pop_effects_by_slot(self, card_slot):
        em_nodes = list(reversed(list(self._slot_to_em_node_list[card_slot])))
        for em_node in em_nodes:
            self.pop_effect(em_node)

    def send_event(self, event, event_slot=None):
        for em_node in self._event_to_effect_node_list.iter_em_nodes(event, event_slot=event_slot):
            em_node.send_event(event, game=self._game, effect_manager=self, event_slot=event_slot)

    def log_state(self):
        lines = []
        lines.append('_em_node_hash_to_node')
        for v in self._em_nodes:
            lines.append(f'\t{v}')
        lines.append('_em_node_hash_to_events')
        for k, v in self._em_node_to_events.items():
            lines.append(f'\t{k} {v}')
        lines.append('_event_to_effect_node_list')
        lines.append(shift_text_lines_by_tab(str(self._event_to_effect_node_list)))
        lines.append('_slot_hash_to_em_node_list')
        for k, v in self._slot_to_em_node_list.items():
            lines.append(f'\t{k} {v}')

        self._game.ui_manager.log_text('\n'.join(lines))

    def __str__(self):
        result = []
        for slot, em_node_list in self._slot_to_em_node_list.items():
            result.append(f'{slot}')
            for em_node in em_node_list:
                result.append(f'\t{em_node.effect}')
        return '\n'.join(result)

