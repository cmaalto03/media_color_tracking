# import required libraries

#code from https://www.tutorialspoint.com/how-to-find-the-hsv-values-of-a-color-using-opencv-python

import numpy as np
import cv2
# define a numpy.ndarray for the color
# bgr 
color = np.uint8([[[0, 0, 255]]])

# convert the color to HSV
hsvColor = cv2.cvtColor(color, cv2.COLOR_BGR2HSV)

# display the color values
print("BGR of color:", color)
print("HSV of color:", hsvColor)

# Compute the lower and upper limits
lowerLimit = hsvColor[0][0][0] - 10, 100, 100
upperLimit = hsvColor[0][0][0] + 10, 255, 255

# display the lower and upper limits
print("Lower Limit:",lowerLimit)
print("Upper Limit", upperLimit)

