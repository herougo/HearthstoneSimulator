from hearthsim.utils.enums import Events
from hearthsim.utils.utils import maybe_wrap_as_tuple
from hearthsim.game.effect_manager import EffectManagerNode
from hearthsim.game.card_slots import MinionCardSlot, SpellCardSlot
from hearthsim.effects.effects_continuous import Sleep
from hearthsim.effects.core import  OneTimeEffectSequence


class CardMover:
    # handles moving cards in a HearthstoneGame (e.g. killing minions, returning to the hand, etc)
    def __init__(self, game):
        self._game = game
        self._limbo = set()

    def play_card(self, card_in_hand_index, destination_index):
        card_slot = self._game.hands[self._game.game_metadata.turn].pop(card_in_hand_index)
        self._game.players[self._game.game_metadata.turn].current_mana -= card_slot.card.mana

        card_name = card_slot.card.name
        self._game.ui_manager.log_play_card(card_name)
        if isinstance(card_slot, MinionCardSlot):
            self._play_minion(card_slot, destination_index)
        elif isinstance(card_slot, SpellCardSlot):
            self._play_spell(card_slot)
        else:
            raise NotImplementedError()

    def _play_minion(self, card_slot, destination_index):
        self._game.battleboard.add_cards(self._game.game_metadata.turn, [card_slot],
                                   index=destination_index)

        for effect in maybe_wrap_as_tuple(card_slot.card.in_play_effects):
            em_node = EffectManagerNode(
                effect=effect, affected_slot=card_slot,
                origin_slot=card_slot, silenceable=True
            )
            self._game.effect_manager.add_effect(em_node)

        # prevent attacking on the turn it's summoned (via Sleep effect)
        em_node = EffectManagerNode(
            effect=Sleep(), affected_slot=card_slot,
            origin_slot=card_slot, silenceable=False
        )
        self._game.effect_manager.add_effect(em_node)

        # send events
        self._game.effect_manager.send_event(Events.MINION_PUT_IN_PLAY.value,
                                       event_slot=card_slot)
        self._game.effect_manager.send_event(Events.MINION_BATTLECRY.value,
                                       event_slot=card_slot)
        self._game.effect_manager.send_event(Events.MINION_SUMMONED.value,
                                       event_slot=card_slot)

    def _play_spell(self, card_slot):
        self.send_card_to_limbo(card_slot)
        effect = card_slot.card.when_played_effects
        if isinstance(effect, tuple):
            effect = OneTimeEffectSequence(effect)

        em_node = EffectManagerNode(effect=effect, affected_slot=card_slot, origin_slot=card_slot, silenceable=False)
        em_node.execute(self, self._game.effect_manager)

        self._game.effect_manager.send_event(Events.AFTER_SPELL_ACTIVATED.value, event_slot=card_slot)
        self._game.remove_card_slot(card_slot)

    def kill_minions(self, card_slots):
        for i in range(len(card_slots)):
            self._game.battleboard.pop_card_slot(card_slots[i])
            self.send_card_to_limbo(card_slots[i])

        for i in range(len(card_slots)):
            self._game.ui_manager.log_line(f'{card_slots[i]} died')
            self._game.effect_manager.send_event(Events.MINION_DIES.value, event_slot=card_slots[i])

        for i in range(len(card_slots)):
            self._game.effect_manager.pop_effects_by_slot(card_slots[i])
            self.remove_card_slot(card_slots[i])

    def draw_cards(self, player, n=1):
        n_can_draw = self._game.player_metadata[player].hand_limit - len(self._game.hands[player])
        n_burned = max(0, n - n_can_draw)
        n_drawn = n - n_burned
        cards_from_deck = list(reversed(self._game.decks[player].draw(n=n)))
        drawn_cards, burned_cards = cards_from_deck[:n_drawn], cards_from_deck[n_drawn:]
        self._game.hands[player].add_cards(drawn_cards)
        for card_slot in burned_cards:
            self.send_card_to_limbo(card_slot)
            self.remove_card_slot(card_slot)
            self._game.ui_manager.log_line(f'{player} Burned {card_slot}')

    def send_card_to_limbo(self, card_slot):
        '''
        limbo is a place in-between dying and living
        assume the card has already been removed from its appropriate place
        '''
        self._limbo.add(card_slot)

    def remove_card_slot(self, card_slot):
        self._limbo.remove(card_slot)

    def destroy_weapon(self, player):
        weapon_card_slot = self._game.weapons[player]
        self.send_card_to_limbo(weapon_card_slot)
        self._game.weapons[player] = None  # must set to None before sending the event
        self._game.effect_manager.send_event(Events.WEAPON_DESTROYED.value,
                                             event_slot=self._game.weapons[player])
        self.remove_card_slot(weapon_card_slot)

    def equip_weapon(self, player, card_slot):
        if self._game.weapons[player]:
            self.destroy_weapon(player)

        self._game.weapons[player] = card_slot  # must set before sending the event
        self._game.effect_manager.send_event(Events.WEAPON_EQUIPPED.value,
                                       event_slot=self._game.weapons[player])

    def can_summon_minion(self, player):
        return self._game.battleboard.board_len(player) < self._game.player_metadata[player].battleboard_limit

    def summon_minion(self, card_slot):
        self._game.battleboard.add_cards(card_slot.player, [card_slot], index=None)

        card_name = card_slot.card.name
        self._game.ui_manager.log_summon_minion(card_slot.player, card_name)

        for effect in maybe_wrap_as_tuple(card_slot.card.in_play_effects):
            em_node = EffectManagerNode(
                effect=effect, affected_slot=card_slot,
                origin_slot=card_slot, silenceable=True
            )
            self._game.effect_manager.add_effect(em_node)

        # prevent attacking on the turn it's summoned (via Sleep effect)
        em_node = EffectManagerNode(
            effect=Sleep(), affected_slot=card_slot,
            origin_slot=card_slot, silenceable=False
        )
        self._game.effect_manager.add_effect(em_node)

        # send events
        self._game.effect_manager.send_event(Events.MINION_PUT_IN_PLAY.value,
                                             event_slot=card_slot)
        # (no battlecry event)
        self._game.effect_manager.send_event(Events.MINION_SUMMONED.value,
                                             event_slot=card_slot)


    def return_minions_to_hand(self, player, card_slots):
        # returns from battleboard to hand
        available_hand_space = self._game.player_metadata[player].hand_limit - len(self._game.hands[player])
        n_to_die = max(0, len(card_slots) - available_hand_space)
        n_to_return = len(card_slots) - n_to_die
        to_return, to_die = card_slots[:n_to_return], card_slots[n_to_return:]

        for card_slot in to_return:
            self._game.battleboard.pop_card_slot(card_slot)
            if player != card_slot.player:
                card_slot.switch_players()

        self._game.hands[player].add_cards(to_return)

        for card_slot in to_return:
            self._game.ui_manager.log_line(f'{card_slot} returned to {player} hand')
            self._game.effect_manager.send_event(Events.MINION_RETURNED_TO_HAND.value,
                                           event_slot=card_slot)
            self._game.effect_manager.pop_effects_by_slot(card_slot)

        self.kill_minions(to_die)
        self._game.ui_manager.log_game_state()