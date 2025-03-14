import cv2 as cv
import numpy as np

img = cv.imread('./image.png')
(height, width) = img.shape[:2]

img = cv.resize(img, (height//2, width//4), interpolation=cv.INTER_AREA)
cv.imshow('my image', img)

# grayscale
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('gray Image', gray)
# binary image (black & white)
ret, binaryImage = cv.threshold(gray, 126, 255, cv.THRESH_BINARY)


# find contour
contour, hierarchy = cv.findContours(
    binaryImage, cv.RETR_LIST, cv.CHAIN_APPROX_NONE)
print(len(contour))

# draw contour on black image
blank = np.zeros(img.shape, dtype='uint8')
cv.drawContours(blank, contour, -1, (0, 255, 0), 2)
cv.imshow('binary image', blank)

cv.waitKey()
cv.destroyAllWindows()
