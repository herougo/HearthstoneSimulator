import random
from hearthsim.selections.core import CharacterSelection
from hearthsim.utils.enums import Events


class RandomCharacter(CharacterSelection):
    def __init__(self, selection):
        self.selection = selection

    def get_selected_card_slots(self, game, em_node):
        possible_card_slots = self.selection.get_selected_card_slots(game, em_node)
        if not possible_card_slots:
            return tuple()

        chosen = random.randint(0, len(possible_card_slots) - 1)
        return (possible_card_slots[chosen],)


class HeroSelection(CharacterSelection):
    def __init__(self, opposing=False):
        self.opposing = opposing

    def get_selected_card_slots(self, game, em_node):
        card_slot = em_node.affected_slot
        if self.opposing:
            player = 1 - card_slot.player
        else:
            player = card_slot.player
        return (game.players[player],)


class OwnSelf(CharacterSelection):
    def get_selected_card_slots(self, game, em_node):
        return (em_node.affected_slot,)


class AllFriendlyCharacters(CharacterSelection):
    _events_received = (Events.MINION_DIES.value,
                        Events.MINION_PUT_IN_PLAY.value)

    def get_selected_card_slots(self, game, em_node):
        card_slot = em_node.affected_slot
        player_slot = game.players[card_slot.player]
        minion_slots = tuple(game.battleboard.iter_board(card_slot.player))
        return (player_slot,) + minion_slots


class AllFriendlyMinions(CharacterSelection):
    _events_received = (Events.MINION_DIES.value,
                        Events.MINION_PUT_IN_PLAY.value)

    def get_selected_card_slots(self, game, em_node):
        card_slot = em_node.affected_slot
        minion_slots = tuple(game.battleboard.iter_board(card_slot.player))
        return minion_slots


class AllOtherFriendlyCharacters(CharacterSelection):
    _events_received = (Events.MINION_DIES.value,
                        Events.MINION_PUT_IN_PLAY.value)

    def get_selected_card_slots(self, game, em_node):
        card_slot = em_node.affected_slot
        player_slot = game.players[card_slot.player]
        minion_slots = list(game.battleboard.iter_board(card_slot.player))
        slots = [player_slot] + minion_slots
        slots = [slot for slot in slots if slot != em_node.affected_slot]
        return tuple(slots)


class AllOtherFriendlyMinions(CharacterSelection):
    _events_received = (Events.MINION_DIES.value,
                        Events.MINION_PUT_IN_PLAY.value)

    def get_selected_card_slots(self, game, em_node):
        card_slot = em_node.affected_slot
        minion_slots = tuple([slot for slot in game.battleboard.iter_board(card_slot.player)
                              if slot != em_node.affected_slot])
        return minion_slots


class AllOtherCharacters(CharacterSelection):
    _events_received = (Events.MINION_DIES.value,
                        Events.MINION_PUT_IN_PLAY.value)

    def get_selected_card_slots(self, game, em_node):
        slots = set(list(game.battleboard.iter_board(0)) +
                    list(game.battleboard.iter_board(1)) +
                    list(game.players))
        slots -= {em_node.affected_slot}
        return tuple(sorted(list(slots)))


class AllOtherMinions(CharacterSelection):
    _events_received = (Events.MINION_DIES.value,
                        Events.MINION_PUT_IN_PLAY.value)

    def get_selected_card_slots(self, game, em_node):
        slots = set(list(game.battleboard.iter_board(0)) +
                    list(game.battleboard.iter_board(1)))
        slots -= {em_node.affected_slot}
        return tuple(sorted(list(slots)))


class AllCharacters(CharacterSelection):
    _events_received = (Events.MINION_DIES.value,
                        Events.MINION_PUT_IN_PLAY.value)

    def get_selected_card_slots(self, game, em_node):
        slots = set(list(game.battleboard.iter_board(0)) +
                    list(game.battleboard.iter_board(1)) +
                    list(game.players))
        return tuple(sorted(list(slots)))


class AdjacentMinions(CharacterSelection):
    _events_received = (Events.MINION_DIES.value,
                        Events.MINION_PUT_IN_PLAY.value)

    def get_selected_card_slots(self, game, em_node):
        card_slot = em_node.affected_slot
        board_index = game.battleboard.card_slot_to_board_index(card_slot)
        if not board_index:
            return tuple()
        neighbour1 = (board_index[0], board_index[1] - 1)
        neighbour2 = (board_index[0], board_index[1] + 1)
        proposed_neighbours = (neighbour1, neighbour2)
        result = [
            game.index_to_slot(proposed_neighbour)
            for proposed_neighbour in proposed_neighbours
            if 0 <= proposed_neighbour[1] and proposed_neighbour[1] < game.battleboard.board_len(card_slot.player)
        ]
        return tuple(result)
