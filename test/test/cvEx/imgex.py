import cv2

#轉灰階 , opencv 預設的排列方式為BGR
# method 1
image = cv2.imread('cat.jpg')
# image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
# method 2
#image = cv2.imread('lena.jpg', cv2.IMREAD_GRAYSCALE)
cv2.imshow('Result', image)
cv2.waitKey(0)