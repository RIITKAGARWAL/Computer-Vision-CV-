import cv2 as cv

# Load an image
image = cv.imread('./image.png')

# Specify new dimensions for resizing
dimension = (640, 480)

# Resize using different interpolation methods
resized_nearest = cv.resize(image, dimension, interpolation=cv.INTER_NEAREST)
resized_bilinear = cv.resize(image, dimension, interpolation=cv.INTER_LINEAR)
resized_bicubic = cv.resize(image, dimension, interpolation=cv.INTER_CUBIC)
resized_area = cv.resize(image, dimension, interpolation=cv.INTER_AREA)
resized_lanczos = cv.resize(image, dimension, interpolation=cv.INTER_LANCZOS4)

# Save or display resized images
cv.imshow('resized_nearest.jpg', resized_nearest)
cv.imshow('resized_bilinear.jpg', resized_bilinear)
cv.imshow('resized_bicubic.jpg', resized_bicubic)
cv.imshow('resized_area.jpg', resized_area)
cv.imshow('resized_lanczos.jpg', resized_lanczos)

cv.waitKey(0)
