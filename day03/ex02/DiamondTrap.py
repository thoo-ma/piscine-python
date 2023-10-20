from S1E7 import Baratheon, Lannister


class King(Baratheon, Lannister):

    @property
    def eyes(self):
        return self._eyes

    @property
    def hair(self):
        return self._hair

    @eyes.setter
    def eyes(self, value):
        self._eyes = value

    @hair.setter
    def hair(self, value):
        self._hair = value

    def set_eyes(self, value):
        self.eyes = value

    def get_eyes(self):
        return self.eyes

    def set_hairs(self, value):
        self.hairs = value

    def get_hairs(self):
        return self.hairs
