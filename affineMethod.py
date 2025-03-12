import numpy as np
import cv2 as cv

# translate an image

def translateImage(img,x,y):
    transMat = np.float32([[1,0,x],[0,1,y]])
    dimensions = (img.shape[1],img.shape[0])
    return cv.warpAffine(img,transMat,dimensions)


img = cv.imread('./image.png')
for x in range(200):
    img1 = translateImage(img,x,x)
    key = cv.waitKey(20)
    if key == ord('d'):
        break
    cv.imshow('my image window',img1)


cv.waitKey()
cv.destroyAllWindows()
