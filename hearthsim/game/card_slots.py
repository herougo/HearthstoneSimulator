from hearthsim.utils.hash_generation import generate_random_hash
from hearthsim.cards.core import Card
from hearthsim.effects.effects_activated import HeroPowerEffect
from hearthsim.game.effect_manager import EffectManagerNode

class CardSlot:
    def __init__(self, card_id, player, game):
        self.hash = generate_random_hash()
        self.card_id = card_id
        self.player = player
        self.card = Card.from_card_id(self.card_id)
        self.game = game
        self.game.register_card_slot(self)

    def iter_em_nodes(self):
        for em_node in self.game.effect_manager.iter_em_nodes_by_slot_hash(self.hash):
            yield em_node

    def __str__(self):
        return f'CardSlot(card_id={self.card_id}, player={self.player}, hash={self.hash}, game=...)'

class WeaponCardSlot(CardSlot):
    mana = None
    attack = None
    durability = None

    def __init__(self, card_id, player, game):
        super(WeaponCardSlot, self).__init__(card_id, player, game)
        self.mana = self.card.mana
        self.attack = self.card.attack
        self.durability = self.card.durability

class HeroCardSlot(CardSlot):
    current_mana = 0
    available_mana = 0
    maximum_mana = 10
    max_health = 30
    health = 30
    armour = 0
    hero_power_used_this_turn = False

    _hero_power_cost = None
    _hero_power_effect = None

    # other metadata
    n_taunt = 0
    n_charge = 0
    n_windfury = 0
    n_stealth = 0
    n_targetable_with_spell_or_hp = 0
    has_sleep = False
    attacks_this_turn = 0

    def __init__(self, card_id, player, game):
        super(HeroCardSlot, self).__init__(card_id, player, game)

    def setup_hero_power(self):
        self._hero_power_cost = self.card.hero_power_cost
        self._hero_power_effect = HeroPowerEffect(self.card.hero_power_effect.copy())
        em_node = EffectManagerNode(self._hero_power_effect,
                                    affected_slot=self,
                                    origin_slot=self,
                                    silenceable=False)
        self.game.effect_manager.add_effect(em_node)

    @property
    def hero_power_effect(self):
        return self._hero_power_effect

    @property
    def hero_power_cost(self):
        return self._hero_power_cost

    @property
    def has_taunt(self):
        return self.n_taunt > 0

    @property
    def has_charge(self):
        return self.n_charge > 0

    @property
    def has_windfury(self):
        return self.n_windfury > 0

    @property
    def has_stealth(self):
        return self.n_stealth > 0

    @property
    def targetable_with_spell_or_hp(self):
        return self.n_targetable_with_spell_or_hp == 0

    @property
    def attack(self):
        if self.game.weapons[self.player]:
            return self.game.weapons[self.player].attack
        else:
            return 0  # ?????


class MinionCardSlot(CardSlot):
    # stats
    mana = None
    attack = None
    max_health = None
    health = None

    # other metadata
    n_taunt = 0
    n_charge = 0
    n_windfury = 0
    n_stealth = 0
    has_sleep = False
    silenced = False
    attacks_this_turn = 0

    def __init__(self, card_id, player, game):
        super(MinionCardSlot, self).__init__(card_id, player, game)
        # self.reset(silenced=False)
        self.compute_stats()

    def play(self):
        pass

    def compute_stats(self):
        self.mana = self.card.mana
        self.attack = self.card.attack
        self.max_health = self.card.health
        if self.health is None:
            self.health = self.max_health
        prev_health = self.health

        for em_node in self.iter_em_nodes():
            em_node.effect.adjust_stats(self)

        self.attack = max(0, self.attack)

        if self.health < prev_health:  # if some buffs wear off or get silenced
            self.health = min(self.max_health, prev_health)

        return (self.mana, self.attack, self.health)

    @property
    def has_taunt(self):
        return self.n_taunt > 0

    @property
    def has_charge(self):
        return self.n_charge > 0

    @property
    def has_windfury(self):
        return self.n_windfury > 0

    @property
    def has_stealth(self):
        return self.n_stealth > 0

    @property
    def n_possible_attacks(self):
        if self.has_windfury:
            return 2
        else:
            return 1

    def switch_players(self):
        self.player = 1 - self.player
        # add and remove taunts using self.game
        raise NotImplementedError()