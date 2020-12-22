import cv2
import numpy as np
cap=cv2.VideoCapture(1)
while True:
 ret,img=cap.read()
 hsv_frame = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
 low_yellow = np.array([20, 100, 100])
 high_yellow = np.array([35, 255, 255])
 yellow_mask = cv2.inRange(hsv_frame, low_yellow, high_yellow)
 yellow = cv2.bitwise_and(img, img, mask=yellow_mask)
 contours, _ = cv2.findContours(yellow_mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
 for c in contours:
        approx = cv2.approxPolyDP(c, 0.02 * cv2.arcLength(c, True), True)
        if len(approx)==3:
            cv2.drawContours(yellow, [approx], 0, (0, 255, 0), 10)
        else:
            cv2.drawContours(yellow, [approx], 0, (0, 0, 0), -1)
            cv2.drawContours(yellow, [approx], 0, (0, 0, 0), 4)
 cv2.imshow("yellow",yellow)
 if cv2.waitKey(1)==27:
     break
cap.release()
cv2.destroyAllWindows()
