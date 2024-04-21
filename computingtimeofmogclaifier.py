
from numba import jit, cuda
import cv2
import numpy as np
import time
#from google.colab.patches import cv2_imshow
# to measure exec time








# function optimized to run on gpu
from numba import jit, cuda
@jit(target_backend="cuda")
def task(frames,kernel,fgbg):
fgmask = fgbg.apply(frames)
fgmask = cv2.morphologyEx(fgmask, cv2.MORPH_OPEN, kernel)
contours, hierarchy = cv2.findContours(fgmask,cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)


# cv2.drawContours(frames, contours, -1, (0, 255, 0), 3)
areas=[]
for c in contours:
are=cv2.contourArea(c)
if are>200:
areas.append(c)
#rint(c)


(x,y,w,h) = cv2.boundingRect(c)
if w > 10 and h > 10:
cv2.rectangle(frames, (x,y), (x+w,y+h), (255, 0, 0), 2)
cv2.drawContours(frames, areas, -1, (0, 255, 0), 3)
#print(areas)
return frames
if __name__=="__main__":
hog = cv2.HOGDescriptor()
hog.setSVMDetector(cv2.HOGDescriptor_getDefaultPeopleDetector())




video = 'car_detec2.mp4'
cap = cv2.VideoCapture(video)
kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (3, 3))
fgbg =cv2.createBackgroundSubtractorMOG2()
# Reading the Image
while(True):
tic = time.perf_counter()


ret, frames = cap.read()
if ret!=False:
img=task(frames,kernel,fgbg)
cv2.imshow('vedio',img)
toc = time.perf_counter()
res= toc-tic
print(res)
if cv2.waitKey(33) == 27:
break


cv2.destroyAllWindows()
