import cv2
import numpy as np

frame=cv2.imread('opencv2.png')
frame1=cv2.imread('opencv1.jpeg')
hsv_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
hsv_frame1 = cv2.cvtColor(frame1, cv2.COLOR_BGR2HSV)

# Red color
low_red = np.array([0,100, 100])
high_red = np.array([20, 255, 255])
red_mask = cv2.inRange(hsv_frame, low_red, high_red)
red_mask1 = cv2.inRange(hsv_frame1, low_red, high_red)
red = cv2.bitwise_and(frame, frame, mask=red_mask)
red1 = cv2.bitwise_and(frame1, frame1, mask=red_mask1)
hsv_red = cv2.cvtColor(red, cv2.COLOR_BGR2HSV)
hsv_red1 = cv2.cvtColor(red1, cv2.COLOR_BGR2HSV)
black=np.array([0,0,0])
red_masking = cv2.inRange(hsv_red, black, black)
red_masking1 = cv2.inRange(hsv_red1, black, black)
red[red_masking>0]=(255,255,255)
red1[red_masking1>0]=(255,255,255)

#Blue color
low_blue = np.array([94, 80, 2])
high_blue = np.array([126, 255, 255])
blue_mask = cv2.inRange(hsv_frame, low_blue, high_blue)
blue_mask1 = cv2.inRange(hsv_frame1, low_blue, high_blue)
blue = cv2.bitwise_and(frame, frame, mask=blue_mask)
blue1 = cv2.bitwise_and(frame1, frame1, mask=blue_mask1)
hsv_blue = cv2.cvtColor(blue, cv2.COLOR_BGR2HSV)
hsv_blue1 = cv2.cvtColor(blue1, cv2.COLOR_BGR2HSV)
black=np.array([0,0,0])
blue_masking = cv2.inRange(hsv_blue, black, black)
blue_masking1 = cv2.inRange(hsv_blue1, black, black)
blue[blue_masking>0]=(255,255,255)
blue1[blue_masking1>0]=(255,255,255)

# Green color
low_green = np.array([36, 25, 25])
high_green = np.array([86, 255, 255])
green_mask = cv2.inRange(hsv_frame, low_green, high_green)
green_mask1 = cv2.inRange(hsv_frame1, low_green, high_green)
green = cv2.bitwise_and(frame, frame, mask=green_mask)
green1 = cv2.bitwise_and(frame1, frame1, mask=green_mask1)
hsv_green = cv2.cvtColor(green, cv2.COLOR_BGR2HSV)
hsv_green1 = cv2.cvtColor(green1, cv2.COLOR_BGR2HSV)
black=np.array([0,0,0])
green_masking = cv2.inRange(hsv_green, black, black)
green_masking1 = cv2.inRange(hsv_green1, black, black)
green[green_masking>0]=(255,255,255)
green1[green_masking1>0]=(255,255,255)

cv2.imwrite("Killer bees_Girija Bansal_red.jpg",red)
cv2.imwrite("Killer bees_Girija Bansal_blue.jpg",blue)
cv2.imwrite("Killer bees_Girija Bansal_green.jpg",green)
cv2.imwrite("Killer bees_Girija Bansal_red1.jpg",red1)
cv2.imwrite("Killer bees_Girija Bansal_blue1.jpg",blue1)
cv2.imwrite("Killer bees_Girija Bansal_green1.jpg",green1)


cv2.imshow("Red", red)
cv2.imshow("Blue", blue)
cv2.imshow("Green", green)
cv2.imshow("Red1", red1)
cv2.imshow("Blue1", blue1)
cv2.imshow("Green1", green1)



cv2.waitKey(0)
cv2.destroyAllWindows()