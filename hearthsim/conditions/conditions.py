class WhileWeaponEquipped(Condition):
    _events_received = (Events.weapon_equipped.value,
                        Events.weapon_destroyed.value)

    def evaluate(self, game, em_node):
        player = em_node.affected_slot.player
        return game.weapons[player] is not None

class WhileSelfDamaged(Condition):
    _events_received = (Events.after_combat_damage.value,)

    def evaluate(self, game, em_node):
        slot = em_node.affected_slot
        return slot.health < slot.max_health