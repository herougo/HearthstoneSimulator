from hearthsim.utils.pile import Pile
from hearthsim.utils.constants import DEBUG

class Battleboard:
    def __init__(self, game):
        self._game = game
        self._boards = (Pile(), Pile())
        self._hash_to_board_index = {}
        self._taunt_hashes = (set(), set())

    def add_cards(self, player, cards, index=None):
        if index is None:
            board_index = len(self._boards[player])
            for card in cards:
                self._hash_to_board_index[card.hash] = (player, board_index)
                board_index += 1
        else:
            board_index = index
            for card in cards:
                self._hash_to_board_index[card.hash] = (player, board_index)
                board_index += 1
            for card in self._boards[player][index:]:
                self._hash_to_board_index[card.hash] = (player, board_index)
                board_index += 1

        self._boards[player].add_cards(cards, index=index)
        if DEBUG:
            self._check_hash_to_board_index()

    def pop_card_slot(self, card_slot):
        # remove from the board
        player, original_board_index = self._hash_to_board_index[card_slot.hash]

        del self._hash_to_board_index[card_slot.hash]
        for board_index in range(original_board_index + 1, self.board_len(player)):
            current_card_slot_hash = self._boards[player][board_index].hash
            self._hash_to_board_index[current_card_slot_hash] = (player, board_index - 1)

        self._boards[player].pop(original_board_index)

        if DEBUG:
            self._check_hash_to_board_index()

    def _check_hash_to_board_index(self):
        for player in range(2):
            for board_index, card in enumerate(self._boards[player]):
                assert self._hash_to_board_index[card.hash] == (player, board_index), (player, board_index)

    def iter_board(self, player):
        for slot in self._boards[player]:
            yield slot

    def board_len(self, player):
        return len(self._boards[player])

    def get_slot(self, player, ix):
        return self._boards[player].get(ix, None)

    def card_slot_to_board_index(self, card_slot):
        return self._hash_to_board_index.get(card_slot.hash, None)

    def add_taunt(self, card_slot):
        assert card_slot.hash not in self._taunt_hashes[card_slot.player]
        self._taunt_hashes[card_slot.player].add(card_slot.hash)

    def remove_taunt(self, card_slot):
        self._taunt_hashes[card_slot.player].remove(card_slot.hash)

    def defender_obeys_taunt(self, defender_card_slot):
        taunt_hashes = self._taunt_hashes[defender_card_slot.player]
        return defender_card_slot and (defender_card_slot.hash not in taunt_hashes)
