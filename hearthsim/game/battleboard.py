from hearthsim.utils.pile import Pile
from hearthsim.utils.constants import DEBUG

class Battleboard:
    def __init__(self, game):
        self._game = game
        self._boards = (Pile(), Pile())
        self._card_slot_to_board_index = {}
        self._taunts = (set(), set())

    def add_cards(self, player, cards, index=None):
        if index is None:
            board_index = len(self._boards[player])
            for card in cards:
                self._card_slot_to_board_index[card] = (player, board_index)
                board_index += 1
        else:
            board_index = index
            for card in cards:
                self._card_slot_to_board_index[card] = (player, board_index)
                board_index += 1
            for card in self._boards[player][index:]:
                self._card_slot_to_board_index[card] = (player, board_index)
                board_index += 1

        self._boards[player].add_cards(cards, index=index)
        if DEBUG:
            self._check_card_slot_to_board_index()

    def pop_card_slot(self, card_slot):
        # remove from the board
        player, original_board_index = self._card_slot_to_board_index[card_slot]

        del self._card_slot_to_board_index[card_slot]
        for board_index in range(original_board_index + 1, self.board_len(player)):
            current_card_slot = self._boards[player][board_index]
            self._card_slot_to_board_index[current_card_slot] = (player, board_index - 1)

        self._boards[player].pop(original_board_index)

        if DEBUG:
            self._check_card_slot_to_board_index()

    def _check_card_slot_to_board_index(self):
        for player in range(2):
            for board_index, card in enumerate(self._boards[player]):
                assert self._card_slot_to_board_index[card] == (player, board_index), (player, board_index)

    def iter_board(self, player):
        for slot in self._boards[player]:
            yield slot

    def board_len(self, player):
        return len(self._boards[player])

    def get_slot(self, player, ix):
        return self._boards[player].get(ix, None)

    def card_slot_to_board_index(self, card_slot):
        return self._card_slot_to_board_index.get(card_slot, None)

    def add_taunt(self, card_slot):
        assert card_slot not in self._taunts[card_slot.player]
        self._taunts[card_slot.player].add(card_slot)

    def remove_taunt(self, card_slot):
        self._taunts[card_slot.player].remove(card_slot)

    def defender_obeys_taunt(self, defender_card_slot):
        taunts = self._taunts[defender_card_slot.player]
        return defender_card_slot and (defender_card_slot not in taunts)

    def has_room(self, player):
        return self.board_len(player) < self._game.player_metadata[player].battleboard_limit