import cv2
import numpy as np

def process_frame(frame, background):

    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
 
    lower_white = np.array([0,0, 200])
    upper_white = np.array([180,50,255])

    mask = cv2.inRange(hsv, lower_white, upper_white)

    mask = cv2.morphologyEx(mask, cv2.MORPH_OPEN, np.ones((3,3), np.uint8))
    mask = cv2.morphologyEx(mask, cv2.MORPH_DILATE, np.ones((3,3), np.uint8))

    mask_inv = cv2.bitwise_not(mask)

    cloak = cv2.bitwise_and(background, background, mask=mask)

    non_cloak = cv2.bitwise_and(frame, frame, mask=mask_inv)

    output = cv2.addWeighted(cloak, 1, non_cloak, 1, 0)
    
    return output




