from PIL import Image
import numpy as np


def ft_load(path: str) -> np.array:
    image = Image.open(path, formats=['JPEG'])
    print("Image format:", image.format)
    if image.mode != "RGB":
        image = image.convert("RGB")
    array = np.array(image)
    print("Image shape:", array.shape)
    return array
