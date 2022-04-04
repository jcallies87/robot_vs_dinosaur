
class Dinosaur:
    def __init__(self, health):
        self.dinosaur_name = "Rex"
        self.attack_power = 20
        self.dinosaur_health = health

    def dino_attack(self):
        from robot import Robot
        robot = Robot(100)
        robot.robot_health -= self.attack_power
        