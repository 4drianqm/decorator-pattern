from abc import ABCMeta, abstractmethod
from component import Component


class PowerUp(metaclass=ABCMeta, Component):
    def __init__(self, component: Component):
        self.component = component

    def calculate_damage(self) -> float:
        return self.component.calculate_damage()
