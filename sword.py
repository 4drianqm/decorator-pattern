from item import Item


class Sword(Item):
    def calculate_damage(self) -> float:
        return super().calculate_damage() + 10
