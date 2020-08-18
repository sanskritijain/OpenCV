import cv2
import numpy as np 
import os


#img = cv2.imread("C:/Users/Sanskriti/AppData/Local/Programs/Python/Python37/Scripts/codingBlocks/ProjectFaceRecogniton-OpenCV/snapchatFilter/Test/Before.png",0)
#cv2.imshow("Before picture ",img)
face_cascade  = cv2.CascadeClassifier("C:/Users/Sanskriti/AppData/Local/Programs/Python/Python37/Scripts/codingBlocks/ProjectFaceRecogniton-OpenCV/haarcascade_frontalface_alt.xml")
eyes_cascade  = cv2.CascadeClassifier("C:/Users/Sanskriti/AppData/Local/Programs/Python/Python37/Scripts/codingBlocks/ProjectFaceRecogniton-OpenCV/snapchatFilter/haarcascade_eye.xml")


#nose_cascade = cv2.CascadeClassifier("C:/Users/Sanskriti/AppData/Local/Programs/Python/Python37/Scripts/codingBlocks/ProjectFaceRecogniton-OpenCV/snapchatFilter/Train/third-party/Nose18x15.xml")

glasses = cv2.imread("C:/Users/Sanskriti/AppData/Local/Programs/Python/Python37/Scripts/codingBlocks/ProjectFaceRecogniton-OpenCV/snapchatFilter/Train/glasses.png")
#mustache = cv2.imread("C:/Users/Sanskriti/AppData/Local/Programs/Python/Python37/Scripts/codingBlocks/ProjectFaceRecogniton-OpenCV/snapchatFilter/Train/mustache.png")

cap = cv2.VideoCapture(0)

while (True) :
    ret,frame= cap.read()

    if ret ==False :
        continue
    

    faces = face_cascade.detectMultiScale(frame , 1.3,5)
    for x,y,w,h in faces:
        roi_img = frame[y:y+h,x:x+w]
        cv2.rectangle(frame, (x,y),(x+w,y+h),(255,0,0),3) # 3 is for the width of the rectanglecv2.imshow("New Image" , img)

        eyes = eyes_cascade.detectMultiScale(roi_img,1.3,5)
        for ex,ey,ew,eh in eyes :
            cv2.rectangle(roi_img , (ex,ey),(ex+ew ,ey+eh),(255,255,0),2)
            
            
        

    cv2.imshow("faces", frame)

    key_pressed = cv2.waitKey(1) & 0xFF
    if key_pressed == ord('q'):
        break
    
cap.release()
cv2.destroyAllWindows();




