import numpy, PIL

def img_to_2D_array(image):                     #This function converts an image file to 2D numpy array
  img = PIL.Image.open(image).convert("L")
  img_array = numpy.array(img)
  return img_array
