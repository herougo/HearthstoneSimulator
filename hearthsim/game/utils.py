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
        (player_choice == PlayerChoice.both.value) or
        ((player_choice == PlayerChoice.player.value) and (player == ref_player)) or
        ((player_choice == PlayerChoice.opponent.value) and (player != ref_player)))
    return result

def weapon_attack(game, card_slot):
    weapon = game.weapons[card_slot.player]
    if not weapon:
        return 0

    return weapon.attack

def attackable_characters(card_slot):
    pass