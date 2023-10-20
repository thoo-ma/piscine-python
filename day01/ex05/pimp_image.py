import numpy as np
import PIL


def ft_invert(array) -> None:
    _array = np.copy(array)
    _array[...] = 255 - _array[...]
    PIL.Image.fromarray(_array).save('assets/landscape_invert.jpeg')


def ft_red(array) -> None:
    _array = np.copy(array)
    _array[..., (1, 2)] = 0
    PIL.Image.fromarray(_array).save('assets/landscape_red.jpeg')


def ft_green(array) -> None:
    _array = np.copy(array)
    _array[..., (0, 2)] = 0
    PIL.Image.fromarray(_array).save('assets/landscape_green.jpeg')


def ft_blue(array) -> None:
    _array = np.copy(array)
    _array[..., (0, 1)] = 0
    PIL.Image.fromarray(_array).save('assets/landscape_blue.jpeg')


def ft_grey(array) -> None:
    _array = np.dot(array, [0.2989, 0.5870, 0.1140])
    PIL.Image.fromarray(_array).convert('L').save('assets/landscape_grey.jpeg')
