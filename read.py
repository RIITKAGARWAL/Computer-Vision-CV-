import cv2 as cv

#picture reading
img = cv.imread('./image.png')
cv.imshow('myImage',img)

cv.waitKey(0)

# video reading
capture = cv.VideoCapture('./video.mp4')
while True:
    isTrue,frame = capture.read()
    cv.imshow('video',frame)

    if cv.waitKey(20) & 0xff == ord('d'):
        break

capture.release()
cv.destroyAllWindows()
