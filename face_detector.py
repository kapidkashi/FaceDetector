import cv2
from random import randrange

#load some pre-trained data on face frontals from opencv (haar cascade algorithm)
trained_face_data = cv2.CascadeClassifier('Face_Detector\haarcascade_frontalface_default.xml')
    
#choose an image to detect faces in
#img = cv2.imread('Face_Detector\RDJ.jpg')
webcam = cv2.VideoCapture(0)





#Iterate forever over frames
while True:
    ### Read Current frames
    successful_frame_read, frame = webcam.read()
    
    #must convert to grayscale
    grayscaled_img = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
   
    
    #Detect Faces   
    face_coordinates = trained_face_data.detectMultiScale(grayscaled_img)
    #Draw rectangles around the faces
    for (x,y,w,h) in face_coordinates:
     cv2.rectangle(frame, (x ,y), (x+w, y+h), (0, 255, 0), 2)
     
    cv2.imshow('Clever Programmer Face Detector', frame)
    key=cv2.waitKey(1)
    ###stop if Q is pressed
    if key==81 or key==113:
        break
    
    ###Release the videocapture object
    #webcam.release()
    
    
    """
#must convert to grayscale
grayscaled_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

#Detect Faces
face_coordinates = trained_face_data.detectMultiScale(grayscaled_img)

#Draw rectangles around the faces
for (x,y,w,h) in face_coordinates:
    cv2.rectangle(img, (x ,y), (x+w, y+h), (0, randrange(255), 0), 2)
#
cv2.imshow('Clever Programmer Face Detector', img)
cv2.waitKey()

print("Code Completed")
    
    """
