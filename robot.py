from weapon import Weapon

class Robot:
    def __init__(self, health):
        self.robot_name = 'Alloy_Cat'
        self.robot_health= health
        self.active_weapon = Weapon()
        self.battle_damage = 0
        
    def choose_weapon(self):
        self.active_weapon.weapon_name = input(f"Which attack would you like to use? {self.active_weapon.weapon_name_one}, {self.active_weapon.weapon_name_two} or {self.active_weapon.weapon_name_three}?")
        if self.active_weapon.weapon_name == self.active_weapon.weapon_name_one:
                self.battle_damage = 15
                
        elif self.active_weapon.weapon_name == self.active_weapon.weapon_name_two:
                self.battle_damage = 20
                
        elif self.active_weapon.weapon_name == self.active_weapon.weapon_name_three:
                self.battle_damage = 25
                
    
    def dino_attack(self):
        from dinosaur import Dinosaur
        dinosaur = Dinosaur(100)
        self.robot_health -= dinosaur.attack_power