import cv2 as cv
import numpy as np

img = cv.imread('./image.png')
cv.imshow("color", img)

b, g, r = cv.split(img)


cv.imshow('blue', b)
cv.imshow('green', g)
cv.imshow('red', r)

print(img.shape[:])
print(b.shape[:])
print(g.shape[:])
print(r.shape[:])

blank = np.zeros(img.shape, dtype='uint8')
newImg = cv.merge([b, g, r])
blueImg = cv.merge([b, blank, blank])
greenImg = cv.merge([blank, g, blank])
redImg = cv.merge([blank, blank, r])

cv.imshow('colored img', newImg)
cv.imshow('bluee', blueImg)
cv.imshow('greenn', greenImg)
cv.imshow('redd', redImg)
cv.waitKey()
