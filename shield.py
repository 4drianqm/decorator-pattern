from item import Item


class Shield(Item):
    def receive_damage(self, damage: float):
        self.champion.receive_damage(damage / 2)
