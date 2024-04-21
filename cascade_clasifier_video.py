

# import required libraries
import cv2
haar_cascade="haarcascade_fullbody.xml"
car_cascade = cv2.CascadeClassifier(haar_cascade)


video = 'firsttake.mp4'
cap = cv2.VideoCapture(video)
# Reading the Image
while(True):
ret, frames = cap.read()
# convert to gray scale of each frames
gray = cv2.cvtColor(frames, cv2.COLOR_BGR2GRAY)
cars = car_cascade.detectMultiScale(gray, 1.1, 1);
for (x,y,w,h) in cars:
cv2.rectangle(frames,(x,y),(x+w,y+h),(0,0,255),2)


cv2.imshow('video', frames)
if cv2.waitKey(33) == 27:
break




# display the output image


cv2.destroyAllWindows()
