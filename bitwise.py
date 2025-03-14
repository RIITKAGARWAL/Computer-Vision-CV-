import cv2 as cv
import numpy as np

img = cv.imread('./image.png')
cv.imshow("color",img)

blank = np.zeros((500,500),'uint8')

#rectangle
rect = cv.rectangle(blank.copy(),(30,30),(480,480),255,-1)
cv.imshow('rectangle',rect)
#circle
cir = cv.circle(blank.copy(),(250,250),250,255,-1)
cv.imshow('CIRCLE  ',cir)

#bitwise and
andImg = cv.bitwise_and(rect,cir)
cv.imshow('andImg',andImg)

#bitwise or
orImg = cv.bitwise_or(rect,cir)
cv.imshow('orImg',orImg)

#bitwise xor
xorImg = cv.bitwise_xor(rect,cir)
cv.imshow('xorImg',xorImg)

#bitwise not
notImg = cv.bitwise_not(rect)
cv.imshow('notImg',notImg)

#bitwise and
andImg = cv.bitwise_and(rect,cir)
cv.imshow('andImg',andImg)

cv.waitKey()
cv.destroyAllWindows()