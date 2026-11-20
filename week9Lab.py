import cv2 
import numpy as np 
from matplotlib import pyplot as plt
#variables
nrows = 2
ncols = 3

#Hellow world 
print("Hello World")

#original image
image = cv2.imread('ATU.jpg')

#greyscale image
gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

#blur image
imgOut = cv2.GaussianBlur(gray_image,(3, 3),0)

imgOut2 = cv2.GaussianBlur(gray_image,(13,13),0)


sobelHorizontal = cv2.Sobel(image,cv2.CV_64F,1,0,ksize=5)  # x dir 
sobelVertical   = cv2.Sobel(image,cv2.CV_64F,0,1,ksize=5)  # y dir 

canny = cv2.Canny(image,150,300) 
sobelSum = cv2.addWeighted(sobelHorizontal,0.5,sobelVertical,0.5,0)

#loading image
# cv2.imshow('Grayscale', gray_image)
# cv2.waitKey(0)  
# cv2.destroyAllWindows()

#plotting images
plt.subplot(nrows, ncols,1),plt.imshow(image, cmap = 'gray') 
plt.title('Original'), plt.xticks([]), plt.yticks([]) 

plt.subplot(nrows, ncols,2),plt.imshow(gray_image, cmap = 'gray') 
plt.title('GrayScale'), plt.xticks([]), plt.yticks([])

plt.subplot(nrows, ncols,3),plt.imshow(sobelHorizontal, cmap = 'gray') 
plt.title('Sobel X'), plt.xticks([]), plt.yticks([]) 

plt.subplot(nrows, ncols,4),plt.imshow(sobelVertical, cmap = 'gray') 
plt.title('Sobel Y'), plt.xticks([]), plt.yticks([]) 

plt.subplot(nrows, ncols,5),plt.imshow(sobelSum, cmap = 'gray') 
plt.title('Sobel Sum'), plt.xticks([]), plt.yticks([]) 

plt.subplot(nrows, ncols,6),plt.imshow(canny, cmap = 'gray') 
plt.title('Canny Edge Image'), plt.xticks([]), plt.yticks([]) 

plt.show()
