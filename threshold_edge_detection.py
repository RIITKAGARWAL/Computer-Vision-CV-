import cv2 as cv
import numpy as np

img = cv.imread('./image.png')
img = cv.resize(img,(img.shape[0] // 2 , img.shape[1] //4),interpolation= cv.INTER_AREA)

cv.imshow("color",img)

grayImg = cv.cvtColor(img,cv.COLOR_BGR2GRAY)
cv.imshow('gray',grayImg)


threshold, thresh = cv.threshold(grayImg,150,255,cv.THRESH_BINARY)
cv.imshow('simple threshhold image',thresh)

threshold, thresh = cv.threshold(grayImg,175,255,cv.THRESH_BINARY_INV)
cv.imshow('simple threshhold image inverse',thresh)

thresh = cv.adaptiveThreshold(grayImg,255,cv.ADAPTIVE_THRESH_MEAN_C,cv.THRESH_BINARY,11,3)
cv.imshow('simple threshhold mean image inverse',thresh)

thresh = cv.adaptiveThreshold(grayImg,255,cv.ADAPTIVE_THRESH_GAUSSIAN_C,cv.THRESH_BINARY,11,3)
cv.imshow('simple threshhold gauss image inverse',thresh)


#laplacian method
lap = cv.Laplacian(grayImg,cv.CV_64F)
lap= np.uint8(np.absolute(lap))

cv.imshow('laplacian',lap)

#sobel method
sobelx = cv.Sobel(grayImg,cv.CV_64F,1,0)
sobely = cv.Sobel(grayImg,cv.CV_64F,0,1)
combined_sobel = cv.bitwise_or(sobelx,sobely)

cv.imshow('sobelx ',sobelx)
cv.imshow('sobely ',sobely)
cv.imshow('combined img',combined_sobel)



cv.waitKey()