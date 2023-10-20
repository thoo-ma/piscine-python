from abc import ABC, abstractmethod


class Character(ABC):

    def __init__(self, first_name, is_alive=True):
        self.first_name = first_name
        self.is_alive = is_alive

    @abstractmethod
    def die(self):
        pass


class Stark(Character):

    def die(self):
        self.is_alive = False
