import matplotlib.pyplot as plt
import pandas as pd
import mglearn
from PIL import Image
from pylab import *
from numpy import *


img_path = '/home/charlie/Pictures/ubuntu.jpeg'

image = array(Image.open(img_path).convert('L'),'f')
print(image.shape,image.dtype)

image = array(Image.open(img_path))
print(image.shape,image.dtype)

imshow(image)

# pixel opposition
image1 = 255 - image
# restrict pixel value in range(100,200)
image2 = (100 / 255.0) * image + 100
# return the square of pixel value
# increase the contrast
image3 = 255.0 * (image / 255.0) ** 2

imshow(image1)
imshow(image2)
imshow(image3)
