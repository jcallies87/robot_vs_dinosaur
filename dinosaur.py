from robot import Robot
class Dinosaur:
    def __init__(self):
        self.dinosaur_name = "Rex"
        self.attack_power = 20
        self.dinosaur_health = 100

    def dino_attack(self , robot):
        robot = Robot
        robot.robot_health -= self.attack_power