import cv2
import imutils

hog = cv2.HOGDescriptor()
hog.setSVMDetector(cv2.HOGDescriptor_getDefaultPeopleDetector())

face_cascade = cv2.CascadeClassifier("C:\\Users\\aishw\\OneDrive\\Desktop\\urgh\\face_detection\\haarcascade_frontalface_default.xml")

cap = cv2.VideoCapture(0)  #opens webcam

while cap.isOpened():           #each frame of the video is converted to gray. rgb to gray
    ret, img, =  cap.read()
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray,1.1, 4 )

    for x,y,w,h in faces:
        img = cv2.rectangle(img, (x,y), (x+w,y+h),(0,255,0),3)
    


    if ret:
        image = imutils.resize(img,
                               width=min(400, img.shape[1]))

        # Detecting all the regions
        # in the Image that has a
        # pedestrians inside it
        (regions, _) = hog.detectMultiScale(img,winStride=(4, 4), padding=(4, 4), scale=1.05)

        # Drawing the regions in the
        # Image
        person=1
        for (x, y, w, h) in regions:

            cv2.rectangle(img, (x, y),(x + w, y + h),(0, 0, 255), 2)
            cv2.putText(img, f'person {person}', (x, y), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 255), 1)
            person+=1
            print(person-1)
            # Showing the output Image
        cv2.imshow("Image", image)
        if cv2.waitKey(25) & 0xFF == ord('q'):
            break
    else:
        break
    
cap.release()
cv2.destroyAllWindows
