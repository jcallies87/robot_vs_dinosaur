from robot import Robot
from dinosaur import Dinosaur

class Battlefield:
    def __init__(self):
        self.dino = Dinosaur
        self.robot = Robot
        self.dino_lost = False
        self.robot_lost = False

    def run_game(self):
        self.display_welcome()
        self.battle_phase()
        self.display_winner()
        
    def display_welcome(self):
        print("Welcome to Robot vs Dinosaur")

    def battle_phase(self):
        dino_hit = Dinosaur
        robot_hit = Robot
        while:
            if dino_hit >= 0:
                dino_hit.dino_attack
                print(f" {self.robot.robot_name} has sustained {self.dino.attack_power} damage points.{self.robot.robot_name} has {self.robot.robot_health} damage points left.")
                continue
            elif robot_hit >= 0:
                robot_hit.robot_attack
                print(f" {self.dino.dinosaur_name} has sustained {self.robot.battle_damage} damage points.{self.dino.dinosaur_name} has {self.dino.dinosaur_health} damage points left.")
                continue
            elif dino_hit <= 0:
                return self.dino_lost = True
            elif robot_hit <= 0:
                return self.robot_lost = True


    def display_winner(self):
        if self.dino_lost == True:
            print(f"{self.robot.robot_name} has won.")
        elif self.robot_lost == True:
            print(f"{self.dino.dinosaur_name} has won.")