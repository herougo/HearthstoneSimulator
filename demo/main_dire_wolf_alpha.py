from hearthsim.utils.enums import HSClass
from hearthsim.game.deck import Deck
from hearthsim.utils.decision_maker_text import split_text_by_player
from hearthsim.game.decision_maker import PlayerDecisionMaker
from hearthsim.game.action_getter import TextActionGetter
from hearthsim.game.hearthstone_game import HearthstoneGame

def main():
    my_deck = Deck(['C011'] * 30, cls=HSClass.PRIEST.value)
    opp_deck = Deck(['C011'] * 30, cls=HSClass.PRIEST.value)
    player_text = '''
    0:
        play 0 0
        play 0 0
        play 0 0
        end_turn
    1:
        play 0 0
        play 0 0
        play 0 0
        end_turn
    0:
        attack 0 1
        concede
    '''
    player0_text, player1_text = split_text_by_player(player_text)
    decision_maker0 = PlayerDecisionMaker(TextActionGetter(player0_text))
    decision_maker1 = PlayerDecisionMaker(TextActionGetter(player1_text))
    game = HearthstoneGame(my_deck, opp_deck, decision_maker0, decision_maker1)
    game.setup(shuffle_decks=False)
    for player in game.players:
        player.health = 5
        player.current_mana = 8
        player.available_mana = 8
    game.play()

if __name__ == '__main__':
    main()