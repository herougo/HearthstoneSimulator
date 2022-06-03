from hearthsim.cards.card_registry import CARD_REGISTRY


class Card:
    card_id = None
    collectible = True

    @classmethod
    def from_card_id(self, card_id):
        return CARD_REGISTRY[card_id]()

    @property
    def card_type(self):
        raise NotImplementedError()
