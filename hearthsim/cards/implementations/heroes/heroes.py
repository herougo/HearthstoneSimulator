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

@register_card(card_id='rogue')
class Druid(OriginalHeroCard):
    name = 'Druid'
    hero_power_cost = 2
    hero_power_effect = None

@register_card(card_id='rogue')
class Shaman(OriginalHeroCard):
    name = 'Shaman'
    hero_power_cost = 2
    hero_power_effect = None

@register_card(card_id='rogue')
class Warlock(OriginalHeroCard):
    name = 'Warlock'
    hero_power_cost = 2
    hero_power_effect = None

@register_card(card_id='rogue')
class Paladin(OriginalHeroCard):
    name = 'Paladin'
    hero_power_cost = 2
    hero_power_effect = None

@register_card(card_id='rogue')
class Warrior(OriginalHeroCard):
    name = 'Warrior'
    hero_power_cost = 2
    hero_power_effect = None

@register_card(card_id='rogue')
class Hunter(OriginalHeroCard):
    name = 'Hunter'
    hero_power_cost = 2
    hero_power_effect = None

@register_card(card_id='rogue')
class Mage(OriginalHeroCard):
    name = 'Mage'
    hero_power_cost = 2
    hero_power_effect = DealDamage(SELECT_CHARACTER, 1)

@register_card(card_id='rogue')
class DemonHunter(OriginalHeroCard):
    name = 'Demon Hunter'
    hero_power_cost = 1
    hero_power_effect = None