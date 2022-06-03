from enum import Enum

class EffectTimeLimit(Enum):
    NO_LIMIT = 0
    END_OF_TURN = 1
    END_OF_OPP_TURN = 2

class PlayerChoice(Enum):
    both = 0
    player = 1
    opponent = 2

class EffectType(Enum):
    continuous = 0
    trigger = 1
    onetime = 2
    wrapper = 3
    conditional = 4

class EffectArea(Enum):
    field = 0
    hand = 1
    deck = 2
    all = 3

class Events(Enum):
    start_turn = 2
    end_turn = 3
    weapon_destroyed = 4
    weapon_equipped = 5
    after_attacker_initial_combat_damage = 7
    after_defender_initial_combat_damage = 24
    after_attacker_attacked = 25
    after_combat_damage = 8
    calculate_stats = 9
    minion_put_in_play = 20
    minion_battlecry = 21
    minion_summoned = 22
    minion_dies = 23
    activate_hero_power = 26
    hero_power_end = 27

class CardTypes(Enum):
    minion = 0
    spell = 1
    weapon = 2
    original_hero = 3

class HSClass(Enum):
    druid = 'druid'
    mage = 'mage'
    hunter = 'hunter'
    warlock = 'warlock'
    shaman = 'shaman'
    demon_hunter = 'demon_hunter'
    priest = 'priest'
    warrior = 'warrior'
    rogue = 'rogue'
    paladin = 'paladin'
    neutral = 'neutral'

class CanAttackResponse(Enum):
    yes = 0
    attacked_enough = 1
    asleep = 2
    defender_has_stealth = 3
    zero_attack = 4
    disobeys_taunt = 5

class Actions(Enum):
    end_turn = 'end_turn'
    play = 'play'
    attack = 'attack'
    select = 'select'
    hero_power = 'hero_power'