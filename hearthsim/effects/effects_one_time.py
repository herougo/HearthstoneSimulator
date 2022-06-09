import random
from hearthsim.effects.core import OneTimeEffect
from hearthsim.effects.effects_continuous import AttackBuff, HealthBuff, Frozen
from hearthsim.game.effect_manager import (EffectManagerNodePlan, EffectManagerNode)
from hearthsim.game.card_slots import HeroCardSlot


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
        amount = self._compute_amount(game, em_node)
        if amount > 0:
            for selected_card_slot in selected_card_slots:
                em_node = EffectManagerNode(
                    effect=AttackBuff(amount=amount),
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
        amount = self.selection.get_selected_card_slots(game, em_node)
        if amount > 0:
            for selected_card_slot in self.selection.get_selected_card_slots(game, em_node):
                em_node = EffectManagerNode(
                    effect=HealthBuff(amount=amount),
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
        if not callable(amount) and amount <= 0:
            raise ValueError('Heal must have a positive amount argument')

    def execute(self, game, em_node):
        selected_card_slots = self.selection.get_selected_card_slots(game, em_node)
        for card_slot in selected_card_slots:
            card_slot.health = min(card_slot.health + self.amount,
                                   card_slot.max_health)


class DealDamage(OneTimeEffect):
    def __init__(self, selection, amount):
        self.selection = selection
        self.amount = amount
        if not callable(amount) and amount <= 0:
            raise ValueError('DealDamage must have a positive amount argument')

    def execute(self, game, em_node):
        selected_card_slots = self.selection.get_selected_card_slots(game, em_node)
        for card_slot in selected_card_slots:
            card_slot.health = card_slot.health - self.amount


class ReturnMinionToHand(OneTimeEffect):
    def __init__(self, selection):
        self.selection = selection

    def execute(self, game, em_node):
        selected_card_slots = self.selection.get_selected_card_slots(game, em_node)
        game.return_minions_to_hand(em_node.affected_slot.player, selected_card_slots)


class Silence(OneTimeEffect):
    def __init__(self, selection):
        self.selection = selection

    def execute(self, game, em_node):
        plan = EffectManagerNodePlan()
        selected_card_slots = self.selection.get_selected_card_slots(game, em_node)
        for card_slot in selected_card_slots:
            card_slot.silenced = True
            for card_slot_em_node in card_slot.iter_em_nodes():
                if card_slot_em_node.silenceable:
                    plan.to_remove.append(card_slot_em_node)
        return plan


class DrawCard(OneTimeEffect):
    def __init__(self, selection):
        self.selection = selection

    def execute(self, game, em_node):
        selected_card_slots = self.selection.get_selected_card_slots(game, em_node)
        for card_slot in selected_card_slots:
            game.draw_cards(card_slot.player, n=1)


class GainManaCrystals(OneTimeEffect):
    def __init__(self, selection, amount):
        self.selection = selection
        self.amount = amount
        if not callable(amount) and amount <= 0:
            raise ValueError('GainManaCrystals must have a positive amount argument')

    def execute(self, game, em_node):
        selected_card_slots = self.selection.get_selected_card_slots(game, em_node)
        for card_slot in selected_card_slots:
            card_slot.available_mana += min(
                card_slot.maximum_mana - card_slot.available_mana,
                self.amount)
            card_slot.current_mana += min(
                card_slot.maximum_mana - card_slot.current_mana,
                self.amount)


class GainCurrentManaCrystals(OneTimeEffect):
    def __init__(self, selection, amount):
        self.selection = selection
        self.amount = amount
        if not callable(amount) and amount <= 0:
            raise ValueError('GainManaCrystals must have a positive amount argument')

    def execute(self, game, em_node):
        selected_card_slots = self.selection.get_selected_card_slots(game, em_node)
        for card_slot in selected_card_slots:
            card_slot.current_mana += min(
                card_slot.maximum_mana - card_slot.current_mana,
                self.amount)


class RefreshAllManaCrystals(OneTimeEffect):
    def __init__(self, selection):
        self.selection = selection

    def execute(self, game, em_node):
        selected_card_slots = self.selection.get_selected_card_slots(game, em_node)
        for card_slot in selected_card_slots:
            card_slot.current_mana = card_slot.available_mana


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


class GainArmour(OneTimeEffect):
    def __init__(self, selection, amount):
        self.selection = selection
        self.amount = amount
        if not callable(amount) and amount <= 0:
            raise ValueError('GainArmour must have a positive amount argument')

    def execute(self, game, em_node):
        selected_card_slots = self.selection.get_selected_card_slots(game, em_node)
        for card_slot in selected_card_slots:
            card_slot.armour += self.amount


class SummonMinion(OneTimeEffect):
    def __init__(self, minion):
        self.minion = minion

    def execute(self, game, em_node):
        player = em_node.affected_slot.player
        if game.can_summon_minion(player):
            card_slot = game.create_card_slot(player, self.minion)
            game.summon_minion(card_slot)


class SummonMinionLikeShamanHP(OneTimeEffect):
    def __init__(self, possible_minions):
        self.possible_minions = possible_minions
        self._card_id_to_minion = {
            card.card_id: card for card in possible_minions
        }
        self._card_id_set = set(self._card_id_to_minion.keys())

    def execute(self, game, em_node):
        player = em_node.affected_slot.player
        if game.can_summon_minion(player):
            unavailable_card_ids = {slot.card.card_id for slot in game.battleboard.iter_board(player)}
            diff = self._card_id_set - unavailable_card_ids
            if not diff:
                available_card_ids = self._card_id_set
            else:
                available_card_ids = diff
            available_card_ids = list(sorted(list(available_card_ids)))  # needed to be deterministic
            chosen_index = random.randint(0, len(available_card_ids) - 1)
            chosen_card_id = available_card_ids[chosen_index]
            card_slot = game.create_card_slot(player, self._card_id_to_minion[chosen_card_id])
            game.summon_minion(card_slot)


class Freeze(OneTimeEffect):
    def __init__(self, selection):
        self.selection = selection

    def execute(self, game, em_node):
        selected_card_slots = self.selection.get_selected_card_slots(game, em_node)
        em_nodes_to_add = []
        for selected_card_slot in selected_card_slots:
            em_node = EffectManagerNode(
                effect=Frozen(),
                affected_slot=selected_card_slot,
                origin_slot=em_node.origin_slot,
                silenceable=True
            )
            em_nodes_to_add.append(em_node)

        return EffectManagerNodePlan(to_add=em_nodes_to_add)