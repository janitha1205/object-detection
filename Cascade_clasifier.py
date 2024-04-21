

# import required libraries
import cv2
haar_cascade="haarcascade_fullbody.xml"
car_cascade = cv2.CascadeClassifier(haar_cascade)




# Reading the Image
image = cv2.imread('img.jpeg')


gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)


# Detects cars of different sizes in the input image
cars = car_cascade.detectMultiScale(gray, 1.1, 1)
# To draw a rectangle in each cars
for (x,y,w,h) in cars:
cv2.rectangle(image,(x,y),(x+w,y+h),(0,0,255),2)








# display the output image
cv2.imshow("Image", image)
cv2.waitKey(0)
cv2.destroyAllWindows()
