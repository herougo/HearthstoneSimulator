import hearthsim
from hearthsim.utils.enums import Events, Actions
from hearthsim.utils.pile import Pile
from hearthsim.utils.utils import maybe_wrap_as_tuple
from hearthsim.utils.constants import HERO_INDEX
from hearthsim.utils.exceptions import GameOverException
from hearthsim.game.effect_manager import EffectManager, EffectManagerNode
from hearthsim.game.card_slots import CardSlot, MinionCardSlot, HeroCardSlot, WeaponCardSlot, SpellCardSlot
from hearthsim.game.metadata import GameMetadata, PlayerMetadata
from hearthsim.game.ui_manager import UIManager
from hearthsim.game.battleboard import Battleboard
from hearthsim.cards.types_of_cards import MinionCard, WeaponCard, SpellCard
from hearthsim.cards.implementations.fundamental import Coin
from hearthsim.game.card_mover import CardMover


class HearthstoneGame:
    def __init__(self, deck0, deck1, decision_maker0, decision_maker1):
        self.deck_lists = (deck0, deck1)
        self.decision_makers = (decision_maker0, decision_maker1)
        decision_maker0.set_game(self)
        decision_maker1.set_game(self)

        self.decks = None
        self.hands = None
        self.players = None
        self.weapons = None
        self.battleboard = None

        self.effect_manager = None
        self.game_metadata = None
        self.player_metadata = None
        self.ui_manager = None
        self.card_mover = CardMover(self)

    def setup(self, shuffle_decks=True):
        self.effect_manager = EffectManager(self)
        self.decks = tuple([Pile([CardSlot.create_card(card_id, player, self)
                                  for card_id in deck.card_id_list])
                            for player, deck in enumerate(self.deck_lists)])
        if shuffle_decks:
            for i in range(2):
                self.decks[i].shuffle()
        self.game_metadata = GameMetadata()
        self.player_metadata = (PlayerMetadata(), PlayerMetadata())
        # self.game_metadata.who_goes_first = random.randint(0, 1)
        self.game_metadata.who_goes_first = 0
        who_goes_second = 1 - self.game_metadata.who_goes_first
        self.hands = (Pile(), Pile())
        self.ui_manager = UIManager(self, hearthsim.utils.logger.LOGGER)
        self.ui_manager.log_player_going_first()

        # draw hands
        self.card_mover.draw_cards(self.game_metadata.who_goes_first, 3)
        self.card_mover.draw_cards(who_goes_second, 4)
        self.create_card_and_add_to_hand(who_goes_second, Coin())

        # (mulligan skipped)

        # players
        self.players = (
            HeroCardSlot(self.deck_lists[0].cls, 0, self),
            HeroCardSlot(self.deck_lists[1].cls, 1, self)
        )
        for player in self.players:
            player.setup_hero_power()

        # weapons
        self.weapons = [None, None]

        # board
        self.battleboard = Battleboard(self)

        # setup in-game effects
        self.game_metadata.turn = self.game_metadata.who_goes_first
        for i in range(2):
            effects = maybe_wrap_as_tuple(self.players[i].card.effects)
            for effect in effects:
                em_node = EffectManagerNode(
                    effect=effect, affected_slot=self.players[i],
                    origin_slot=self.players[i], silenceable=False
                )
                self.effect_manager.add_effect(em_node)

    def play(self):
        try:
            # turns
            for i in range(1000):
                self.effect_manager.send_event(Events.START_TURN.value)
                self.ui_manager.log_turn()
                self.ui_manager.log_game_state()

                self.loop_actions_until_end_turn()
                self.effect_manager.send_event(Events.PRE_END_TURN_FROZEN.value)
                self.effect_manager.send_event(Events.END_TURN.value)

                self.game_metadata.turn = 1 - self.game_metadata.turn
        except GameOverException as ex:
            pass

    def loop_actions_until_end_turn(self):
        end_turn = False
        while not end_turn:
            turn = self.game_metadata.turn

            action = self.decision_makers[turn].get_action()
            if action:
                action_type, args = action
                if action_type == Actions.END_TURN.value:
                    end_turn = True
                    continue
                elif action_type == Actions.ATTACK.value:
                    attacker_card_slot, defender_card_slot = args
                    self.attack(attacker_card_slot, defender_card_slot)
                elif action_type == Actions.PLAY.value:
                    card_in_hand_index, destination_index = args
                    self.card_mover.play_card(card_in_hand_index, destination_index)
                elif action_type == Actions.HERO_POWER.value:
                    self.players[turn].current_mana -= self.players[turn].hero_power_cost
                    self.effect_manager.send_event(Events.ACTIVATE_HERO_POWER.value,
                                                   event_slot=self.players[turn])
                    self.effect_manager.send_event(Events.HERO_POWER_END.value,
                                                   event_slot=self.players[turn])
                    self.ui_manager.log_game_state()
                elif action_type == Actions.CONCEDE.value:
                    self.end_game(turn == 0, turn == 1)
            else:
                continue

            self.ui_manager.log_game_state()

    def create_card_and_add_to_hand(self, player, card):
        n_can_draw = self.player_metadata[player].hand_limit - len(self.hands[player])
        if n_can_draw > 0:
            card_slot = self.create_card_slot(player, card)
            self.hands[player].add_cards([card_slot])

    def check_game_over(self):
        player0_dead = self.players[0].health <= 0
        player1_dead = self.players[1].health <= 0
        if not player0_dead and not player1_dead:
            return
        self.end_game(player0_dead, player1_dead)

    def end_game(self, player0_dead, player1_dead):
        self.ui_manager.log_game_state()

        self.ui_manager.log_game_over_result(player0_dead, player1_dead)

        raise GameOverException()

    def attack(self, attacker_card_slot, defender_card_slot):
        self.ui_manager.log_attack(attacker_card_slot, defender_card_slot)
        attacker_card_slot.attacks_this_turn += 1
        self.game_metadata.attacker_damage_taken = defender_card_slot.attack
        self.game_metadata.defender_damage_taken = attacker_card_slot.attack
        self.effect_manager.send_event(Events.AFTER_ATTACKER_INITIAL_COMBAT_DAMAGE.value)
        self.effect_manager.send_event(Events.AFTER_DEFENDER_INITIAL_COMBAT_DAMAGE.value)
        attacker_card_slot.take_damage(self.game_metadata.attacker_damage_taken)
        defender_card_slot.take_damage(self.game_metadata.defender_damage_taken)
        self.effect_manager.send_event(Events.AFTER_ATTACKER_ATTACKED.value,
                                       event_slot=attacker_card_slot)
        self.effect_manager.send_event(Events.AFTER_COMBAT_DAMAGE.value)
        if (isinstance(attacker_card_slot, HeroCardSlot) and
                self.weapons[attacker_card_slot.player]):
            self.weapons[attacker_card_slot.player].durability -= 1
            if self.weapons[attacker_card_slot.player].durability == 0:
                self.card_mover.destroy_weapon(attacker_card_slot.player)

        self.check_game_over()
        card_slots = [attacker_card_slot, defender_card_slot]
        minions_to_kill = [card_slot for card_slot in card_slots
                           if isinstance(card_slot, MinionCardSlot) and (card_slot.health <= 0)]
        self.card_mover.kill_minions(minions_to_kill)

    def index_to_slot(self, board_index):
        player, board_index = board_index
        if board_index == HERO_INDEX:
            card_slot = self.players[player]
        else:
            card_slot = self.battleboard.get_slot(player, board_index)
        return card_slot

    def create_card_slot(self, player, card):
        if isinstance(card, MinionCard):
            card_slot = MinionCardSlot(card.card_id, player, self)
        elif isinstance(card, WeaponCard):
            card_slot = WeaponCardSlot(card.card_id, player, self)
        elif isinstance(card, SpellCard):
            card_slot = SpellCardSlot(card.card_id, player, self)
        else:
            raise NotImplementedError(f'{type(card)}')

        return card_slot
