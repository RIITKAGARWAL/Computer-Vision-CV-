import cv2 as cv

img = cv.imread('./image.png')
cv.imshow("color",img)

#resize the image
img = cv.resize(img,(img.shape[0] // 2 , img.shape[1] // 2),interpolation= cv.INTER_AREA)

#average blur
averageBlur = cv.blur(img,(3,3))
cv.imshow('average blur',averageBlur)

#gaussian Blur
blurImg = cv.GaussianBlur(img,(7,7),cv.BORDER_CONSTANT)
cv.imshow('gauss blur',blurImg)

#median Blur
medianImage = cv.medianBlur(img,3)
cv.imshow('median blur',medianImage)

#bilateral Blur
bilateralImage = cv.bilateralFilter(img,5,15,15)
cv.imshow('bilateral blur',bilateralImage)

cv.waitKey()