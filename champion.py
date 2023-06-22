from abc import ABCMeta, abstractmethod


class Champion(metaclass=ABCMeta):
    @abstractmethod
    def get_life_points(self) -> float:
        raise NotImplemented

    @abstractmethod
    def calculate_damage(self) -> float:
        raise NotImplemented

    @abstractmethod
    def receive_damage(self, damage: float):
        raise NotImplemented
