
class Dinosaur:
    def __init__(self,health):
        self.dinosaur_name = "Rex"
        self.attack_power = 20
        self.dinosaur_health = health
        self.dinosaur_damage = 0

    def robot_attack(self):
        from robot import Robot
        robot = Robot(100)
        robot.choose_weapon()
        self.dinosaur_health -= robot.battle_damage
        self.dinosaur_damage = robot.battle_damage
        