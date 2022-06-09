from hearthsim.cards.card_registry import register_card
from hearthsim.cards.types_of_cards import MinionCard
from hearthsim.utils.enums import HSClass, Tag


@register_card(card_id='CU001')
class DamagedGolem(MinionCard):
    name = 'Damaged Golem'
    hs_class = HSClass.NEUTRAL.value
    mana = 1
    attack = 2
    health = 1
    tag = Tag.MECH.value
    in_play_effects = tuple()
    collectible = False