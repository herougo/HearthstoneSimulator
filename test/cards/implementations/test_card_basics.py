import unittest
from hearthsim.cards.core import Card
from hearthsim.cards.types_of_cards import MinionCard, WeaponCard, SpellCard, OriginalHeroCard
from hearthsim.cards.card_registry import CARD_REGISTRY
from hearthsim.utils.enums import HSClass
from hearthsim.game.deck import Deck
from hearthsim.utils.decision_maker_text import split_text_by_player
from hearthsim.game.decision_maker import PlayerDecisionMakerWithFirstSelection
from hearthsim.game.action_getter import TextActionGetter
from hearthsim.game.hearthstone_game import HearthstoneGame
from test.utils import generate_class


def _play_game(player_deck, opp_deck, player_text):
    player0_text, player1_text = split_text_by_player(player_text)
    decision_maker0 = PlayerDecisionMakerWithFirstSelection(TextActionGetter(player0_text))
    decision_maker1 = PlayerDecisionMakerWithFirstSelection(TextActionGetter(player1_text))
    game = HearthstoneGame(player_deck, opp_deck, decision_maker0, decision_maker1)
    game.setup(shuffle_decks=False)
    for player in game.players:
        player.health = 5
        player.current_mana = 100
        player.available_mana = 100
        player.maximum_mana = 100
    game.play()


def main():
    # Note: modifying __init__ of a TestCase object throws an error
    class TestBasicsOfCardIdBaseClass(unittest.TestCase):
        card_id = None
        class_type = None

        def test_card_constructor(self):
            Card.from_card_id(card_id=self.card_id)


    class TestBasicsOfMinionBaseClass(TestBasicsOfCardIdBaseClass):
        def test_card_playing(self):
            player_deck = Deck([self.card_id] * 30, cls=HSClass.PRIEST.value)
            opp_deck = Deck([self.card_id] * 30, cls=HSClass.PRIEST.value)
            player_text = '''
                0:
                    play 0 0
                    play 0 0
                    end_turn
                1:
                    play 0 0
                    play 0 0
                    concede
            '''
            _play_game(player_deck, opp_deck, player_text)

        def test_card_attacking(self):
            if self.class_type.attack == 0:
                return

            player_deck = Deck([self.card_id] * 30, cls=HSClass.PRIEST.value)
            opp_deck = Deck([self.card_id] * 30, cls=HSClass.PRIEST.value)
            player_text = '''
                0:
                    play 0 0
                    play 0 0
                    end_turn
                1:
                    play 0 0
                    play 0 0
                    end_turn
                0:
                    attack 0 0
                    play 0 0
                    play 0 0
                    end_turn
                1:
                    attack 0 0
                    play 0 0
                    play 0 0
                    concede
            '''
            _play_game(player_deck, opp_deck, player_text)


    class TestBasicsOfOriginalHeroBaseClass(TestBasicsOfCardIdBaseClass):
        def test_card_playing(self):
            player_deck = Deck(['C001'] * 30, cls=self.class_type.hs_class)  # Wisp
            opp_deck = Deck(['C001'] * 30, cls=self.class_type.hs_class)  # Wisp
            player_text = '''
                0:
                    hero_power
                    hero_power
                    end_turn
                1:
                    hero_power
                    hero_power
                0:
                    end_turn
                1:
                    concede
            '''
            _play_game(player_deck, opp_deck, player_text)


    class TestBasicsOfWeaponBaseClass(TestBasicsOfCardIdBaseClass):
        pass


    class TestBasicsOfSpellBaseClass(TestBasicsOfCardIdBaseClass):
        def test_card_playing(self):
            player_deck = Deck([self.card_id] * 30, cls=HSClass.PRIEST.value)
            opp_deck = Deck([self.card_id] * 30, cls=HSClass.PRIEST.value)
            player_text = '''
                0:
                    play 0 0
                    play 0 0
                    end_turn
                1:
                    play 0 0
                    play 0 0
                    concede
            '''
            _play_game(player_deck, opp_deck, player_text)


    for card_id, class_type in sorted(CARD_REGISTRY.items()):
        name = f'TestBasicsOf{class_type.__name__}'
        if issubclass(class_type, MinionCard):
            gen_class = generate_class(name, TestBasicsOfMinionBaseClass)
        elif issubclass(class_type, WeaponCard):
            gen_class = generate_class(name, TestBasicsOfWeaponBaseClass)
        elif issubclass(class_type, SpellCard):
            gen_class = generate_class(name, TestBasicsOfSpellBaseClass)
        elif issubclass(class_type, OriginalHeroCard):
            gen_class = generate_class(name, TestBasicsOfOriginalHeroBaseClass)
        else:
            raise NotImplementedError()
        gen_class.card_id = card_id
        gen_class.class_type = class_type
        globals()[name] = gen_class


main()
