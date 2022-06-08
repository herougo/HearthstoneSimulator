from enum import Enum

class EffectTimeLimit(Enum):
    NO_LIMIT = 0
    END_OF_TURN = 1
    END_OF_OPP_TURN = 2

class PlayerChoice(Enum):
    BOTH = 0
    PLAYER = 1
    OPPONENT = 2

class EffectType(Enum):
    CONTINUOUS = 0
    TRIGGER = 1
    ONE_TIME = 2
    WRAPPER = 3
    CONDITIONAL = 4

class EffectArea(Enum):
    FIELD = 0
    HAND = 1
    DECK = 2
    ALL = 3

class Events(Enum):
    START_TURN = 2
    END_TURN = 3
    WEAPON_DESTROYED = 4
    WEAPON_EQUIPPED = 5
    AFTER_ATTACKER_INITIAL_COMBAT_DAMAGE = 7
    AFTER_DEFENDER_INITIAL_COMBAT_DAMAGE = 24
    AFTER_ATTACKER_ATTACKED = 25
    AFTER_COMBAT_DAMAGE = 8
    CALCULATE_STATS = 9
    MINION_PUT_IN_PLAY = 20
    MINION_BATTLECRY = 21
    MINION_SUMMONED = 22
    MINION_DIES = 23
    ACTIVATE_HERO_POWER = 26
    HERO_POWER_END = 27
    MINION_RETURNED_TO_HAND = 28
    AFTER_SPELL_ACTIVATED = 29

class CardTypes(Enum):
    MINION = 0
    SPELL = 1
    WEAPON = 2
    ORIGINAL_HERO = 3

class HSClass(Enum):
    DRUID = 'druid'
    MAGE = 'mage'
    HUNTER = 'hunter'
    WARLOCK = 'warlock'
    SHAMAN = 'shaman'
    DEMON_HUNTER = 'demon_hunter'
    PRIEST = 'priest'
    WARRIOR = 'warrior'
    ROGUE = 'rogue'
    PALADIN = 'paladin'
    NEUTRAL = 'neutral'

class CanAttackResponse(Enum):
    YES = 0
    ATTACKED_ENOUGH = 1
    ASLEEP = 2
    DEFENDER_HAS_STEALTH = 3
    ZERO_ATTACK = 4
    DISOBEYS_TAUNT = 5

class Actions(Enum):
    END_TURN = 'end_turn'
    PLAY = 'play'
    ATTACK = 'attack'
    SELECT = 'select'
    HERO_POWER = 'hero_power'