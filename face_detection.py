import cv2 as cv

img = cv.imread('./picture.jpg')
img = cv.resize(img,(img.shape[0] // 2 , img.shape[1] //4),interpolation= cv.INTER_AREA)

cv.imshow("color",img)

grayImg = cv.cvtColor(img,cv.COLOR_BGR2GRAY)
cv.imshow('gray',grayImg)

# call xml file
haar_cascade = cv.CascadeClassifier('./haar_face.xml')
faces_rect = haar_cascade.detectMultiScale(grayImg,1.1,6)
print(f'number of faces found: {len(faces_rect)}')
for(x,y,w,h) in faces_rect:
    cv.rectangle(img,(x,y),(x+w,y+h),(0,255,0),thickness=2)
cv.imshow('detected faces',img)

cv.waitKey()
cv.destroyAllWindows()