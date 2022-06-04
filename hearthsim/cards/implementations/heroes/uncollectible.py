from hearthsim.cards.card_registry import register_card
from hearthsim.cards.types_of_cards import WeaponCard

@register_card(card_id='HU001')
class RogueDagger12(WeaponCard):
    name = 'Rogue Dagger 1/2'
    mana = 1
    attack = 1
    durability = 2