from hearthsim.conditions.core import Condition
from hearthsim.utils.enums import Events


class WhileWeaponEquipped(Condition):
    _events_received = (Events.WEAPON_EQUIPPED.value,
                        Events.WEAPON_DESTROYED.value)

    def evaluate(self, game, em_node):
        player = em_node.affected_slot.player
        return game.weapons[player] is not None


class WhileSelfDamaged(Condition):
    _events_received = (Events.AFTER_COMBAT_DAMAGE.value,)

    def evaluate(self, game, em_node):
        slot = em_node.affected_slot
        return slot.health < slot.max_health