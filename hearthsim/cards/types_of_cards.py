from hearthsim.cards.core import Card
from hearthsim.utils.enums import CardTypes
from hearthsim.effects.effects_trigger import (OnTurnStart, OnTurnEnd)
from hearthsim.effects.effects_one_time import (DrawCard, GainManaCrystals, RefreshAllManaCrystals,
                                                RefreshMinionAttacks, RefreshHeroPower)
from hearthsim.selections.predefined_constants import (PLAYER, ALL_FRIENDLY_CHARACTERS)


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
        return CardTypes.ORIGINAL_HERO.value


class MinionCard(Card):
    mana = None
    attack = None
    health = None
    tag = None
    in_play_effects = tuple()

    @property
    def card_type(self):
        return CardTypes.MINION.value


class WeaponCard(Card):
    mana = None
    attack = None
    durability = None
    in_play_effects = tuple()

    @property
    def card_type(self):
        return CardTypes.WEAPON.value


class SpellCard(Card):
    mana = None
    when_played_effects = tuple()

    @property
    def card_type(self):
        return CardTypes.SPELL.value