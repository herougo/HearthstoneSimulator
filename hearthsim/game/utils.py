from hearthsim.utils.enums import PlayerChoice, CardTypes
from hearthsim.game.card_slots import MinionCardSlot, WeaponCardSlot, SpellCardSlot, HeroCardSlot

def targetable_with_hero_power(source_player, target_card_slot):
    if source_player != target_card_slot.player and target_card_slot.has_stealth:
        return False

    return target_card_slot.targetable_with_spell_or_hp


def targetable_with_spell(source_player, target_card_slot):
    if source_player != target_card_slot.player and target_card_slot.has_stealth:
        return False

    return target_card_slot.targetable_with_spell_or_hp


def is_player_affected(player, ref_player, player_choice):
    # ref_player can be turn
    result = (
        (player_choice == PlayerChoice.BOTH.value) or
        ((player_choice == PlayerChoice.PLAYER.value) and (player == ref_player)) or
        ((player_choice == PlayerChoice.OPPONENT.value) and (player != ref_player)))
    return result


def weapon_attack(game, card_slot):
    weapon = game.weapons[card_slot.player]
    if not weapon:
        return 0

    return weapon.attack


def attackable_characters(card_slot):
    pass


def matches_card_type(desired_card_type, card_slot):
    if desired_card_type == CardTypes.ALL.value:
        return True
    elif desired_card_type == CardTypes.MINION.value:
        return isinstance(card_slot, MinionCardSlot)
    elif desired_card_type == CardTypes.SPELL.value:
        return isinstance(card_slot, SpellCardSlot)
    elif desired_card_type == CardTypes.WEAPON.value:
        return isinstance(card_slot, WeaponCardSlot)
    elif desired_card_type == CardTypes.ORIGINAL_HERO.value:
        return isinstance(card_slot, HeroCardSlot)
    else:
        raise NotImplementedError()