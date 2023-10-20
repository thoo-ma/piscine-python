from load_image import ft_load
from pimp_image import ft_invert, ft_red, ft_green, ft_blue, ft_grey

array = ft_load("assets/landscape.jpg")

image_invert = ft_invert(array)
image_green = ft_green(array)
image_red = ft_red(array)
image_blue = ft_blue(array)
image_grey = ft_grey(array)

print(ft_invert.__doc__)
