from hearthsim.cards.card_registry import register_card
from hearthsim.utils.enums import EffectTimeLimit, HSClass, Tag, PlayerChoice
from hearthsim.cards.types_of_cards import MinionCard
from hearthsim.selections.predefined_constants import (PLAYER, OPP, OWN_SELF, ADJACENT_MINIONS, RANDOM_OTHER_CHARACTER,
                                                       SELECT_OTHER_CHARACTER, SELECT_OTHER_MINION,
                                                       SELECT_OTHER_FRIENDLY_MINION)
from hearthsim.effects.core import ConditionalEffect
from hearthsim.effects.effects_trigger import Battlecry, Deathrattle, WhenOtherMinionDies
from hearthsim.effects.effects_wrapped import TimeLimitedEffect, NEffects
from hearthsim.effects.effects_one_time import (DrawCard, ChangeAttack, DealDamage, ReturnMinionToHand, Heal,
                                                SummonMinion, Silence)
from hearthsim.effects.effects_continuous import (DivineShield, Taunt, Charge, Stealth, Windfury, AttackBuff,
                                                  CantBeTargetedBySpellsOrHP, ContinuousSelectionFieldEffect)
from hearthsim.conditions.conditions import WhileWeaponEquipped, WhileSelfDamaged
from hearthsim.game.utils import weapon_attack
from hearthsim.cards.implementations.classic.uncollectible import DamagedGolem


@register_card(card_id='C001')
class Wisp(MinionCard):
    name = 'Wisp'
    hs_class = HSClass.NEUTRAL.value
    mana = 0
    attack = 1
    health = 1
    in_play_effects = tuple()


@register_card(card_id='C002')
class AbusiveSergeant(MinionCard):
    name = 'Abusive Sergeant'
    hs_class = HSClass.NEUTRAL.value
    mana = 1
    attack = 1
    health = 1
    def __init__(self):
        self.in_play_effects = Battlecry(
            TimeLimitedEffect(
                ChangeAttack(SELECT_OTHER_FRIENDLY_MINION, 2),
                until_when=EffectTimeLimit.END_OF_TURN.value))


@register_card(card_id='C003')
class ArgentSquire(MinionCard):
    name = 'Argent Squire'
    hs_class = HSClass.NEUTRAL.value
    mana = 1
    attack = 1
    health = 1
    def __init__(self):
        self.in_play_effects = DivineShield()


@register_card(card_id='C004')
class LeperGnome(MinionCard):
    name = 'Leper Gnome'
    hs_class = HSClass.NEUTRAL.value
    mana = 1
    attack = 2
    health = 1
    def __init__(self):
        self.in_play_effects = Deathrattle(
            DealDamage(OPP, 2))


@register_card(card_id='C005')
class Shieldbearer(MinionCard):
    name = 'Shieldbearer'
    hs_class = HSClass.NEUTRAL.value
    mana = 1
    attack = 0
    health = 4
    def __init__(self):
        self.in_play_effects = Taunt()


@register_card(card_id='C006')
class SouthseaDeckhand(MinionCard):
    name = 'Southsea Deckhand'
    hs_class = HSClass.NEUTRAL.value
    mana = 1
    attack = 2
    health = 1
    tag = Tag.PIRATE.value
    def __init__(self):
        self.in_play_effects = ConditionalEffect(
            WhileWeaponEquipped(),
            Charge())


@register_card(card_id='C007')
class WorgenInfiltrator(MinionCard):
    name = 'Worgen Infiltrator'
    hs_class = HSClass.NEUTRAL.value
    mana = 1
    attack = 2
    health = 1
    def __init__(self):
        self.in_play_effects = Stealth()


@register_card(card_id='C008')
class YoungDragonhawk(MinionCard):
    name = 'Young Dragonhawk'
    hs_class = HSClass.NEUTRAL.value
    mana = 1
    attack = 1
    health = 1
    tag = Tag.BEAST.value
    def __init__(self):
        self.in_play_effects = Windfury()


@register_card(card_id='C009')
class AmaniBerserker(MinionCard):
    name = 'Amani Berserker'
    hs_class = HSClass.NEUTRAL.value
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
    hs_class = HSClass.NEUTRAL.value
    mana = 2
    attack = 2
    health = 3
    tag = Tag.PIRATE.value
    def __init__(self):
        self.in_play_effects = Battlecry(
            ChangeAttack(OWN_SELF, weapon_attack)
        )


@register_card(card_id='C011')
class DireWolfAlpha(MinionCard):
    name = 'Dire Wolf Alpha'
    hs_class = HSClass.NEUTRAL.value
    mana = 2
    attack = 2
    health = 2
    tag = Tag.BEAST.value
    def __init__(self):
        self.in_play_effects = ContinuousSelectionFieldEffect(ADJACENT_MINIONS,
                                                              AttackBuff(1))


@register_card(card_id='C012')
class FaerieDragon(MinionCard):
    name = 'Faerie Dragon'
    hs_class = HSClass.NEUTRAL.value
    mana = 2
    attack = 3
    health = 2
    tag = Tag.DRAGON.value
    def __init__(self):
        self.in_play_effects = CantBeTargetedBySpellsOrHP()


@register_card(card_id='C013')
class LootHoarder(MinionCard):
    name = 'Loot Hoarder'
    hs_class = HSClass.NEUTRAL.value
    mana = 2
    attack = 2
    health = 1
    def __init__(self):
        self.in_play_effects = Deathrattle(DrawCard(PLAYER))


@register_card(card_id='C014')
class MadBomber(MinionCard):
    name = 'Mad Bomber'
    hs_class = HSClass.NEUTRAL.value
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
    hs_class = HSClass.NEUTRAL.value
    mana = 2
    attack = 3
    health = 2
    def __init__(self):
        self.in_play_effects = Battlecry(ReturnMinionToHand(
            SELECT_OTHER_FRIENDLY_MINION))


@register_card(card_id='C016')
class EarthenRingFarseer(MinionCard):
    name = 'Earthen Ring Farseer'
    hs_class = HSClass.NEUTRAL.value
    mana = 3
    attack = 3
    health = 3
    def __init__(self):
        self.in_play_effects = Battlecry(Heal(
            SELECT_OTHER_CHARACTER, 3))


@register_card(card_id='C017')
class FlesheatingGhoul(MinionCard):
    name = 'Flesheating Ghoul'
    hs_class = HSClass.NEUTRAL.value
    mana = 3
    attack = 3
    health = 3
    def __init__(self):
        self.in_play_effects = WhenOtherMinionDies(ChangeAttack(
            OWN_SELF, 1
        ), player_choice=PlayerChoice.BOTH.value)


@register_card(card_id='C018')
class HarvestGolem(MinionCard):
    name = 'Harvest Golem'
    hs_class = HSClass.NEUTRAL.value
    mana = 3
    attack = 2
    health = 3
    tag = Tag.MECH.value
    def __init__(self):
        self.in_play_effects = Deathrattle(SummonMinion(DamagedGolem()))


@register_card(card_id='C019')
class IronbeakOwl(MinionCard):
    name = 'Ironbeak Owl'
    hs_class = HSClass.NEUTRAL.value
    mana = 3
    attack = 2
    health = 1
    tag = Tag.BEAST.value
    def __init__(self):
        self.in_play_effects = Battlecry(Silence(SELECT_OTHER_MINION))


@register_card(card_id='C020')
class JunglePanther(MinionCard):
    name = 'Jungle Panther'
    hs_class = HSClass.NEUTRAL.value
    mana = 3
    attack = 4
    health = 2
    def __init__(self):
        self.in_play_effects = Stealth()


@register_card(card_id='C021')
class RagingWorgen(MinionCard):
    name = 'Raging Worgen'
    hs_class = HSClass.NEUTRAL.value
    mana = 3
    attack = 3
    health = 3
    def __init__(self):
        self.in_play_effects = ConditionalEffect(
            WhileSelfDamaged(),
            (AttackBuff(1), Windfury())
        )


@register_card(card_id='C022')
class ScarletCrusader(MinionCard):
    name = 'Scarlet Crusader'
    hs_class = HSClass.NEUTRAL.value
    mana = 3
    attack = 3
    health = 1
    def __init__(self):
        self.in_play_effects = DivineShield()


@register_card(card_id='C023')
class TaurenWarrior(MinionCard):
    name = 'Tauren Warrior'
    hs_class = HSClass.NEUTRAL.value
    mana = 3
    attack = 2
    health = 3
    def __init__(self):
        self.in_play_effects = (
            Taunt(),
            ConditionalEffect(WhileSelfDamaged(), AttackBuff(3))
        )


@register_card(card_id='C024')
class ThrallmarFarseer(MinionCard):
    name = 'Thrallmar Farseer'
    hs_class = HSClass.NEUTRAL.value
    mana = 3
    attack = 2
    health = 3
    def __init__(self):
        self.in_play_effects = Windfury()


@register_card(card_id='C025')
class AncientBrewmaster(MinionCard):
    name = 'Ancient Brewmaster'
    hs_class = HSClass.NEUTRAL.value
    mana = 4
    attack = 5
    health = 4
    def __init__(self):
        self.in_play_effects = Battlecry(ReturnMinionToHand(SELECT_OTHER_FRIENDLY_MINION))


@register_card(card_id='C026')
class CultMaster(MinionCard):
    name = 'Cult Master'
    hs_class = HSClass.NEUTRAL.value
    mana = 4
    attack = 4
    health = 2
    def __init__(self):
        self.in_play_effects = WhenOtherMinionDies(DrawCard(PLAYER), player_choice=PlayerChoice.PLAYER.value)