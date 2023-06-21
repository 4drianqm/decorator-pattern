from component import Component


class Fighter(Component):
    def __init__(self):
        self.life_points = 100
        self.attack = 50
        self.defense = 38

    def calculate_damage(self) -> float:
        return self.attack
