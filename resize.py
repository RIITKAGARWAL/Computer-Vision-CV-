import cv2 as cv
def resizeImage(frame,scale = 0.75):
    height = int(frame.shape[0] * scale)
    width = int(frame.shape[1] * scale)

    dimension = (height,width)

    return cv.resize(frame,dimension,interpolation = cv.INTER_AREA)

def resolution(width,height):
    capture.set(3,width)
    capture.set(4,height)
  #  capture.set(10,brightness)

frame = cv.imread('./image.png')
img = resizeImage(frame,0.2)
cv.imshow('big image',frame)
cv.imshow('small image',img)

capture = cv.VideoCapture('./video.mp4')

cv.waitKey(0)