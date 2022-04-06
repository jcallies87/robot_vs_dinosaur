class Battlefield:
    def __init__(self):
        from robot import Robot
        from dinosaur import Dinosaur
        self.dino = Dinosaur(100)
        self.robot = Robot(100)

    def run_game(self):
        self.display_welcome()
        
        self.battle_phase()
        self.display_winner()
        
    def display_welcome(self):
        print("Welcome to Robot vs Dinosaur. This game has two characters a robot cat named 'Alloy Cat' and a T-Rex named 'Rex'.")

    def battle_phase(self):
        epic_battle = (self.dino.dinosaur_health >= 0) or (self.robot.robot_health >= 0)
        while epic_battle:
            if (self.dino.dinosaur_health >= 0) or (self.robot.robot_health >= 0):
                self.robot.dino_attack()
                if self.robot.robot_health >= 1 and self.dino.dinosaur_health >= 1:
                    print(f" {self.robot.robot_name} has sustained {self.dino.attack_power} damage points.{self.robot.robot_name} has {self.robot.robot_health} damage points left.")
                elif self.robot.robot_health <= 1:
                    robot_lost = (f"{self.robot.robot_name} has sustained {self.dino.attack_power} damage points.{self.robot.robot_name} has 0 damage points left.{self.dino.dinosaur_name} is the winner!")
                    return robot_lost
                self.dino.robot_attack()
                if self.dino.dinosaur_health >= 1 and self.robot.robot_health >= 1:
                    print(f" {self.dino.dinosaur_name} has sustained {self.dino.dinosaur_damage} damage points.{self.dino.dinosaur_name} has {self.dino.dinosaur_health} damage points left.")
                elif self.dino.dinosaur_health <= 1:
                    dino_lost = (f" {self.dino.dinosaur_name} has sustained {self.dino.dinosaur_damage} damage points.{self.dino.dinosaur_name} has 0 damage points left.{self.robot.robot_name} is the winner!")
                    return dino_lost
                continue

    def display_winner(self):
        print(self.battle_phase())