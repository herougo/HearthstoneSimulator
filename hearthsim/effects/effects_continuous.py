from hearthsim.utils.enums import (Events, EffectArea)
from hearthsim.effects.core import (ContinuousEffect, is_one_time_effect)
from hearthsim.game.effect_manager import EffectManagerNodePlan

class DivineShield(ContinuousEffect):
    _events_received = (Events.after_attacker_initial_combat_damage.value,
                        Events.after_defender_initial_combat_damage.value)
    _requires_slot_match_for_event = True
    _effect_area = EffectArea.field.value

    def start(self, game, em_node):
        pass

    def send_event(self, event, game, em_node):
        assert event in self.events_received, (event, self.events_received)
        # handle dealing 0 damage ????
        if event == Events.after_attacker_initial_combat_damage.value:
            game.game_metadata.attacker_damage_taken = 0
        elif event == Events.after_defender_initial_combat_damage.value:
            game.game_metadata.defender_damage_taken = 0
        else:
            raise ValueError(f'Incorrect event received: {event}')

        return EffectManagerNodePlan(to_remove=em_node)


class Taunt(ContinuousEffect):
    _effect_area = EffectArea.field.value

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
    _effect_area = EffectArea.field.value

    def start(self, game, em_node):
        em_node.affected_slot.n_charge += 1

    def stop(self, game, em_node):
        em_node.affected_slot.n_charge -= 1
        assert em_node.affected_slot.n_charge >= 0


class Windfury(ContinuousEffect):
    _effect_area = EffectArea.field.value

    def start(self, game, em_node):
        em_node.affected_slot.n_windfury += 1

    def stop(self, game, em_node):
        em_node.affected_slot.n_windfury -= 1
        assert em_node.affected_slot.n_windfury >= 0


class Stealth(ContinuousEffect):
    _events_received = (Events.after_attacker_attacked.value,)
    _requires_slot_match_for_event = True
    _effect_area = EffectArea.field.value

    def start(self, game, em_node):
        em_node.affected_slot.n_stealth += 1

    def stop(self, game, em_node):
        em_node.affected_slot.n_stealth -= 1
        assert em_node.affected_slot.n_stealth >= 0

    def send_event(self, event, game, em_node):
        assert event in self.events_received, (event, self.events_received)
        return EffectManagerNodePlan(to_remove=em_node)


class CantBeTargetedBySpellsOrHP(ContinuousEffect):
    _effect_area = EffectArea.field.value

    def start(self, game, em_node):
        pass


class Sleep(ContinuousEffect):
    _events_received = (Events.end_turn.value,)

    def start(self, game, em_node):
        em_node.affected_slot.has_sleep = True

    def send_event(self, event, game, em_node):
        assert event in self.events_received
        return EffectManagerNodePlan(to_remove=[em_node])

    def stop(self, game, em_node):
        em_node.affected_slot.has_sleep = False


class AttackBuff(ContinuousEffect):
    _effect_area = EffectArea.all.value

    def __init__(self, amount):
        self.amount = amount
        if not callable(amount) and amount <= 0:
            raise ValueError('AttackBuff must have a positive amount argument')

    def adjust_stats(self, card_slot):
        card_slot.attack += self.amount

    def start(self, game, em_node):
        pass


class HealthBuff(ContinuousEffect):
    _effect_area = EffectArea.all.value

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
    _effect_area = EffectArea.all.value

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
    _effect_area = EffectArea.field.value

    def __init__(self, selection, effect):
        super(ContinuousSelectionFieldEffect, self).__init__()
        self.effect = effect
        if is_one_time_effect(self.effect):
            raise ValueError("ContinuousSelectionFieldEffect doesn't expect a one-time effect")
        self.selection = selection

    def start(self, game, em_node):
        return self.effect.start(game, em_node)

    @property
    def events_received(self):
        return (self._events_received + self.effect.events_received +
                self.selection.events_received)