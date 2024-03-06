import numpy as np
import cv2
vid = cv2.VideoCapture(0)
while (True):

    ret, frame = vid.read()
    cv2.imshow('frame', frame)
    colorDetect = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    red_lower = np.array([0, 100, 100], dtype="uint8")
    red_higher = np.array([30, 255, 255], dtype="uint8")
    yellow_lower = np.array([31, 100, 100], dtype="uint8")
    yellow_higher = np.array([60, 255, 255], dtype="uint8")
    green_lower = np.array([61, 100, 100], dtype="uint8")
    green_higher = np.array([90, 255, 255], dtype="uint8")
    cyan_lower = np.array([91, 100, 100], dtype="uint8")
    cyan_higher = np.array([120, 255, 255], dtype="uint8")
    blue_lower = np.array([121, 100, 100], dtype="uint8")
    blue_higher = np.array([150, 255, 255], dtype="uint8")
    magenta_lower = np.array([151, 100, 100], dtype="uint8")
    magenta_higher = np.array([179, 255, 255], dtype="uint8")
    white_lower = np.array([0, 0, 100], dtype="uint8")
    white_higher = np.array([0, 0, 255], dtype="uint8")
    red = cv2.inRange(colorDetect, red_lower, red_higher)
    if (cv2.countNonZero(red) > 10):
        gray_image = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        # convert the grayscale image to binary imageret
        ret, thresh = cv2.threshold(gray_image, 127, 255, 0)
        # calculate moments of binary image
        M = cv2.moments(thresh)
        # calculate x,y coordinate of center
        cX = int(M["m10"] / M["m00"])
        cY = int(M["m01"] / M["m00"])
        print(cX, cY)
