from hearthsim.cards.card_registry import register_card
from hearthsim.selections.predefined_constants import SELECT_CHARACTER, PLAYER, OPP
from hearthsim.cards.types_of_cards import OriginalHeroCard
from hearthsim.cards.implementations.heroes.uncollectible import RogueDagger12
from hearthsim.effects.core import OneTimeEffectSequence
from hearthsim.effects.effects_one_time import Heal, EquipWeapon, DealDamage, ChangeAttack, GainArmour, DrawCard
from hearthsim.effects.effects_wrapped import TimeLimitedEffect
from hearthsim.utils.enums import EffectTimeLimit

@register_card(card_id='priest')
class Priest(OriginalHeroCard):
    name = 'Priest'
    hero_power_cost = 2
    hero_power_effect = Heal(SELECT_CHARACTER, 2)


@register_card(card_id='rogue')
class Rogue(OriginalHeroCard):
    name = 'Rogue'
    hero_power_cost = 2
    hero_power_effect = EquipWeapon(PLAYER, RogueDagger12())


@register_card(card_id='druid')
class Druid(OriginalHeroCard):
    name = 'Druid'
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
    hero_power_cost = 2
    hero_power_effect = None


@register_card(card_id='warlock')
class Warlock(OriginalHeroCard):
    name = 'Warlock'
    hero_power_cost = 2
    hero_power_effect = OneTimeEffectSequence(
        DealDamage(PLAYER, 2),
        DrawCard(PLAYER)
    )


@register_card(card_id='paladin')
class Paladin(OriginalHeroCard):
    name = 'Paladin'
    hero_power_cost = 2
    hero_power_effect = None


@register_card(card_id='warrior')
class Warrior(OriginalHeroCard):
    name = 'Warrior'
    hero_power_cost = 2
    hero_power_effect = GainArmour(PLAYER, 2)


@register_card(card_id='hunter')
class Hunter(OriginalHeroCard):
    name = 'Hunter'
    hero_power_cost = 2
    hero_power_effect = DealDamage(OPP, 2)


@register_card(card_id='mage')
class Mage(OriginalHeroCard):
    name = 'Mage'
    hero_power_cost = 2
    hero_power_effect = DealDamage(SELECT_CHARACTER, 1)


@register_card(card_id='demon_hunter')
class DemonHunter(OriginalHeroCard):
    name = 'Demon Hunter'
    hero_power_cost = 1
    hero_power_effect = TimeLimitedEffect(
        ChangeAttack(PLAYER, 1),
        until_when=EffectTimeLimit.END_OF_TURN.value)