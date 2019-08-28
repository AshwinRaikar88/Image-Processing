import numpy, PIL
from skimage import io, filters

def img_to_2D_array(image):                     # This function converts an image file to 2D numpy array
  img = PIL.Image.open(image).convert("L")
  img_array = numpy.array(img)
  return img_array


imgarr = img_to_2D_array(r"Your file name")     # Always specify file name in this format
                                                # e.g: r"C:\Users\username\Desktop\website.jpg"

edges = filters.sobel(imgarr)                   # Filter function to detect edges
io.imshow(edges)
io.show()
