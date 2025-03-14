import cv2 as cv
import matplotlib.pyplot as plt

import numpy as np

# read image
img = cv.imread('./image.png')
# extract dimensions
height, width = img.shape[:2]
# resize image
img = cv.resize(img, (height//2, width//4), interpolation=cv.INTER_AREA)
# display image
cv.imshow('my image', img)

# blank image
blankImg = np.zeros(img.shape[:2],dtype='uint8')
# display image
cv.imshow('blank image',blankImg)

# circle draw
circle = cv.circle(blankImg.copy(), (width // 8, height // 8), height // 5, (31, 212, 111), -1)
# display image
cv.imshow('circle image',circle)

# masking 
mask = circle
maskedImg = cv.bitwise_and(img,img,mask=mask)
# display image
cv.imshow('masked image',maskedImg)

#grayscale image
grayImg = cv.cvtColor(img,cv.COLOR_BGR2GRAY)
grayHistogram = cv.calcHist([grayImg],[0],mask,[256],[0,256])
plt.figure()
plt.title('grayscale histogram')
plt.xlabel('Bins')
plt.ylabel('Number of pixels')
plt.plot(grayHistogram)
plt.xlim([0,256])
plt.show()

# color histogram
plt.figure()
plt.title('color histogram')
plt.xlabel('bins')
plt.ylabel('# of pixels')
colors = ('b','g','r')

for i,col in enumerate(colors):
    hist = cv.calcHist([img],[i],None,[256],[0,256])
    plt.plot(hist,color=col)
    plt.xlim([0,256])
plt.show()
# wait for a key press
cv.waitKey()
# close all windows
cv.destroyAllWindows()
