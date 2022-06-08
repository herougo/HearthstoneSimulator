from hearthsim.utils.enums import (Events, PlayerChoice,  Actions)
from hearthsim.utils.logger import LOGGER
from hearthsim.utils.pile import Pile
from hearthsim.utils.utils import maybe_wrap_as_tuple
from hearthsim.utils.constants import HERO_INDEX
from hearthsim.utils.exceptions import GameOverException
from hearthsim.game.effect_manager import (EffectManager, EffectManagerNode)
from hearthsim.game.card_slots import (MinionCardSlot, HeroCardSlot, WeaponCardSlot)
from hearthsim.game.metadata import (GameMetadata, PlayerMetadata)
from hearthsim.game.ui_manager import UIManager
from hearthsim.game.battleboard import Battleboard
from hearthsim.game.utils import targetable_with_hero_power
from hearthsim.cards.types_of_cards import (MinionCard, WeaponCard)
from hearthsim.effects.effects_continuous import Sleep


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
        self._limbo = {}  # hash to CardSlot

        self.effect_manager = None
        self.game_metadata = None
        self.player_metadata = None
        self.ui_manager = None

        self.hash_to_slot_dict = {}

    def register_card_slot(self, card_slot):
        self.hash_to_slot_dict[card_slot.hash] = card_slot

    def setup(self):
        self.effect_manager = EffectManager(self)
        self.decks = tuple([Pile([MinionCardSlot(card_id, player, self)
                                  for card_id in deck.card_id_list])
                            for player, deck in enumerate(self.deck_lists)])
        # for i in range(2):
        #     self.decks[i].shuffle()
        self.game_metadata = GameMetadata()
        self.player_metadata = (PlayerMetadata(), PlayerMetadata())
        # self.game_metadata.who_goes_first = random.randint(0, 1)
        self.game_metadata.who_goes_first = 0
        who_goes_second = 1 - self.game_metadata.who_goes_first
        self.hands = (Pile(), Pile())
        self.ui_manager = UIManager(self, LOGGER)
        self.ui_manager.log_player_going_first()

        # draw hands
        self.draw_cards(self.game_metadata.who_goes_first, 3)
        self.draw_cards(who_goes_second, 4)

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
                    self.play_card(card_in_hand_index, destination_index)
                elif action_type == Actions.HERO_POWER.value:
                    self.effect_manager.send_event(Events.ACTIVATE_HERO_POWER.value,
                                                   event_slot=self.players[turn])
                    self.effect_manager.send_event(Events.HERO_POWER_END.value,
                                                   event_slot=self.players[turn])
                    self.ui_manager.log_game_state()
            else:
                continue

            self.ui_manager.log_game_state()

    def play_card(self, card_in_hand_index, destination_index):
        card_slot = self.hands[self.game_metadata.turn].pop(card_in_hand_index)
        self.players[self.game_metadata.turn].current_mana -= card_slot.card.mana
        self.battleboard.add_cards(self.game_metadata.turn, [card_slot],
                                   index=destination_index)

        card_name = self.hands[self.game_metadata.turn][card_in_hand_index].card.name
        self.ui_manager.log_play_card(card_name)

        for effect in maybe_wrap_as_tuple(card_slot.card.in_play_effects):
            em_node = EffectManagerNode(
                effect=effect, affected_slot=card_slot,
                origin_slot=card_slot, silenceable=True
            )
            self.effect_manager.add_effect(em_node)

        # prevent attacking on the turn it's summoned (via Sleep effect)
        em_node = EffectManagerNode(
            effect=Sleep(), affected_slot=card_slot,
            origin_slot=card_slot, silenceable=False
        )
        self.effect_manager.add_effect(em_node)

        # send events
        self.effect_manager.send_event(Events.MINION_PUT_IN_PLAY.value,
                                       event_slot=card_slot)
        self.effect_manager.send_event(Events.MINION_BATTLECRY.value,
                                       event_slot=card_slot)
        self.effect_manager.send_event(Events.MINION_SUMMONED.value,
                                       event_slot=card_slot)

    def check_game_over(self):
        player0_dead = self.players[0].health <= 0
        player1_dead = self.players[1].health <= 0
        if not player0_dead and not player1_dead:
            return

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
                self.destroy_weapon(attacker_card_slot.player)

        self.check_game_over()
        death = [False, False]
        card_slots = [attacker_card_slot, defender_card_slot]
        for i in range(2):
            death[i] = (isinstance(card_slots[i], MinionCardSlot) and
                        card_slots[i].health <= 0)
            if death[i]:
                self.battleboard.pop_card_slot(card_slots[i])
                self.send_card_to_limbo(card_slots[i])

        for i in range(2):
            if death[i]:
                self.ui_manager.log_line(f'{card_slots[i]} died')
                self.effect_manager.send_event(Events.MINION_DIES.value,
                                               event_slot=card_slots[i])
                self.effect_manager.pop_effects_by_slot(card_slots[i])
                self.remove_card_slot(card_slots[i])

    def draw_cards(self, player, n=1):
        self.hands[player].add_cards(self.decks[player].draw(n=n))

    def hash_to_slot(self, hash):
        return self.hash_to_slot_dict[hash]

    def index_to_slot(self, player, board_index):
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
        else:
            raise NotImplementedError(f'{type(card)}')

        return card_slot

    def send_card_to_limbo(self, card_slot):
        '''
        limbo is a place in-between dying and living
        assume the card has already been removed from its appropriate place
        '''
        self._limbo[card_slot.hash] = card_slot

    def remove_card_slot(self, card_slot):
        del self._limbo[card_slot.hash]

    def destroy_weapon(self, player):
        weapon_card_slot = self.weapons[player]
        self.send_card_to_limbo(weapon_card_slot)
        self.weapons[player] = None  # must set to None before sending the event
        self.effect_manager.send_event(Events.WEAPON_DESTROYED.value,
                                       event_slot=self.weapons[player])
        self.remove_card_slot(weapon_card_slot)

    def equip_weapon(self, player, card_slot):
        if self.weapons[player]:
            self.destroy_weapon(player)

        self.weapons[player] = card_slot  # must set before sending the event
        self.effect_manager.send_event(Events.WEAPON_EQUIPPED.value,
                                       event_slot=self.weapons[player])

    def get_card_slots_targetable_by_hp(self, targeting_player, target_player_choice):
        opp = 1 - targeting_player
        if target_player_choice == PlayerChoice.BOTH.value:
            available_players_for_target = [targeting_player, opp]
        elif target_player_choice == PlayerChoice.OPPONENT.value:
            available_players_for_target = [opp]
        elif target_player_choice == PlayerChoice.PLAYER.value:
            available_players_for_target = [targeting_player]
        else:
            raise ValueError()
        result = []
        for player in available_players_for_target:
            if targetable_with_hero_power(targeting_player, self.players[player]):
                result.append(self.players[player])
            for card_slot in self.battleboard.iter_board(opp):
                if targetable_with_hero_power(targeting_player, card_slot):
                    result.append(card_slot)

        return result

    def can_summon_minion(self, player):
        return self.battleboard.board_len(player) < self.game_metadata.battleboard_limit

    def summon_minion(self, card_slot):
        self.battleboard.add_cards(card_slot.player, [card_slot], index=None)

        card_name = card_slot.card.name
        self.ui_manager.log_summon_minion(card_slot.player, card_name)

        for effect in maybe_wrap_as_tuple(card_slot.card.in_play_effects):
            em_node = EffectManagerNode(
                effect=effect, affected_slot=card_slot,
                origin_slot=card_slot, silenceable=True
            )
            self.effect_manager.add_effect(em_node)

        # prevent attacking on the turn it's summoned (via Sleep effect)
        em_node = EffectManagerNode(
            effect=Sleep(), affected_slot=card_slot,
            origin_slot=card_slot, silenceable=False
        )
        self.effect_manager.add_effect(em_node)

        # send events
        self.effect_manager.send_event(Events.MINION_PUT_IN_PLAY.value,
                                       event_slot=card_slot)
        # (no battlecry event)
        self.effect_manager.send_event(Events.MINION_SUMMONED.value,
                                       event_slot=card_slot)