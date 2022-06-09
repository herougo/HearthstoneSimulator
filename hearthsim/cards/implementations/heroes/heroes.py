from hearthsim.cards.card_registry import register_card
from hearthsim.selections.predefined_constants import SELECT_CHARACTER, PLAYER, OPP
from hearthsim.cards.types_of_cards import OriginalHeroCard
from hearthsim.cards.implementations.heroes.uncollectible import (RogueDagger12, SilverHandRecruit, SearingTotem,
                                                                  HealingTotem, StoneclawTotem, StrengthTotem)
from hearthsim.effects.core import OneTimeEffectSequence
from hearthsim.effects.effects_one_time import (Heal, EquipWeapon, DealDamage, ChangeAttack, GainArmour, DrawCard,
                                                SummonMinion, SummonMinionLikeShamanHP)
from hearthsim.effects.effects_wrapped import TimeLimitedEffect
from hearthsim.utils.enums import EffectTimeLimit, HSClass

@register_card(card_id='priest')
class Priest(OriginalHeroCard):
    name = 'Priest'
    hs_class = HSClass.PRIEST.value
    hero_power_cost = 2
    hero_power_effect = Heal(SELECT_CHARACTER, 2)


@register_card(card_id='rogue')
class Rogue(OriginalHeroCard):
    name = 'Rogue'
    hs_class = HSClass.ROGUE.value
    hero_power_cost = 2
    hero_power_effect = EquipWeapon(PLAYER, RogueDagger12())


@register_card(card_id='druid')
class Druid(OriginalHeroCard):
    name = 'Druid'
    hs_class = HSClass.DRUID.value
    hero_power_cost = 2
    hero_power_effect = OneTimeEffectSequence(
        GainArmour(PLAYER, 1),
        TimeLimitedEffect(
            ChangeAttack(PLAYER, 1),
            until_when=EffectTimeLimit.END_OF_TURN.value)
    )


@register_card(card_id='shaman')
class Shaman(OriginalHeroCard):
    name = 'Shaman'
    hs_class = HSClass.SHAMAN.value
    hero_power_cost = 2
    hero_power_effect = SummonMinionLikeShamanHP((
        SearingTotem(), HealingTotem(), StoneclawTotem(), StrengthTotem()
    ))


@register_card(card_id='warlock')
class Warlock(OriginalHeroCard):
    name = 'Warlock'
    hs_class = HSClass.WARLOCK.value
    hero_power_cost = 2
    hero_power_effect = OneTimeEffectSequence(
        DealDamage(PLAYER, 2),
        DrawCard(PLAYER)
    )


@register_card(card_id='paladin')
class Paladin(OriginalHeroCard):
    name = 'Paladin'
    hs_class = HSClass.PALADIN.value
    hero_power_cost = 2
    hero_power_effect = SummonMinion(SilverHandRecruit())


@register_card(card_id='warrior')
class Warrior(OriginalHeroCard):
    name = 'Warrior'
    hs_class = HSClass.WARRIOR.value
    hero_power_cost = 2
    hero_power_effect = GainArmour(PLAYER, 2)


@register_card(card_id='hunter')
class Hunter(OriginalHeroCard):
    name = 'Hunter'
    hs_class = HSClass.HUNTER.value
    hero_power_cost = 2
    hero_power_effect = DealDamage(OPP, 2)


@register_card(card_id='mage')
class Mage(OriginalHeroCard):
    name = 'Mage'
    hs_class = HSClass.MAGE.value
    hero_power_cost = 2
    hero_power_effect = DealDamage(SELECT_CHARACTER, 1)


@register_card(card_id='demon_hunter')
class DemonHunter(OriginalHeroCard):
    name = 'Demon Hunter'
    hs_class = HSClass.DEMON_HUNTER.value
    hero_power_cost = 1
    hero_power_effect = TimeLimitedEffect(
        ChangeAttack(PLAYER, 1),
        until_when=EffectTimeLimit.END_OF_TURN.value)