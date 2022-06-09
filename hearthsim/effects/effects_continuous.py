from easydict import EasyDict as edict
from hearthsim.utils.enums import Events, EffectArea
from hearthsim.effects.core import ContinuousEffect, is_one_time_effect, ExternalEffect
from hearthsim.game.effect_manager import EffectManagerNodePlan, EffectManagerNode

class DivineShield(ContinuousEffect):
    _events_received = (Events.AFTER_ATTACKER_INITIAL_COMBAT_DAMAGE.value,
                        Events.AFTER_DEFENDER_INITIAL_COMBAT_DAMAGE.value)
    _requires_slot_match_for_event = True
    _effect_area = EffectArea.FIELD.value

    def start(self, game, em_node):
        pass

    def send_event(self, event, game, em_node, event_slot):
        assert event in self.events_received, (event, self.events_received)
        # handle dealing 0 damage ????
        if event == Events.AFTER_ATTACKER_INITIAL_COMBAT_DAMAGE.value:
            game.game_metadata.attacker_damage_taken = 0
        elif event == Events.AFTER_DEFENDER_INITIAL_COMBAT_DAMAGE.value:
            game.game_metadata.defender_damage_taken = 0
        else:
            raise ValueError(f'Incorrect event received: {event}')

        return EffectManagerNodePlan(to_remove=em_node)


class Taunt(ContinuousEffect):
    _effect_area = EffectArea.FIELD.value

    def start(self, game, em_node):
        em_node.affected_slot.n_taunt += 1
        if em_node.affected_slot.n_taunt == 1:
            game.battleboard.add_taunt(em_node.affected_slot)

    def stop(self, game, em_node):
        em_node.affected_slot.n_taunt -= 1
        assert em_node.affected_slot.n_taunt >= 0
        if em_node.affected_slot.n_taunt == 0:
            game.battleboard.remove_taunt(em_node.affected_slot)


class Charge(ContinuousEffect):
    _effect_area = EffectArea.FIELD.value

    def start(self, game, em_node):
        em_node.affected_slot.n_charge += 1

    def stop(self, game, em_node):
        em_node.affected_slot.n_charge -= 1
        assert em_node.affected_slot.n_charge >= 0


class Windfury(ContinuousEffect):
    _effect_area = EffectArea.FIELD.value

    def start(self, game, em_node):
        em_node.affected_slot.n_windfury += 1

    def stop(self, game, em_node):
        em_node.affected_slot.n_windfury -= 1
        assert em_node.affected_slot.n_windfury >= 0


class Stealth(ContinuousEffect):
    _events_received = (Events.AFTER_ATTACKER_ATTACKED.value,)
    _requires_slot_match_for_event = True
    _effect_area = EffectArea.FIELD.value

    def start(self, game, em_node):
        em_node.affected_slot.n_stealth += 1

    def stop(self, game, em_node):
        em_node.affected_slot.n_stealth -= 1
        assert em_node.affected_slot.n_stealth >= 0

    def send_event(self, event, game, em_node, event_slot):
        assert event in self.events_received, (event, self.events_received)
        return EffectManagerNodePlan(to_remove=em_node)


class CantBeTargetedBySpellsOrHP(ContinuousEffect):
    _effect_area = EffectArea.FIELD.value

    def start(self, game, em_node):
        pass


class Sleep(ContinuousEffect):
    _events_received = (Events.END_TURN.value,)

    def start(self, game, em_node):
        em_node.affected_slot.has_sleep = True

    def send_event(self, event, game, em_node, event_slot):
        assert event in self.events_received
        return EffectManagerNodePlan(to_remove=[em_node])

    def stop(self, game, em_node):
        em_node.affected_slot.has_sleep = False


class AttackBuff(ContinuousEffect):
    _effect_area = EffectArea.ALL.value

    def __init__(self, amount):
        self.amount = amount
        if not callable(amount) and amount <= 0:
            raise ValueError('AttackBuff must have a positive amount argument')

    def adjust_stats(self, card_slot):
        card_slot.attack += self.amount

    def start(self, game, em_node):
        pass


class HealthBuff(ContinuousEffect):
    _effect_area = EffectArea.ALL.value

    def __init__(self, amount):
        self.amount = amount
        if not callable(amount) and amount <= 0:
            raise ValueError('HealthBuff must have a positive amount argument')

    def adjust_stats(self, card_slot):
        card_slot.max_health += self.amount
        card_slot.health += self.amount

    def start(self, game, em_node):
        pass


class Buff(ContinuousEffect):
    _effect_area = EffectArea.ALL.value

    def __init__(self, attack_amount, health_amount):
        self.attack_amount = attack_amount
        self.health_amount = health_amount
        if ((not callable(attack_amount) and attack_amount <= 0) or
                (not callable(health_amount) and health_amount <= 0)):
            raise ValueError('Buff must have positive amount arguments')

    def adjust_stats(self, card_slot):
        card_slot.attack += self.attack_amount
        card_slot.max_health += self.health_amount
        card_slot.health += self.health_amount

    def start(self, game, em_node):
        pass


class ContinuousSelectionFieldEffect(ContinuousEffect):
    _effect_area = EffectArea.FIELD.value
    _requires_slot_player_match_for_event = True

    def __init__(self, selection, effect):
        super(ContinuousSelectionFieldEffect, self).__init__()
        self.effect = effect
        if is_one_time_effect(self.effect):
            raise ValueError("ContinuousSelectionFieldEffect doesn't expect a one-time effect")
        self.selection = selection
        # (using regular dict because edict automatically converts dict to edict and throws error when you use CardSlot
        # as a key)
        self.memory = dict()  # maps slots to EffectManagerNodes
        self.memory['current_selection'] = dict()

    def start(self, game, em_node):
        pass

    def send_event(self, event, game, em_node, event_slot):
        assert event in self.events_received
        prev_selected_slots = set(self.memory['current_selection'].keys())
        selected_card_slots = set(self.selection.get_selected_card_slots(game, em_node))

        plan = EffectManagerNodePlan()

        for card_slot in (prev_selected_slots - selected_card_slots):
            plan.to_remove.append(self.memory['current_selection'][card_slot])
            del self.memory['current_selection'][card_slot]

        for card_slot in (selected_card_slots - prev_selected_slots):
            effect = ExternalEffect(self.effect.copy())
            node = EffectManagerNode(effect=effect, affected_slot=card_slot, origin_slot=em_node.affected_slot,
                                     silenceable=False)
            plan.to_add.append(node)
            self.memory['current_selection'][card_slot] = node

        return plan

    @property
    def events_received(self):
        return self.effect.events_received + self.selection.events_received


class Frozen(ContinuousEffect):
    _events_received = (Events.AFTER_ATTACKER_ATTACKED.value,)
    _effect_area = EffectArea.FIELD.value

    def start(self, game, em_node):
        em_node.affected_slot.n_frozen += 1

    def stop(self, game, em_node):
        em_node.affected_slot.n_frozen -= 1
        assert em_node.affected_slot.n_frozen >= 0

    def send_event(self, event, game, em_node, event_slot):
        assert event in self.events_received, (event, self.events_received)
        if em_node.affected_slot.attacks_this_turn < em_node.affected_slot.n_possible_attacks_ignoring_frozen:
            return EffectManagerNodePlan(to_remove=em_node)