import cv2
import numpy as np

## Read an image
img = cv2.imread("img/cat.jpg")

# img_resize = cv2.resize(img, (225*3, 148*3))
img_resize = cv2.resize(img, (img.shape[1]//2, img.shape[0]//2  ))

cv2.imshow("big image",img_resize)
cv2.waitKey(0)

# print(img.shape[0]//2)