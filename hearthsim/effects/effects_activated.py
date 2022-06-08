from hearthsim.utils.enums import Events
from hearthsim.effects.core import ActivatedEffect

class HeroPowerEffect(ActivatedEffect):
    _events_received = (Events.ACTIVATE_HERO_POWER.value,)
    _requires_slot_match_for_event = True

    def send_event(self, event, game, em_node, event_slot):
        assert event in self.events_received
        self.effect.execute(game, em_node)
        game.players[em_node.affected_slot.player].hero_power_used_this_turn = True