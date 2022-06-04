from hearthsim.cards.card_registry import register_card
from hearthsim.utils.enums import (EffectTimeLimit, HSClass)
from hearthsim.cards.types_of_cards import MinionCard
from hearthsim.selections.predefined_constants import (PLAYER, OPP, OWN_SELF, ADJACENT_MINIONS, RANDOM_OTHER_CHARACTER)
from hearthsim.effects.core import ConditionalEffect
from hearthsim.effects.effects_trigger import (Battlecry, Deathrattle)
from hearthsim.effects.effects_wrapped import (TimeLimitedEffect, NEffects)
from hearthsim.effects.effects_one_time import (DrawCard, ChangeAttack, DealDamage, ReturnMinionToHand)
from hearthsim.effects.effects_continuous import (DivineShield, Taunt, Charge, Stealth, Windfury, AttackBuff,
                                                  CantBeTargetedBySpellsOrHP, ContinuousSelectionFieldEffect)
from hearthsim.selections.predefined_constants import SELECT_FRIENDLY_MINION
from hearthsim.conditions.conditions import (WhileWeaponEquipped, WhileSelfDamaged)
from hearthsim.game.utils import weapon_attack


@register_card(card_id='C001')
class Wisp(MinionCard):
    name = 'Wisp'
    hs_class = HSClass.neutral.value
    mana = 0
    attack = 1
    health = 1
    in_play_effects = tuple()


@register_card(card_id='C002')
class AbusiveSergeant(MinionCard):
    name = 'Abusive Sergeant'
    hs_class = HSClass.neutral.value
    mana = 1
    attack = 1
    health = 1
    def __init__(self):
        self.in_play_effects = Battlecry(
            TimeLimitedEffect(
                ChangeAttack(SELECT_FRIENDLY_MINION, 2),
                until_when=EffectTimeLimit.END_OF_TURN.value))


@register_card(card_id='C003')
class ArgentSquire(MinionCard):
    name = 'Argent Squire'
    hs_class = HSClass.neutral.value
    mana = 1
    attack = 1
    health = 1
    def __init__(self):
        self.in_play_effects = DivineShield()


@register_card(card_id='C004')
class LeperGnome(MinionCard):
    name = 'Leper Gnome'
    hs_class = HSClass.neutral.value
    mana = 1
    attack = 2
    health = 1
    def __init__(self):
        self.in_play_effects = Deathrattle(
            DealDamage(OPP, 2))


@register_card(card_id='C005')
class Shieldbearer(MinionCard):
    name = 'Shieldbearer'
    hs_class = HSClass.neutral.value
    mana = 1
    attack = 0
    health = 4
    def __init__(self):
        self.in_play_effects = Taunt()


@register_card(card_id='C006')
class SouthseaDeckhand(MinionCard):
    name = 'Southsea Deckhand'
    hs_class = HSClass.neutral.value
    mana = 1
    attack = 2
    health = 1
    def __init__(self):
        self.in_play_effects = ConditionalEffect(
            WhileWeaponEquipped(),
            Charge())


@register_card(card_id='C007')
class WorgenInfiltrator(MinionCard):
    name = 'Worgen Infiltrator'
    hs_class = HSClass.neutral.value
    mana = 1
    attack = 2
    health = 1
    def __init__(self):
        self.in_play_effects = Stealth()


@register_card(card_id='C008')
class YoungDragonhawk(MinionCard):
    name = 'Young Dragonhawk'
    hs_class = HSClass.neutral.value
    mana = 1
    attack = 1
    health = 1
    def __init__(self):
        self.in_play_effects = Windfury()


@register_card(card_id='C009')
class AmaniBerserker(MinionCard):
    name = 'Amani Berserker'
    hs_class = HSClass.neutral.value
    mana = 2
    attack = 2
    health = 3
    def __init__(self):
        self.in_play_effects = ConditionalEffect(
            WhileSelfDamaged(),
            AttackBuff(3)
        )


@register_card(card_id='C010')
class BloodsailRaider(MinionCard):
    name = 'Bloodsail Raider'
    hs_class = HSClass.neutral.value
    mana = 2
    attack = 2
    health = 3
    def __init__(self):
        self.in_play_effects = Battlecry(
            ChangeAttack(OWN_SELF, weapon_attack)
        )


@register_card(card_id='C011')
class DireWolfAlpha(MinionCard):
    name = 'Dire Wolf Alpha'
    hs_class = HSClass.neutral.value
    mana = 2
    attack = 2
    health = 2
    def __init__(self):
        self.in_play_effects = ContinuousSelectionFieldEffect(ADJACENT_MINIONS,
                                                              AttackBuff(1))


@register_card(card_id='C012')
class FaerieDragon(MinionCard):
    name = 'Faerie Dragon'
    hs_class = HSClass.neutral.value
    mana = 2
    attack = 3
    health = 2
    def __init__(self):
        self.in_play_effects = CantBeTargetedBySpellsOrHP()


@register_card(card_id='C013')
class LootHoarder(MinionCard):
    name = 'Loot Hoarder'
    hs_class = HSClass.neutral.value
    mana = 2
    attack = 2
    health = 1
    def __init__(self):
        self.in_play_effects = Deathrattle(DrawCard(PLAYER))


@register_card(card_id='C014')
class MadBomber(MinionCard):
    name = 'Mad Bomber'
    hs_class = HSClass.neutral.value
    mana = 2
    attack = 3
    health = 2
    def __init__(self):
        self.in_play_effects = Battlecry(NEffects(
            DealDamage(RANDOM_OTHER_CHARACTER, 1),
            n=3))


@register_card(card_id='C015')
class YouthfulBrewmaster(MinionCard):
    name = 'Youthful Brewmaster'
    hs_class = HSClass.neutral.value
    mana = 2
    attack = 3
    health = 2
    def __init__(self):
        self.in_play_effects = Battlecry(ReturnMinionToHand(
            SELECT_FRIENDLY_MINION))