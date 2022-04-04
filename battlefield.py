

class Battlefield:
    def __init__(self):
        from robot import Robot
        from dinosaur import Dinosaur
        self.dino = Dinosaur(100)
        self.robot = Robot(100)
        self.dino_lost = False
        self.robot_lost = False

    def run_game(self):
        self.display_welcome()
        self.battle_phase()
        self.display_winner()
        
    def display_welcome(self):
        print("Welcome to Robot vs Dinosaur")

    def battle_phase(self):
        epic_battle = self.dino.dinosaur_health >= 0 or self.robot.robot_health >= 0
        while epic_battle:
            if self.dino.dinosaur_health >= 0 or self.robot.robot_health >= 0:
                self.dino.dino_attack()
                self.robot.robot_health >= 0
                print(f" {self.robot.robot_name} has sustained {self.dino.attack_power} damage points.{self.robot.robot_name} has {self.robot.robot_health} damage points left.")
                
                self.robot.robot_attack()
                print(f" {self.dino.dinosaur_name} has sustained {self.robot.battle_damage} damage points.{self.dino.dinosaur_name} has {self.dino.dinosaur_health} damage points left.")
                continue
            elif self.dino.dinosaur_health <= 0:
                return self.dino_lost == True
            elif self.robot.robot_health <= 0:
                return self.robot_lost == True


    def display_winner(self):
        if self.dino_lost == True:
            print(f"{self.robot.robot_name} has won.")
        elif self.robot_lost == True:
            print(f"{self.dino.dinosaur_name} has won.")