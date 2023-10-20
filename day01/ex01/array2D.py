import numpy as np


def slice_me(family: list, start: int, end: int) -> list:
    if not isinstance(family, list):
        raise TypeError('family should be a list')

    if not all(len(array) == len(family[0]) for array in family):
        raise ValueError('family elements should all have the same size')

    if len(family[0]) == 0:
        raise ValueError('family elements should not be empty')

    old = np.array(family)
    new = old[start:end]

    print("My shape is:", old.shape)
    print("My new shape is:", new.shape)

    return new
