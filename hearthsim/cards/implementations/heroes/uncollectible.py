from hearthsim.cards.card_registry import register_card
from hearthsim.cards.types_of_cards import WeaponCard, MinionCard
from hearthsim.effects.effects_continuous import Taunt
from hearthsim.effects.effects_trigger import OnTurnEnd
from hearthsim.effects.effects_one_time import Heal, ChangeAttack
from hearthsim.selections.predefined_constants import ALL_FRIENDLY_MINIONS, RANDOM_OTHER_FRIENDLY_MINION
from hearthsim.utils.enums import HSClass


@register_card(card_id='HU001')
class RogueDagger12(WeaponCard):
    name = 'Rogue Dagger 1/2'
    hs_class = HSClass.ROGUE.value
    mana = 1
    attack = 1
    durability = 2
    collectible = False


@register_card(card_id='HU002')
class SilverHandRecruit(MinionCard):
    name = 'Silver Hand Recruit'
    hs_class = HSClass.PALADIN.value
    mana = 1
    attack = 1
    health = 1
    in_play_effects = tuple()
    collectible = False


@register_card(card_id='HU003')
class SearingTotem(MinionCard):
    name = 'Searing Totem'
    hs_class = HSClass.SHAMAN.value
    mana = 1
    attack = 1
    health = 1
    in_play_effects = tuple()
    collectible = False


@register_card(card_id='HU004')
class StoneclawTotem(MinionCard):
    name = 'Stoneclaw Totem'
    hs_class = HSClass.SHAMAN.value
    mana = 1
    attack = 0
    health = 2
    in_play_effects = Taunt()
    collectible = False


@register_card(card_id='HU004')
class StrengthTotem(MinionCard):
    name = 'Strength Totem'
    hs_class = HSClass.SHAMAN.value
    mana = 1
    attack = 0
    health = 2
    in_play_effects = OnTurnEnd(ChangeAttack(RANDOM_OTHER_FRIENDLY_MINION, 1))
    collectible = False


@register_card(card_id='HU004')
class HealingTotem(MinionCard):
    name = 'Healing Totem'
    hs_class = HSClass.SHAMAN.value
    mana = 1
    attack = 0
    health = 2
    in_play_effects = OnTurnEnd(Heal(ALL_FRIENDLY_MINIONS, 1))
    collectible = False

