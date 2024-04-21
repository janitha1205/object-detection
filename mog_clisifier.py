

# import required libraries
import cv2
import numpy as np
# convert to gray scale of each frames
hog = cv2.HOGDescriptor()
hog.setSVMDetector(cv2.HOGDescriptor_getDefaultPeopleDetector())


video = 'car_detec2.mp4'
cap = cv2.VideoCapture(video)
kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (3, 3))
fgbg =cv2.createBackgroundSubtractorMOG2()
# Reading the Image
while(True):
ret, frames = cap.read()
fgmask = fgbg.apply(frames)
fgmask = cv2.morphologyEx(fgmask, cv2.MORPH_OPEN, kernel)
contours, hierarchy = cv2.findContours(fgmask,
cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
cv2.drawContours(frames, contours, -1, (0, 255, 0), 3)
cv2.imshow('video', frames)
if cv2.waitKey(33) == 27:
break
""" (humans, _) = hog.detectMultiScale(frames2, winStride=(8, 8),
padding=(32, 32), scale=1.1)
print('Human Detected : ', len(humans))
for (x, y, w, h) in humans:
pad_w, pad_h = int(0.15 * w), int(0.01 * h)
cv2.rectangle(frames, (x + pad_w, y + pad_h), (x + w - pad_w, y + h - pad_h), (0, 255, 0), 2) """










# display the output image


cv2.destroyAllWindows()
