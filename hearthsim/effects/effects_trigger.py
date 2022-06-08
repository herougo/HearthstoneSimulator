from hearthsim.utils.enums import (Events, EffectArea, PlayerChoice)
from hearthsim.effects.core import TriggerEffect
from hearthsim.game.utils import is_player_affected

class WhenMinionDies(TriggerEffect):
    _events_received = (Events.MINION_DIES.value,)

    def __init__(self, effect):
        super(WhenMinionDies, self).__init__(effect)

    def start(self, game, em_node):
        raise NotImplementedError()


class OnTurnStart(TriggerEffect):
    _events_received = (Events.START_TURN.value,)

    def __init__(self, effect, player_choice=PlayerChoice.PLAYER.value):
        super(OnTurnStart, self).__init__(effect)
        self.player_choice = player_choice

    def start(self, game, em_node):
        pass

    def send_event(self, event, game, em_node):
        assert event in self.events_received
        if is_player_affected(em_node.affected_slot.player, game.game_metadata.turn,
                              self.player_choice):
            return self.effect.execute(game, em_node)

        return None


class OnTurnEnd(TriggerEffect):
    _events_received = (Events.END_TURN.value,)

    def __init__(self, effect, player_choice=PlayerChoice.PLAYER.value):
        super(OnTurnEnd, self).__init__(effect)
        self.player_choice = player_choice

    def start(self, game, em_node):
        pass

    def send_event(self, event, game, em_node):
        assert event in self.events_received
        if is_player_affected(em_node.affected_slot.player, game.game_metadata.turn,
                              self.player_choice):
            return self.effect.execute(game, em_node)

        return None


class Battlecry(TriggerEffect):
    _events_received = (Events.MINION_BATTLECRY.value,)
    _requires_slot_match_for_event = True
    _effect_area = EffectArea.FIELD.value

    def __init__(self, effect):
        super(Battlecry, self).__init__(effect)

    def start(self, game, em_node):
        pass

    def send_event(self, event, game, em_node):
        assert event in self.events_received, (event, self.events_received)
        return self.effect.execute(game, em_node)


class Deathrattle(TriggerEffect):
    _events_received = (Events.MINION_DIES.value,)
    _requires_slot_match_for_event = True
    _effect_area = EffectArea.FIELD.value

    def __init__(self, effect):
        super(Deathrattle, self).__init__(effect)

    def start(self, game, em_node):
        pass

    def send_event(self, event, game, em_node):
        assert event in self.events_received, (event, self.events_received)
        return self.effect.execute(game, em_node)