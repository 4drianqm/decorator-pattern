from champion import Champion


class Item(Champion):
    def get_life_points(self) -> float:
        return self.champion.get_life_points()

    def __init__(self, champion: Champion):
        self.champion = champion

    def receive_damage(self, damage: float):
        self.champion.receive_damage(damage)

    def calculate_damage(self) -> float:
        return self.champion.calculate_damage()
