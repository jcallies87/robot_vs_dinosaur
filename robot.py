from weapon import Weapon
from dinosaur import Dinosaur
class Robot:
    def __init__(self):
        self.robot_name = 'Alloy_Cat'
        self.robot_health= 100
        self.active_weapon = Weapon

    def robot_attack(self, dinosaur):
        dinosaur = Dinosaur
        dinosaur.dinosaur_health -= (self.active_weapon.weapon_power)