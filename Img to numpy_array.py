import numpy as np
from PIL import Image


img = Image.open(r"image directory or loaction")
try:
    image = np.asarray(img)
except SystemError:
    image = np.asarray(img.getdata())
