from S1E9 import Character


class Baratheon(Character):

    def __init__(self, first_name, is_alive=True):
        self.first_name = first_name
        self.is_alive = is_alive
        self.family_name = 'Barateon'
        self._eyes = 'brown'
        self._hairs = 'dark'

    def __repr__(self):
        return f"Vector: ('{self.family_name}', '{self.eyes}', '{self.hairs}')"

    def __str__(self):
        return self.__repr__()

    def die(self):
        self.is_alive = False


class Lannister(Character):

    def __init__(self, first_name, is_alive=True):
        self.first_name = first_name
        self.is_alive = is_alive
        self.family_name = 'Lannister'
        self._eyes = 'blue'
        self._hairs = 'light'

    def __repr__(self):
        return f"Vector: ('{self.family_name}', '{self.eyes}', '{self.hairs}')"

    def __str__(self):
        return self.__repr__()

    def die(self):
        self.is_alive = False

    @classmethod
    def create_lannister(cls, first_name, is_alive=True):
        return cls(first_name, is_alive)
