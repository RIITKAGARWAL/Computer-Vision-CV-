import cv2 as cv
import numpy as np

img = np.zeros((500,500),dtype = 'uint8')
cv.imshow('d',img)

img1 = np.zeros((500,500,3),dtype = 'uint8')
# Get the dimensions of the image
height, width = img1.shape[:2]

# Calculate the center position for the text
position = (width // 2, height // 2)

text = "hwllo world"
# Add the text to the image
cv.putText(img1, text, position, cv.FONT_HERSHEY_TRIPLEX, 1, (0, 255, 0), thickness=1)
           
cv.imshow('e',img1)

cv.waitKey()