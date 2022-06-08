from easydict import EasyDict as edict
from hearthsim.utils.enums import Events, EffectTimeLimit
from hearthsim.effects.core import WrappedEffect, is_one_time_effect
from hearthsim.game.effect_manager import EffectManagerNodePlan


class TimeLimitedEffect(WrappedEffect):
    _events_received = (Events.END_TURN.value,)

    def __init__(self, effect, until_when):
        super(TimeLimitedEffect, self).__init__(effect)
        self.until_when = until_when
        self.memory = edict({'player': None})  # turn the effect started

    def start(self, game, em_node):
        result = self.effect.start(game, em_node)
        if result:
            for em_node in result.to_add:
                em_node.effect = TimeLimitedEffect(em_node.effect, self.until_when)
        self.memory.player = em_node.affected_slot.player
        return result

    def execute(self, game, em_node):
        result = self.effect.execute(game, em_node)
        if result:
            for em_node in result.to_add:
                em_node.effect = TimeLimitedEffect(em_node.effect, self.until_when)
        return result

    def _is_time_up(self, ending_turn):
        if self.until_when == EffectTimeLimit.NO_LIMIT.value:
            return False
        elif self.until_when == EffectTimeLimit.END_OF_TURN.value:
            return True
        elif self.until_when == EffectTimeLimit.END_OF_OPP_TURN.value:
            return ending_turn != self.memory.player
        else:
            raise ValueError('_is_time_up encountered an unknown until_when value')

    def send_event(self, event, game, em_node):
        assert event in self.events_received

        if (event == Events.END_TURN.value and
                self._is_time_up(game.game_metadata.turn)):
            return EffectManagerNodePlan(to_remove=[em_node])
        elif event in self.effect.events_received:
            self.effect.send_event(event, game, em_node)


class NEffects(WrappedEffect):
    def __init__(self, effect, n):
        super(NEffects, self).__init__(effect)
        if not is_one_time_effect(effect):
            raise ValueError('NEffects only works with one-time effect classes')
        self.n = n

    def execute(self, game, em_node):
        for i in range(self.n):
            self.effect.execute(game, em_node)