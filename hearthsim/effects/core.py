from easydict import EasyDict as edict
from hearthsim.utils.utils import deep_copy
from hearthsim.game.effect_manager import EffectManagerNodePlan

class Effect:
    _events_received = tuple()
    _requires_slot_match_for_event = False
    _requires_slot_player_match_for_event = False

    @property
    def is_compound_effect(self):
        return hasattr(self, 'effect')

    @property
    def requires_slot_match_for_event(self):
        return self._requires_slot_match_for_event

    @property
    def requires_slot_player_match_for_event(self):
        return self._requires_slot_player_match_for_event

    @property
    def events_received(self):
        '''
        if self.is_compound_effect:
            return self._events_received + self.effect.events_received
        else:
            return self._events_received
        '''
        return self._events_received

    def adjust_stats(self, card_slot):
        pass

    @property
    def effect_area(self):
        return self._effect_area

    def copy(self):
        return deep_copy(self)


class ContinuousEffect(Effect):
    def start(self, game, em_node):
        raise NotImplementedError()

    def stop(self, game, em_node):
        pass


class GroupContinuousEffect(Effect):
    # made of multiple continuous effects
    def __init__(self, effects):
        super(GroupContinuousEffect, self).__init__()
        self.effects = effects
        for effect in self.effects:
            if is_one_time_effect(effect):
                raise ValueError('GroupContinuousEffect only takes non-one-time effects as arguments')

    def start(self, game, em_node):
        plan = EffectManagerNodePlan()
        for effect in self.effects:
            new_plan = effect.start(game, em_node)
            plan.update(new_plan)
        if not plan.is_empty():
            return plan

    def stop(self, game, em_node):
        plan = EffectManagerNodePlan()
        for effect in self.effects:
            new_plan = effect.stop(game, em_node)
            plan.update(new_plan)
        if not plan.is_empty():
            return plan

    def adjust_stats(self, card_slot):
        for effect in self.effects:
            effect.adjust_stats(card_slot)

    @property
    def events_received(self):
        result = []
        for effect in self.effects:
            result.extend(list(effect.events_received))
        return tuple(result)


class OneTimeEffect(Effect):
    _events_received = tuple()

    def execute(self, game, em_node):
        raise NotImplementedError()

    @property
    def events_received(self):
        assert not self._events_received  # one-time effects cannot receive events (not continuous)
        return self._events_received


class OneTimeEffectSequence(OneTimeEffect):
    def __init__(self, effects):
        super(OneTimeEffectSequence, self).__init__()
        self.effects = effects
        for effect in self.effects:
            if not is_one_time_effect(effect):
                raise ValueError('OneTimeEffectSequence only takes one-time effects as arguments')

    def execute(self, game, em_node):
        plan = EffectManagerNodePlan()
        for effect in self.effects:
            new_plan = effect.execute(game, em_node)
            plan.update(new_plan)
        return plan


class TriggerEffect(Effect):
    def __init__(self, effect):
        super(TriggerEffect, self).__init__()
        if isinstance(effect, (tuple, list)):
            effect = OneTimeEffectSequence(effect)
        self.effect = effect
        if not is_one_time_effect(effect):
            raise ValueError('ActivatedEffect only takes one-time effects as arguments')

    def start(self, game, em_node):
        pass

    def stop(self, game, em_node):
        pass


class ActivatedEffect(TriggerEffect):
    # these effects are "triggered" by events caused by user input (e.g. "hero_power")

    def send_event(self, event, game, em_node, event_slot):
        assert event in self.events_received
        self.effect.execute(game, em_node)


class ConditionalEffect(Effect):
    def __init__(self, condition, effect):
        super(ConditionalEffect, self).__init__()
        if isinstance(effect, (tuple, list)):
            effect = GroupContinuousEffect(effect)
        self.effect = effect
        self.condition = condition
        self.memory = edict({'current_cond_eval': False})  # current condition evaluation

    @property
    def events_received(self):
        return self.condition.events_received + self.effect.events_received

    def _check_condition_and_affect_effect(self, game, em_node):
        prev_condition_evaluation = self.memory.current_cond_eval
        self.memory.current_cond_eval = self.condition.evaluate(game, em_node)

        if prev_condition_evaluation != self.memory.current_cond_eval:
            if self.memory.current_cond_eval:  # turn on
                plan = self.effect.start(game, em_node)
            else:  # turn off
                plan = self.effect.stop(game, em_node)
            if plan:
                raise ValueError(f'ConditionalEffect cannot handle EffectManagerNodePlan objects {em_node}')

    def start(self, game, em_node):
        self._check_condition_and_affect_effect(game, em_node)

    def stop(self, game, em_node):
        if self.memory.current_cond_eval:
            plan = self.effect.stop(game, em_node)
            if plan:
                raise ValueError(f'ConditionalEffect cannot handle EffectManagerNodePlan objects {em_node}')

    def send_event(self, event, game, em_node, event_slot):
        if event in self.condition.events_received:
            self._check_condition_and_affect_effect(game, em_node)

        if self.memory.current_cond_eval and (event in self.effect.events_received):
            return self.effect.send_event(event, game, em_node, event_slot)

    def adjust_stats(self, card_slot):
        return self.effect.adjust_stats(card_slot)


class WrappedEffect(Effect):
    # A compound effect whose affect area solely depends on the contained effect.
    def __init__(self, effect):
        super(WrappedEffect, self).__init__()
        self.effect = effect

    @property
    def effect_area(self):
        return self.effect.effect_area

    def adjust_stats(self, card_slot):
        return self.effect.adjust_stats(card_slot)

    def send_event(self, event, game, em_node, event_slot):
        return self.effect.send_event(event, game, em_node, event_slot)

    def start(self, game, em_node):
        return self.effect.start(game, em_node)

    def stop(self, game, em_node):
        return self.effect.stop(game, em_node)

    @property
    def events_received(self):
        if is_one_time_effect(self.effect):
            return self._events_received
        else:
            return self._events_received + self.effect.events_received


class ExternalEffect(WrappedEffect):
    # cannot be silenced
    def __init__(self, effect):
        super(ExternalEffect, self).__init__(effect)


def is_one_time_effect(effect):
    if effect.is_compound_effect:
        return is_one_time_effect(effect.effect)
    else:
        return isinstance(effect, OneTimeEffect)
