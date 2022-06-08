import collections
from hearthsim.utils.hash_generation import (generate_random_hash, NULL_HASH, PLAYER0_HASH, PLAYER1_HASH)
from hearthsim.utils.linked_list import (LinkedList, LinkedListNode)


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
        self.to_add.extend(new_plan.to_add)
        self.to_remove.extend(new_plan.to_remove)
        self.update_stats = self.update_stats | new_plan.update_stats


class EffectManagerNode:
    def __init__(self, effect, affected_slot, origin_slot, silenceable, hash=None):
        self.effect = effect.copy()
        self.affected_slot = affected_slot  # what the effect affects
        self.origin_slot = origin_slot  # where the effect came from
        self.silenceable = silenceable
        self.hash = hash or generate_random_hash()

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
        return f'EffectManagerNode(effect={self.effect}, hash={self.hash})'


class EffectManagerNodeList:
    def __init__(self):
        self._linked_list = LinkedList()
        self._em_hash_to_node = {}

    def append(self, em_node):
        node = LinkedListNode(em_node)
        self._em_hash_to_node[em_node.hash] = node
        self._linked_list.add_node_before(None, node)

    def remove_by_hash(self, em_hash):
        self._linked_list.remove_node(self._em_hash_to_node[em_hash])
        del self._em_hash_to_node[em_hash]

    def __iter__(self):
        for node in self._linked_list:
            yield node.val

    def __str__(self):
        return ', '.join(([str(node) for node in self]))


class EffectManager:
    def __init__(self, game):
        self._em_node_hash_to_node = {}
        self._em_node_hash_to_events = collections.defaultdict(list)
        self._event_to_effect_node_list = {}  # event and slot_hash to effect node list
        self._slot_hash_to_em_node_list = collections.defaultdict(EffectManagerNodeList)
        self._game = game

    def add_effect(self, em_node):
        slot_hash = em_node.affected_slot.hash
        player = em_node.affected_slot.player

        self._em_node_hash_to_node[em_node.hash] = em_node
        for received_event in em_node.effect.events_received:
            self._em_node_hash_to_events[em_node.hash].append(received_event)
            if received_event not in self._event_to_effect_node_list:
                self._event_to_effect_node_list[received_event] = {
                    NULL_HASH: EffectManagerNodeList(),
                    PLAYER0_HASH: EffectManagerNodeList(),
                    PLAYER1_HASH: EffectManagerNodeList()
                }
            if em_node.effect.requires_slot_match_for_event:
                hash_to_em_node_list = self._event_to_effect_node_list[received_event]
                if slot_hash not in hash_to_em_node_list:
                    self._event_to_effect_node_list[received_event][slot_hash] = EffectManagerNodeList()
                self._event_to_effect_node_list[received_event][slot_hash].append(em_node)
            elif em_node.effect.requires_slot_player_match_for_event:
                self._event_to_effect_node_list[received_event][player].append(em_node)
            else:
                self._event_to_effect_node_list[received_event][NULL_HASH].append(em_node)

        em_node.start(self._game, self)

        self._slot_hash_to_em_node_list[slot_hash].append(em_node)

    def get_em_node_by_em_node_hash(self, effect_hash):
        return self._em_node_hash_to_node[effect_hash]

    def iter_em_nodes_by_slot_hash(self, slot_hash):
        for em_node in self._slot_hash_to_em_node_list.get(slot_hash, []):
            yield em_node

    def pop_effect(self, em_node):
        em_node_hash = em_node.hash
        em_node.stop(self._game, self)
        for event in self._em_node_hash_to_events[em_node_hash]:
            if em_node.effect.requires_slot_match_for_event:
                slot_hash = em_node.affected_slot.hash
            elif em_node.effect.requires_slot_player_match_for_event:
                slot_hash = em_node.affected_slot.player
            else:
                slot_hash = NULL_HASH
            self._event_to_effect_node_list[event][slot_hash].remove_by_hash(em_node.hash)

        self._slot_hash_to_em_node_list[em_node.affected_slot.hash].remove_by_hash(em_node_hash)
        del self._em_node_hash_to_node[em_node_hash]
        del self._em_node_hash_to_events[em_node_hash]

    def pop_effects_by_slot(self, card_slot):
        em_nodes = list(reversed(list(self._slot_hash_to_em_node_list[card_slot.hash])))
        for em_node in em_nodes:
            self.pop_effect(em_node)

    def send_event(self, event, event_slot=None):
        slot_hash_to_em_node = self._event_to_effect_node_list.get(event, None)
        if slot_hash_to_em_node:
            for em_node in slot_hash_to_em_node[NULL_HASH]:
                em_node.send_event(event, game=self._game, effect_manager=self, event_slot=event_slot)
            if event_slot:
                em_node_list = slot_hash_to_em_node.get(event_slot.player, None)
                if em_node_list:
                    for em_node in slot_hash_to_em_node[event_slot.player]:
                        em_node.send_event(event, game=self._game, effect_manager=self, event_slot=event_slot)
                em_node_list = slot_hash_to_em_node.get(event_slot.hash, None)
                if em_node_list:
                    for em_node in slot_hash_to_em_node[event_slot.hash]:
                        em_node.send_event(event, game=self._game, effect_manager=self, event_slot=event_slot)

    def log_state(self):
        lines = []
        lines.append('_em_node_hash_to_node')
        for k, v in self._em_node_hash_to_node.items():
            lines.append(f'\t{k} {v}')
        lines.append('_em_node_hash_to_events')
        for k, v in self._em_node_hash_to_events.items():
            lines.append(f'\t{k} {v}')
        lines.append('_event_to_effect_node_list')
        for event, em_node_hash_to_em_node_list in self._event_to_effect_node_list.items():
            lines.append(f'\t{event}')
            for k, v in em_node_hash_to_em_node_list.items():
                lines.append(f'\t\t{k} {v}')
        lines.append('_slot_hash_to_em_node_list')
        for k, v in self._slot_hash_to_em_node_list.items():
            lines.append(f'\t{k} {v}')

        self._game.ui_manager.log_text('\n'.join(lines))

    def __str__(self):
        result = []
        for hash, em_node_list in self._slot_hash_to_em_node_list.items():
            slot = self._game.hash_to_slot(hash)
            result.append(f'{slot}')
            for em_node in em_node_list:
                result.append(f'\t{em_node.effect}')
        return '\n'.join(result)

