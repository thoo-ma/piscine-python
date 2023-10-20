class calculator:

    @staticmethod
    def dotproduct(v1: list[float], v2: list[float]) -> None:
        print('Dot product is:', sum([x * y for x, y in zip(v1, v2)]))

    @staticmethod
    def add_vec(v1: list[float], v2: list[float]) -> None:
        print('Add vector is:', [float(x + y) for x, y in zip(v1, v2)])

    @staticmethod
    def sous_vec(v1: list[float], v2: list[float]) -> None:
        print('Sous vector is:', [float(x - y) for x, y in zip(v1, v2)])
