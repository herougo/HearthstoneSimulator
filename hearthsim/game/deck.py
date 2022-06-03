DECK_N_CARDS = 30

class Deck:
    def __init__(self, card_id_list, cls):
        self.card_id_list = card_id_list
        self.cls = cls

    def is_valid_deck(self):
        return len(self.card_id_list) == DECK_N_CARDS