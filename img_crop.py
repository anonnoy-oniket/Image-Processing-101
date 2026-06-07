import cv2
import numpy as np

## Read an image
img = cv2.imread("img/cat.jpg")

img_crop = img[10:120, 50:200]

cv2.imshow("window", img_crop)
cv2.waitKey(0)

print(img_crop.shape)