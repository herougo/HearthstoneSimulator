class UIManager:
    def __init__(self, game, logger):
        self.game = game
        self.logger = logger

    def log_turn(self):
        self.logger.info(f'Turn: {self.game.game_metadata.turn}')

    def _log_hand(self, player):
        for i, card_slot in enumerate(self.game.hands[player]):
            mana, attack, health = card_slot.compute_stats()
            to_print = (f'{i}: {card_slot.card.name} - {mana} '
                        f'mana, ({attack}, {health}) stats')
            self.logger.info(to_print)

    def _log_board(self, player):
        for i, card_slot in enumerate(self.game.battleboard.iter_board(player)):
            mana, attack, health = card_slot.compute_stats()
            to_print = (f'\t{i}: {card_slot.card.name} - {mana} '
                        f'mana, ({attack}, {health}) stats')
            self.logger.info(to_print)

    def log_game_state(self):
        player = 0
        opp = 1 - player
        opp_slot = self.game.players[opp]
        opp_current_mana = opp_slot.current_mana
        opp_available_mana = opp_slot.available_mana
        self.logger.info(f'Opponent ({opp}) - health: {opp_slot.health}, armour: {opp_slot.armour}, '
                         f'mana: {opp_current_mana} / {opp_available_mana}')
        weapon = self.game.weapons[opp]
        if weapon:
            self.logger.info(f'Weapon: {weapon.card.name}, {weapon.attack} attack, {weapon.durability} durability')
        else:
            self.logger.info('Weapon: None')
        self._log_hand(opp)

        self.logger.info('')
        self._log_board(opp)
        self._log_board(player)
        self.logger.info('')

        player_slot = self.game.players[player]
        player_current_mana = player_slot.current_mana
        player_available_mana = player_slot.available_mana
        self.logger.info(f'Player ({player}) - health: {player_slot.health}, armour: {player_slot.armour}, '
                         f'mana: {player_current_mana} / {player_available_mana}')
        self._log_hand(player)
        self.logger.info('')

    def log_player_going_first(self):
        self.logger.info(f'{self.game.game_metadata.who_goes_first} goes first')

    def log_turn(self):
        self.logger.info('-' * 30)
        self.logger.info(f'{self.game.game_metadata.turn} turn')
        self.logger.info('-' * 30)

    def log_line(self, line):
        self.logger.info(line)

    def log_text(self, text):
        self.logger.info(text)

    def log_play_card(self, card_name):
        self.logger.info(f'{self.game.game_metadata.turn} plays {card_name}')

    def log_attack(self, attacker_slot, defender_slot):
        self.logger.info(f'{attacker_slot} attacks {defender_slot}')

    def log_game_over_result(self, player0_dead, player1_dead):
        # at least one of them is true
        if player0_dead and player1_dead:
            self.logger.info('Game Over: TIE')
        elif player0_dead:
            self.logger.info('Game Over: Player 1 wins')
        elif player1_dead:
            self.logger.info('Game Over: Player 0 wins')
        else:
            raise ValueError('Neither player is dead in log_game_over_result')
