from hearthsim.utils.utils import deep_copy
from hearthsim.game.utils import targetable_with_hero_power
from hearthsim.effects.effects_activated import HeroPowerEffect


def _filter_based_on_em_node(options, em_node):
    options = set(options)
    targeting_player = em_node.affected_slot.player
    result = []
    for card_slot_to_target in options:
        if isinstance(em_node.effect, HeroPowerEffect):
            if targetable_with_hero_power(targeting_player, card_slot_to_target):
                result.append(card_slot_to_target)
        else:
            result.append(card_slot_to_target)
    return set(result)


class CharacterSelection:
    _events_received = tuple()

    def get_selected_card_slots(self, game, em_node):
        raise NotImplementedError()

    @property
    def events_received(self):
        return self._events_received

    def copy(self):
        return deep_copy(self)


class SelectCharacterFrom(CharacterSelection):
    def __init__(self, selection):
        self.selection = selection

    def get_selected_card_slots(self, game, em_node):
        player = em_node.affected_slot.player
        options = self.selection.get_selected_card_slots(game, em_node)
        options = _filter_based_on_em_node(options, em_node)
        if not options:
            return (game.decision_makers[player].get_verified_selection(options),)
        else:
            return tuple()