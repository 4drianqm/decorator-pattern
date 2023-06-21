from power_up import PowerUp


class Sword(PowerUp):
    def calculate_damage(self) -> float:
        return super().calculate_damage() + 10
