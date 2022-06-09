import unittest
from hearthsim.cards.core import Card
from hearthsim.cards.card_registry import CARD_REGISTRY
from test.utils import generate_class


def main():
    # Note: modifying __init__ of a TestCase object throws an error
    class TestBasicsOfCardIdBaseClass(unittest.TestCase):
        card_id = None

        def test_card_constructor(self):
            Card.from_card_id(card_id=self.card_id)

    for card_id in sorted(CARD_REGISTRY.keys()):
        name = f'TestBasicsOfCardId{card_id}'
        gen_class = generate_class(name, TestBasicsOfCardIdBaseClass)
        gen_class.card_id = card_id
        globals()[name] = gen_class


main()
