import random

from champion import Champion


class Wizard(Champion):
    def __init__(self):
        self.life_points = 300
        self.attack = 5
        self.defense = 100

    def calculate_damage(self) -> float:
        return self.attack

    def receive_damage(self, damage: float):
        random_number = random.randint(1, 100)
        if random_number > 50:
            self.life_points -= max(0.0, damage * (1/self.defense))

    def get_life_points(self) -> float:
        return self.life_points
