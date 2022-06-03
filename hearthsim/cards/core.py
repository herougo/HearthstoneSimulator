from hearthsim.cards.card_registry import CARD_REGISTRY

class Card:
    card_id = None
    collectible = True

    @classmethod
    def from_card_id(self, card_id):
        return CARD_REGISTRY[card_id]()

    @property
    def card_type(self):
        raise NotImplementedError()

class OriginalHeroCard(Card):
    hero_power_cost = None
    hero_power_effect = None
    collectible = False
    effects = (OnTurnStart(DrawCard(PLAYER)),
               OnTurnStart(GainManaCrystals(PLAYER, 1)),
               OnTurnStart(RefreshAllManaCrystals(PLAYER)),
               OnTurnEnd(RefreshMinionAttacks(ALL_FRIENDLY_CHARACTERS)),
               OnTurnEnd(RefreshHeroPower(PLAYER)))

    @property
    def card_type(self):
        return CardTypes.original_hero.value

class MinionCard(Card):
    mana = None
    attack = None
    health = None
    in_play_effects = tuple()

    @property
    def card_type(self):
        return CardTypes.minion.value

class WeaponCard(Card):
    mana = None
    attack = None
    durability = None
    in_play_effects = tuple()

    @property
    def card_type(self):
        return CardTypes.weapon.value