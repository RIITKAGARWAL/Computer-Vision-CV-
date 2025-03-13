import cv2 as cv

img = cv.imread('./image.png')
img = cv.resize(img,(img.shape[0]//2,img.shape[1]//4),interpolation=cv.INTER_AREA)
cv.imshow("color",img)

grayImg = cv.cvtColor(img,cv.COLOR_BGR2GRAY)
cv.imshow('gray',grayImg)

grayImg = cv.cvtColor(img,cv.COLOR_BGR2HSV)
cv.imshow('HSV',grayImg)

grayImg = cv.cvtColor(img,cv.COLOR_BGR2RGB)
cv.imshow('RGB',grayImg)

grayImg = cv.cvtColor(img,cv.COLOR_BGR2LAB)
cv.imshow('LAB',grayImg)

cv.waitKey()