import cv2 
import numpy as np 
from matplotlib import pyplot as plt
#variables
nrows = 2
ncols = 2

#Hellow world 
print("Hello World")

#original image
image = cv2.imread('ATU.jpg')

#greyscale image
gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

#blur image
imgOut = cv2.GaussianBlur(gray_image,(3, 3),0)

imgOut2 = cv2.GaussianBlur(gray_image,(13,13),0)


sobelHorizontal = cv2.Sobel(imgIn,cv2.CV_64F,1,0,ksize=5)  # x dir 
sobelVertical   = cv2.Sobel(imgIn,cv2.CV_64F,0,1,ksize=5)  # y dir 

#loading image
# cv2.imshow('Grayscale', gray_image)
# cv2.waitKey(0)  
# cv2.destroyAllWindows()

#plotting images
plt.subplot(nrows, ncols,1),plt.imshow(image, cmap = 'gray') 
plt.title('Original'), plt.xticks([]), plt.yticks([]) 

plt.subplot(nrows, ncols,2),plt.imshow(gray_image, cmap = 'gray') 
plt.title('GrayScale'), plt.xticks([]), plt.yticks([])

plt.subplot(nrows, ncols,3),plt.imshow(imgOut, cmap = 'gray') 
plt.title('3x3 blur'), plt.xticks([]), plt.yticks([]) 

plt.subplot(nrows, ncols,4),plt.imshow(imgOut2, cmap = 'gray') 
plt.title('13x13 blur'), plt.xticks([]), plt.yticks([]) 

plt.show()
