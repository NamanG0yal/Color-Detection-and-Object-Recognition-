# Author  : Naman Goyal
import numpy as np
import cv2
img = cv2.imread("img.png",  cv2.IMREAD_COLOR)
hsv_image = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
lower_red_1 = np.array([0, 250, 200])
upper_red_1 = np.array([1, 255, 255])
lower_red_2 = np.array([178, 250, 200])
upper_red_2 = np.array([180, 255, 255])
lower_green = np.array([60, 100, 100])
upper_green = np.array([86, 255, 255])
lower_blue = np.array([118, 200, 100])
upper_blue = np.array([130, 255, 255])
red_mask1 = cv2.inRange(hsv_image , lower_red_1 , upper_red_1)
red_mask2 = cv2.inRange(hsv_image , lower_red_2 , upper_red_2)
red_mask = cv2.bitwise_or(red_mask1 , red_mask2)
green_mask = cv2.inRange(hsv_image , lower_green,upper_green)
blue_mask =  cv2.inRange(hsv_image , lower_blue , upper_blue)
cont_red , h = cv2.findContours(red_mask , cv2.RETR_EXTERNAL , cv2.CHAIN_APPROX_SIMPLE)
cont_green , h = cv2.findContours(green_mask , cv2.RETR_EXTERNAL , cv2.CHAIN_APPROX_SIMPLE)
cont_blue , h = cv2.findContours(blue_mask , cv2.RETR_EXTERNAL , cv2.CHAIN_APPROX_SIMPLE)
red_count = 0
blue_count =  0 
green_count = 0
for contour in cont_red:
    x, y, w, h = cv2.boundingRect(contour)
    cv2.rectangle(img, (x, y), (x + w, y + h), (255, 109, 255), 10)
    red_count += 1
for contour in cont_blue:
    x, y, w, h = cv2.boundingRect(contour)
    cv2.rectangle(img, (x, y), (x + w, y + h), (255, 109, 255), 10)
    blue_count +=1
for contour in cont_green:
    x, y, w, h = cv2.boundingRect(contour)
    cv2.rectangle(img, (x, y), (x + w, y + h), (255, 109, 255), 10)
    green_count += 1
print("Number of Red Balls are : " , red_count )
print("Number of Green Balls are: " , green_count)
print("Number of Blue Balls are: " , blue_count)
cv2.imshow("img" , img)
cv2.waitKey(0)
