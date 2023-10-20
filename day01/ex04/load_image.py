from PIL import Image
import numpy as np


def ft_load(path: str) -> np.array:
    image = Image.open(path, formats=['JPEG'])
    if image.mode != "RGB":
        image = image.convert("RGB")
    return np.array(image)
