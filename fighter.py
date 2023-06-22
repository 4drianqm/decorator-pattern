from champion import Champion


class Fighter(Champion):
    def __init__(self):
        self.life_points = 100
        self.attack = 50
        self.defense = 38

    def get_life_points(self) -> float:
        return self.life_points

    def calculate_damage(self) -> float:
        return self.attack

    def receive_damage(self, damage: float):
        self.life_points -= max(0.0, damage * (1/self.defense))
