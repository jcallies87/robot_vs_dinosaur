
class Dinosaur:
    def __init__(self,health):
        self.dinosaur_name = "Rex"
        self.attack_power = 15
        self.dinosaur_health = health

    def robot_attack(self):
        from robot import Robot
        robot = Robot(100)
        self.dinosaur_health -= robot.battle_damage
        