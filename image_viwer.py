from skimage import io, color
import numpy as np
import matplotlib.pyplot as plt
from skimage import exposure
from skimage.filters import threshold_otsu

from convolution import convo as convolve

img = io.imread('data.jpg')    # Load the image
img = color.rgb2gray(img)

kernel = np.array([[-1,-1,-1], [-1,8,-1], [-1,-1,-1]])
thresh = threshold_otsu(img)
binary = img > thresh
edges = convolve(binary,kernel)

plt.imshow(edges, cmap=plt.cm.gray)
plt.axis('off')
plt.show()
