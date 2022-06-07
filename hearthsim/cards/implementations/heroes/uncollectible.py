from hearthsim.cards.card_registry import register_card
from hearthsim.cards.types_of_cards import WeaponCard, MinionCard
from hearthsim.utils.enums import HSClass

@register_card(card_id='HU001')
class RogueDagger12(WeaponCard):
    name = 'Rogue Dagger 1/2'
    hs_class = HSClass.rogue.value
    mana = 1
    attack = 1
    durability = 2
    collectible = False


@register_card(card_id='HU002')
class SilverHandRecruit(MinionCard):
    name = 'Silver Hand Recruit'
    hs_class = HSClass.paladin.value
    mana = 1
    attack = 1
    health = 1
    in_play_effects = tuple()
    collectible = False

