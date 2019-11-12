import PIL
from PIL import Image
from numpy import *
from pylab import *

#Read an image and convert it to gray scale
img1=Image.open('C:/Users/Nurture-01/Desktop/download.jpg').convert('L')

#Covert the image into a numpy array
im = array(img1)

#Get the dimensions of an image
print (im.shape, im.dtype)

#Display the image
imshow(img1)
# Add title and show the plot
title('Input Image')
plt.axis('off')
show()

#function which performs Intensity Slicing
def Color_slices(img_grey, T):
    
    img_rgb = np.zeros((img_grey.shape[0],img_grey.shape[1],3),dtype='uint8')
    
    for x in range(img_grey.shape[0]):
        for y in range(img_grey.shape[1]):
            
            if img_grey[x,y]< T:
                img_rgb[x,y,2] = 255

            else:
                img_rgb[x,y,0] = 255
                img_rgb[x,y,1] = 255
                img_rgb[x,y,2] = 255
                
            img_output = PIL.Image.fromarray(img_rgb)
    return img_output
    
img_out = Color_slices(im, 150)

#Display the output image
imshow(img_out)

#Add a title and show the plot
title('Output Image')
plt.axis('off')
show()

'''r, g, b = im.split()
im = Image.merge("RGB", (b, g, r))'''
