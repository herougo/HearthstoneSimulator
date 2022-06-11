from hearthsim.utils.enums import Actions, CanAttackResponse
from hearthsim.game.card_slots import MinionCardSlot, SpellCardSlot


class DecisionMaker:
    def __init__(self, action_getter):
        self._action_getter = action_getter
        self.game = None

    def set_game(self, game):
        self.game = game

    def get_action(self):
        assert self.game
        action = self._action_getter.get_action()
        split = action.split(' ')
        action_type, args = split[0], split[1:]
        if action_type == '':
            return
        elif action_type == Actions.END_TURN.value:
            return (action_type, None)
        elif action_type == Actions.ATTACK.value:
            return self._get_attack_action(args)
        elif action_type == Actions.PLAY.value:
            return self._get_play_card_action(args)
        elif action_type == Actions.SELECT.value:
            return self._get_selection_action(args)
        elif action_type == Actions.HERO_POWER.value:
            return self._get_hero_power_action()
        elif action_type == Actions.CONCEDE.value:
            return (action_type, None)
        else:
            raise ValueError(f'Unhandled command: {action}')

    def _get_attack_action(self, args):
        if len(args) != 2:
            self.game.ui_manager.log_line('ERROR: Invalid action argument number')
            return

        attacker = args[0]
        defender = args[1]
        try:
            attacker = int(attacker)
            defender = int(defender)
        except Exception as ex:
            self.game.ui_manager.log_line('ERROR: Invalid action argument type')
            return

        # -1 means the hero

        player_board_size = self.game.battleboard.board_len(self.game.game_metadata.turn)
        if attacker < -1 or player_board_size <= attacker:
            self.game.ui_manager.log_line('ERROR: attacker outside range')
            return

        opp_board_size = self.game.battleboard.board_len(1 - self.game.game_metadata.turn)
        if defender < -1 or opp_board_size <= defender:
            self.game.ui_manager.log_line('ERROR: defender outside range')
            return

        attacking_player = self.game.game_metadata.turn
        attacker_card_slot = self.game.index_to_slot((attacking_player, attacker))
        defender_card_slot = self.game.index_to_slot((1 - attacking_player, defender))

        can_attack_response = self.can_voluntarily_attack(attacker_card_slot, defender_card_slot)
        if can_attack_response != CanAttackResponse.YES.value:
            if can_attack_response == CanAttackResponse.ATTACKED_ENOUGH.value:
                self.game.ui_manager.log_line('ERROR: attacker cannot attack (already attacked enough)')
            elif can_attack_response == CanAttackResponse.ASLEEP.value:
                self.game.ui_manager.log_line('ERROR: attacker cannot attack (asleep)')
            elif can_attack_response == CanAttackResponse.DEFENDER_HAS_STEALTH.value:
                self.game.ui_manager.log_line('ERROR: defender cannot be attacked (stealth)')
            elif can_attack_response == CanAttackResponse.ZERO_ATTACK.value:
                self.game.ui_manager.log_line('ERROR: attacker has 0 attack')
            elif can_attack_response == CanAttackResponse.DISOBEYS_TAUNT.value:
                self.game.ui_manager.log_line('ERROR: attack disobey taunt')
            else:
                raise ValueError('Unknown can_voluntarily_attack response')
            return

        return (Actions.ATTACK.value, (attacker_card_slot, defender_card_slot))

    def _get_play_card_action(self, args):
        if len(args) == 0:
            self.game.ui_manager.log_line('ERROR: Invalid action argument number (should be >= 1)')
            return

        card_in_hand_index = args[0]
        try:
            card_in_hand_index = int(card_in_hand_index)
        except Exception as ex:
            self.game.ui_manager.log_line('ERROR: Invalid action argument type')
            return

        hand_size = len(self.game.hands[self.game.game_metadata.turn])
        if card_in_hand_index < 0 or hand_size <= card_in_hand_index:
            self.game.ui_manager.log_line('ERROR: card_in_hand outside range')
            return

        card_slot = self.game.hands[self.game.game_metadata.turn][card_in_hand_index]
        if card_slot.mana > self.game.players[self.game.game_metadata.turn].current_mana:
            self.game.ui_manager.log_line('ERROR: not enough mana to play the card')
            return

        if isinstance(card_slot, MinionCardSlot):
            if len(args) != 2:
                self.game.ui_manager.log_line('ERROR: Invalid action argument number (should be 2)')
                return

            destination_index = args[1]
            try:
                destination_index = int(destination_index)
            except Exception as ex:
                self.game.ui_manager.log_line('ERROR: Invalid action argument type')
                return

            player_board_size = self.game.battleboard.board_len(self.game.game_metadata.turn)
            if destination_index < 0 or player_board_size < destination_index:
                self.game.ui_manager.log_line('ERROR: destination outside range')
                return

            if not self.game.card_mover.can_summon_minion(self.game.game_metadata.turn):
                self.game.ui_manager.log_line('ERROR: not enough space on the battleboard')
                return
        elif isinstance(card_slot, SpellCardSlot):
            if len(args) != 1:
                self.game.ui_manager.log_line('ERROR: Invalid action argument number (should be 1)')
                return
            destination_index = None
        else:
            raise NotImplementedError()

        return (Actions.PLAY.value, (card_in_hand_index, destination_index))

    def _get_selection_action(self, args):
        try:
            args = [int(index) for index in args]
            if len(args) == 1:
                # expect HERO_INDEX or battleboard
                return (Actions.SELECT.value, (None, args[0]))
            elif len(args) == 2:
                # expect player followed by HERO_INDEX or battleboard
                return (Actions.SELECT.value, tuple(args))
            else:
                message = 'ERROR: Invalid number of selection arguments'
                self.game.ui_manager.log_line(message)
        except Exception as ex:
            self.game.ui_manager.log_line(f'ERROR: Invalid selection - {ex}')

        return None

    def _get_hero_power_action(self):
        player_slot = self.game.players[self.game.game_metadata.turn]
        mana_cost = player_slot.hero_power_cost
        if mana_cost > self.game.players[self.game.game_metadata.turn].current_mana:
            self.game.ui_manager.log_line('ERROR: not enough mana to use the hero power')
            return

        if player_slot.hero_power_used_this_turn:
            self.game.ui_manager.log_line('ERROR: already used the hero power')
            return

        return (Actions.HERO_POWER.value, None)

    def get_verified_selection(self, options):
        while True:
            action = self.get_action()
            if action and action[0] == Actions.SELECT.value:
                _, selection = action
                selection_player, selection_board_index = selection
                targeted_slot = self.game.index_to_slot((selection_player, selection_board_index))
                if targeted_slot is None:
                    self.game.ui_manager.log_line('ERROR: selection does not exist')
                    continue
                if targeted_slot not in options:
                    self.game.ui_manager.log_line('ERROR: Invalid selection')
                    continue

                return targeted_slot

    def can_voluntarily_attack(self, attacker, defender):
        if attacker.attack == 0:
            return CanAttackResponse.ZERO_ATTACK.value
        elif attacker.is_frozen:
            return CanAttackResponse.FROZEN.value
        elif attacker.has_sleep:
            return CanAttackResponse.ASLEEP.value
        elif attacker.attacks_this_turn >= attacker.n_possible_attacks_ignoring_frozen:
            return CanAttackResponse.ATTACKED_ENOUGH.value
        elif attacker.has_charge:
            pass

        if not self.game.battleboard.defender_obeys_taunt(defender):
            return CanAttackResponse.DISOBEYS_TAUNT.value
        elif defender.has_stealth:
            return CanAttackResponse.DEFENDER_HAS_STEALTH.value

        return CanAttackResponse.YES.value


class PlayerDecisionMaker(DecisionMaker):
    pass


class PlayerDecisionMakerWithFirstSelection(DecisionMaker):
    def get_verified_selection(self, options):
        assert options, options
        return next(iter(options))


class RandomAIDecisionMaker(DecisionMaker):
    pass