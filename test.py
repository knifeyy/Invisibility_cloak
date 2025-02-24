import cv2
import numpy as np

cap = cv2.VideoCapture(0)

print("do you have a white cloak?")
print("press 's' to capture the background when ready")
print("press 'q' to quit")
background = None

while True:
    ret,frame = cap.read()
    if not ret:
        break

    frame = cv2.flip(frame,1) #mirror

    key = cv2.waitKey(1) & 0xFF
    if key == ord('s'):
        background= frame
        continue
    
    if background is not None:
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
        cv2.imshow("Invisibility Cloak", output)

    else:
        cv2.imshow("Invisibility Cloak", frame)

    if key == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()

