from hearthsim.cards.card_registry import register_card
from hearthsim.cards.types_of_cards import SpellCard
from hearthsim.utils.enums import HSClass
from hearthsim.effects.effects_one_time import GainCurrentManaCrystals
from hearthsim.selections.predefined_constants import PLAYER


@register_card(card_id='F001')
class Coin(SpellCard):
    name = 'Coin'
    hs_class = HSClass.NEUTRAL.value
    mana = 0
    collectible = False
    when_played_effects = GainCurrentManaCrystals(PLAYER, 1)