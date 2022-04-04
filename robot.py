from weapon import Weapon

class Robot:
    def __init__(self, health):
        self.robot_name = 'Alloy_Cat'
        self.robot_health= health
        self.active_weapon = Weapon()
        self.battle_damage = self.active_weapon.weapon_power
    def robot_attack(self):
        from dinosaur import Dinosaur
        dinosaur = Dinosaur(100)
        dinosaur.dinosaur_health -= self.battle_damage