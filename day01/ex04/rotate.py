import load_image
import matplotlib.pyplot as plt
import numpy as np


def main():
    array = load_image.ft_load('assets/animal.jpeg')

    print("The shape of image is:", array.shape)
    print(array)

    array = array[200:600, 400:800]
    array = np.dot(array, [0.2989, 0.5870, 0.1140])

    _array = np.zeros((array.shape[1], array.shape[0]))
    for i in range(array.shape[1]):
        _array[i] = array[:, i]

    print("New shape after Transpose:", _array.shape)
    print(_array)

    plt.imshow(_array, cmap=plt.get_cmap('gray'))
    plt.show()


if __name__ == "__main__":
    main()
