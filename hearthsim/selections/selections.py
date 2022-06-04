from hearthsim.selections.core import CharacterSelection
from hearthsim.utils.enums import PlayerChoice, Events
from hearthsim.effects.effects_activated import HeroPowerEffect
from hearthsim.game.utils import targetable_with_hero_power


class SelectCharacter(CharacterSelection):
    def get_selected_card_slots(self, game, em_node):
        player = em_node.origin_slot.player
        if (isinstance(em_node.effect, HeroPowerEffect) and
                (not game.get_card_slots_targetable_by_hp(player, PlayerChoice.both.value))):
            return tuple()

        while True:
            _, selection = game.decision_makers[player].get_unverified_selection()
            selection_player, selection_board_index = selection
            targeted_slot = game.index_to_slot(selection_player, selection_board_index)

            if (isinstance(em_node.effect, HeroPowerEffect) and
                    (not targetable_with_hero_power(player, targeted_slot))):
                game.ui_manager.log_line("ERROR: SelectCharacter - selection can't be targeted by hero powers")
                continue

            return (targeted_slot,)


class SelectFriendlyMinion(CharacterSelection):
    def get_selected_card_slots(self, game, em_node):
        origin_card_slot = em_node.origin_slot
        player = origin_card_slot.player
        player_board_index = game.battleboard.hash_to_board_index(origin_card_slot.hash)
        if player_board_index:
            exclusion_options = {player_board_index[1]}
        else:
            exclusion_options = set()

        if game.battleboard.board_len(player) - len(exclusion_options) == 0:
            return tuple()

        while True:
            _, selection = game.decision_makers[player].get_unverified_selection()
            selection_player, selection_board_index = selection
            if selection_player is None:
                selection_player = player
            if selection_player != player:
                game.ui_manager.log_line('ERROR: SelectFriendlyMinion - selection needs to match players')
                continue

            board_len = game.battleboard.board_len(player)
            if selection_board_index < 0 and board_len <= selection_board_index:
                game.ui_manager.log_line(
                    'ERROR: SelectFriendlyMinion - selection needs to be within the bounds of the battleboard')
                continue

            if selection_board_index in exclusion_options:
                game.ui_manager.log_line('ERROR: SelectFriendlyMinion - selection cannot be itself')
                continue

            return (game.battleboard.get_slot(player, selection_board_index),)


class RandomOtherCharacter(CharacterSelection):
    def get_selected_card_slots(self, game, em_node):
        raise NotImplementedError()


class HeroSelection(CharacterSelection):
    def __init__(self, opposing=False):
        self.opposing = opposing

    def get_selected_card_slots(self, game, em_node):
        origin_card_slot = em_node.origin_slot
        if self.opposing:
            player = 1 - origin_card_slot.player
        else:
            player = origin_card_slot.player
        return (game.players[player],)


class OwnSelf(CharacterSelection):
    def get_selected_card_slots(self, game, em_node):
        raise NotImplementedError()


class AllFriendlyCharacters(CharacterSelection):
    _events_received = (Events.minion_dies.value,
                        Events.minion_put_in_play.value)

    def get_selected_card_slots(self, game, em_node):
        origin_card_slot = em_node.origin_slot
        player_slot = game.players[origin_card_slot.player]
        minion_slots = tuple(game.battleboard.iter_board(origin_card_slot.player))
        return (player_slot,) + minion_slots


class AdjacentMinions(CharacterSelection):
    _events_received = (Events.minion_dies.value,
                        Events.minion_put_in_play.value)

    def get_selected_card_slots(self, game, em_node):
        raise NotImplementedError()