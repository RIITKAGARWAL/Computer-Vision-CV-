import cv2 as cv

img = cv.imread('./image.png')
cv.imshow("color",img)

blurImg = cv.GaussianBlur(img,(7,7),cv.BORDER_CONSTANT)
cv.imshow('blur',blurImg)
img = cv.resize(blurImg,(img.shape[0] // 2 , img.shape[1] // 2),interpolation= cv.INTER_AREA)
cv.imshow('gray',img)


cannyImg = cv.Canny(img,125,175)
cv.imshow('canny',cannyImg)
cv.waitKey()