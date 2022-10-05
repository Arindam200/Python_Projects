import cv2
import mediapipe as mp
import time
Wcam,hcam=1080,2046
cap=cv2.VideoCapture(0)
cap.set(3,Wcam)
cap.set(4,hcam)
mpHands=mp.solutions.hands
hands=mpHands.Hands()
mpDraw=mp.solutions.drawing_utils
pTime=0
cTime=0
while True:
    success,img=cap.read()
    imgrgb=cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
    results=hands.process(imgrgb)
    #print(results.multi_hand_landmarks)
    if results.multi_hand_landmarks :
        for handlms in results.multi_hand_landmarks:
            for id,lm in enumerate(handlms.landmark):
                h,w,c=img.shape
                cx,cy=int(lm.x*w),int(lm.y*h)
                if id==4 :
                    cv2.circle(img,(cx,cy),15,(255,0,255),cv2.FILLED)
                if id==8 :
                    cv2.circle(img,(cx,cy),15,(255,0,255),cv2.FILLED)
                print(id,cx,cy)
            mpDraw.draw_landmarks(img,handlms,mpHands.HAND_CONNECTIONS)
    cTime=time.time()
    fps=1/(cTime-pTime)
    pTime=cTime
    

    cv2.putText(img,"FPS-"+str(int(fps)),(10,70),cv2.FONT_HERSHEY_COMPLEX,1,(255,0,255),4)

    cv2.imshow("image",img)
    cv2.waitKey(1)

