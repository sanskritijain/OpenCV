import cv2
import numpy as np

#init camera
cap = cv2.VideoCapture(0)

#Face Detection
face_cascade  = cv2.CascadeClassifier("C:/Users/Sanskriti/AppData/Local/Programs/Python/Python37/Scripts/codingBlocks/ProjectFaceRecogniton-OpenCV/haarcascade_frontalface_alt.xml")
skip = 0
face_data  = []
dataset_path = './data/'

file_name = input("enter the name of the person: ")
while (True):


    ret ,frame = cap.read()
    #ret = return 
    if ret == False :
        continue

    gray_frame = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    
    faces = face_cascade.detectMultiScale(frame,1.3,5)

    if(len(faces))==0:
       continue
    
    faces = sorted(faces, key = lambda f : f[2]*f[3] ,reverse = True) 
    #print(faces)

    for face in faces:
        x,y,w,h =face
        cv2.rectangle(frame , (x,y),(x+w,y+h),(255,0,0),2)

        

    #Extract (Crop out the required face) :Region of interest

        offset = 10 #pixels
        face_section = frame[y-offset:y+h+offset , x-offset : x+w+offset]
        face_section = cv2.resize(face_section ,(100,100))

        skip +=1
        if skip%10 ==0 :
            face_data.append(face_section)
            print(len(face_data))

   

    cv2.imshow("Frame", frame)
    cv2.imshow("Face Section" ,face_section)
    
    key_pressed = cv2.waitKey(1) & 0xFF
    if key_pressed == ord('q') :
        break
    
#Convert our face list array into numpy array
face_data = np.asarray(face_data)
face_data = face_data.reshape((face_data.shape[0],-1))
print(face_data.shape)

#Save this data into file system 
np.save(dataset_path+file_name+'.npy',face_data)
print("Data Successfully save at "+dataset_path+file_name+'.npy')

cap.release()
cv2.destroyAllWindows()
