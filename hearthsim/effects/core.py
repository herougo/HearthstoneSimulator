from hearthsim.utils.utils import deep_copy

class Effect:
    _events_received = tuple()
    _requires_slot_match_for_event = False

    @property
    def is_compound_effect(self):
        return hasattr(self, 'effect')

    @property
    def requires_slot_match_for_event(self):
        return self._requires_slot_match_for_event

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


class OneTimeEffect(Effect):
    _events_received = tuple()

    def execute(self, game, em_node):
        raise NotImplementedError()

    @property
    def events_received(self):
        assert not self._events_received  # one-time effects cannot receive events (not continuous)
        return self._events_received


class TriggerEffect(Effect):
    def __init__(self, effect):
        super(TriggerEffect, self).__init__()
        self.effect = effect
        if not is_one_time_effect(effect):
            raise ValueError('ActivatedEffect only takes one-time effects as arguments')

    def start(self, game, em_node):
        pass

    def stop(self, game, em_node):
        pass

class ActivatedEffect(TriggerEffect):
    # these effects are "triggered" by events caused by user input (e.g. "hero_power")

    def send_event(self, event, game, em_node):
        assert event in self.events_received
        self.effect.execute(game, em_node)


class ConditionalEffect(Effect):
    def __init__(self, condition, effect):
        super(ConditionalEffect, self).__init__()
        self.effect = effect
        self.condition = condition
        self.memory = False  # current condition evaluation

    @property
    def events_received(self):
        return self.condition.events_received + self.effect.events_received

    def _check_condition_and_affect_effect(self, game, em_node):
        prev_condition_evaluation = self.memory
        self.memory = self.condition.evaluate(game, em_node)

        if prev_condition_evaluation != self.memory:
            if self.memory:  # turn on
                plan = self.effect.start(game, em_node)
            else:  # turn off
                plan = self.effect.stop(game, em_node)
            if plan:
                raise ValueError(f'ConditionalEffect cannot handle EffectManagerNodePlan objects {em_node}')

    def start(self, game, em_node):
        self._check_condition_and_affect_effect(game, em_node)

    def stop(self, game, em_node):
        if self.memory:
            plan = self.effect.stop(game, em_node)
            if plan:
                raise ValueError(f'ConditionalEffect cannot handle EffectManagerNodePlan objects {em_node}')

    def send_event(self, event, game, em_node):
        if event in self.condition.events_received:
            self._check_condition_and_affect_effect(game, em_node)

        if self.memory and (event in self.effect.events_received):
            return self.effect.send_event(event, game, em_node)

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

    def send_event(self, event, game, em_node):
        return self.effect.send_event(event, game, em_node)

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