import cv2 as cv

img = cv.imread('./image.png')
cv.imshow("color",img)

grayImg = cv.cvtColor(img,cv.COLOR_BGR2GRAY)
cv.imshow('gray',grayImg)

cv.waitKey()