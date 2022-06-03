class ChangeAttack(OneTimeEffect):
    def __init__(self, selection, amount):
        self.selection = selection
        self.amount = amount
        if not callable(amount) and amount <= 0:
            raise ValueError('ChangeAttack must have a positive amount argument')

    def _compute_amount(self, game, em_node):
        if callable(self.amount):
            return self.amount(game, em_node.affected_slot)
        else:
            return self.amount

    def execute(self, game, em_node):
        selected_card_slots = self.selection.get_selected_card_slots(game, em_node)
        em_nodes_to_add = []
        for selected_card_slot in selected_card_slots:
            em_node = EffectManagerNode(
                effect=AttackBuff(amount=self._compute_amount(game, em_node)),
                affected_slot=selected_card_slot,
                origin_slot=em_node.origin_slot,
                silenceable=True
            )
            em_nodes_to_add.append(em_node)

        return EffectManagerNodePlan(to_add=em_nodes_to_add)

class ChangeHealth(OneTimeEffect):
    def __init__(self, selection, amount):
        self.selection = selection
        self.amount = amount
        if not callable(amount) and amount <= 0:
            raise ValueError('ChangeHealth must have a positive amount argument')

    def _compute_amount(self, game, em_node):
        if callable(self.amount):
            return self.amount(game, em_node.affected_slot)
        else:
            return self.amount

    def execute(self, game, em_node):
        em_nodes_to_add = []
        for selected_card_slot in self.selection.get_selected_card_slots(game, em_node):
            em_node = EffectManagerNode(
                effect=HealthBuff(amount=self.compute_amount(game, em_node)),
                affected_slot=selected_card_slot,
                origin_slot=em_node.origin_slot,
                silenceable=True
            )
            em_nodes_to_add.append(em_node)

        return EffectManagerNodePlan(to_add=em_nodes_to_add)

class Heal(OneTimeEffect):
    def __init__(self, selection, amount):
        self.selection = selection
        self.amount = amount

    def execute(self, game, em_node):
        selected_card_slots = self.selection.get_selected_card_slots(game, em_node)
        for card_slot in selected_card_slots:
            card_slot.health = min(card_slot.health + self.amount,
                                   card_slot.max_health)

class DealDamage(OneTimeEffect):
    def __init__(self, selection, amount):
        self.selection = selection
        self.amount = amount

    def execute(self, game, em_node):
        selected_card_slots = self.selection.get_selected_card_slots(game, em_node)
        for card_slot in selected_card_slots:
            card_slot.health = card_slot.health - self.amount

class ReturnMinionToHand(OneTimeEffect):
    def __init__(self, selection):
        self.selection = selection

    def execute(self, game, em_node):
        pass

class Silence(OneTimeEffect):
    def __init__(self, selection):
        self.selection = selection

    def execute(self, game, em_node):
        pass

class DrawCard(OneTimeEffect):
    def __init__(self, selection):
        self.selection = selection

    def execute(self, game, em_node):
        game.draw_cards(em_node.affected_slot.player, n=1)

class GainManaCrystals(OneTimeEffect):
    def __init__(self, selection, amount):
        self.selection = selection
        self.amount = amount

    def execute(self, game, em_node):
        player_slot = game.players[em_node.affected_slot.player]
        player_slot.available_mana += min(
            player_slot.maximum_mana - player_slot.available_mana,
            self.amount)
        player_slot.current_mana += min(
            player_slot.maximum_mana - player_slot.current_mana,
            self.amount)

class RefreshAllManaCrystals(OneTimeEffect):
    def __init__(self, selection):
        self.selection = selection

    def execute(self, game, em_node):
        player_slot = game.players[em_node.affected_slot.player]
        player_slot.current_mana = player_slot.available_mana

class RefreshMinionAttacks(OneTimeEffect):
    def __init__(self, selection):
        self.selection = selection

    def execute(self, game, em_node):
        selected_card_slots = self.selection.get_selected_card_slots(game, em_node)
        for card_slot in selected_card_slots:
            card_slot.attacks_this_turn = 0

class RefreshHeroPower(OneTimeEffect):
    def __init__(self, selection):
        self.selection = selection

    def execute(self, game, em_node):
        selected_card_slots = self.selection.get_selected_card_slots(game, em_node)
        for card_slot in selected_card_slots:
            card_slot.hero_power_used_this_turn = False

class EquipWeapon(OneTimeEffect):
    def __init__(self, selection, weapon):
        super(EquipWeapon, self).__init__()
        self.selection = selection
        self.weapon = weapon

    def execute(self, game, em_node):
        selected_card_slots = self.selection.get_selected_card_slots(game, em_node)
        for card_slot in selected_card_slots:
            assert isinstance(card_slot, HeroCardSlot)
            weapon_card_slot = game.create_card_slot(card_slot.player, self.weapon)
            game.equip_weapon(card_slot.player, weapon_card_slot)