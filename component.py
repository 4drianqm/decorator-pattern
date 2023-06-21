from abc import ABCMeta, abstractmethod


class Component(metaclass=ABCMeta):
    @abstractmethod
    def calculate_damage(self) -> float:
        raise NotImplemented
