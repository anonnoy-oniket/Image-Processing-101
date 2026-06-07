import cv2
import numpy as np

## Read an image
img = cv2.imread("img/cat.jpg")

# print(img.shape)  # it has 3 channels B, G and R
# img[:, :, 0] = 0 # Remove Blue or set it to 0 
# cv2.imshow("Cat", img)
# cv2.waitKey(0)  #this means infinite delay


## Convert the rgb image in gray
# img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
# cv2.imshow("Gray Cat", img_gray)
# cv2.waitKey(0)
# print(img_gray.shape) # Only one channel now



# separating 3 components
imgBlue = img[:, :, 0]
imgGreen = img[:,:,1]
imgRed = img[:,:,2]

new_img = np.hstack((imgBlue, imgGreen, imgRed))
cv2.imshow("new image",new_img)
cv2.waitKey(0)

print(new_img.shape) # this is now a 2D array
