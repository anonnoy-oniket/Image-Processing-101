import cv2
import numpy as np

## Read an image
img = cv2.imread("img/cat.jpg")

img_flip = cv2.flip(img, -1) #possible values -1, 0, 1

cv2.imshow("window", img_flip)
cv2.waitKey(0)