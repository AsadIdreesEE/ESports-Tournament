from pickle import TRUE
import cv2
import numpy as np
import time
from pytesseract import pytesseract

cpt=0
mtime=0
x=0
y=0
maxframes = 10

cap = cv2.VideoCapture(1)
cap.set(3, 1920)
cap.set(4, 1080)
pytesseract.tesseract_cmd= "C:\\Program Files\\Tesseract-OCR\\tesseract.exe"
while True: #cpt<maxframes:
    ret,frame = cap.read()
    #frame=cv2.resize(frame,(0,0),fx=2,fy=2)
    frame = cv2.resize(frame,(3840,2160))
    frameTime = frame[280:350, 420:615]
    frameTeam1_name = frame[205:270, 230:390]
    frameTeam2_name = frame[205:270, 630:815]
    frame_Score_ALL= frame[205:350, 420:615]
    #frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    #frame=cv2.resize(frame,(0,0),fx=2,fy=2)
    #frame = (255-frame)
    #ret, frame = cv2.threshold(frame,127,255,cv2.THRESH_TOZERO)
    #cv2.adaptiveThreshold(img,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C,cv2.THRESH_BINARY,11,-2)
    #frame = cv2.adaptiveThreshold(frame, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C,cv2.THRESH_BINARY, 11, 2 )
    cv2.imshow('frame',frame_Score_ALL)
    #cv2.imwrite("C:/Work_File/ip_camera_project/photos/photos_%d.png" %cpt, frame)
    Score="AAAAAAA"
    letter_boxes = pytesseract.image_to_string(frameTime)
    Team1name = pytesseract.image_to_string(frameTeam1_name)
    Team2name = pytesseract.image_to_string(frameTeam2_name)
    Score=pytesseract.image_to_string(frame_Score_ALL)
    Score=Score+"000"
    if (Score[0]=='1') or (Score[0]=='2') or (Score[0]=='3') or (Score[0]=='4') or (Score[0]=='5') or (Score[0]=='6') or (Score[0]=='7') or (Score[0]=='8') or (Score[0]=='9'):
        x=int(Score[0])
    else:
        x=0
    if (Score[2]=='1') or (Score[2]=='2') or (Score[2]=='3') or (Score[2]=='4') or (Score[2]=='5') or (Score[2]=='6') or (Score[2]=='7') or (Score[2]=='8') or (Score[2]=='9'):
        y=int(Score[2])
    else:
        y=0

    var= letter_boxes[:1] 
    var2= letter_boxes[:2] 

    if (var =='0') or (var =='1') or (var=='2') or (var=='3') or (var=='4') or (var=='5') or (var=='6') or (var=='7')or (var=='8') or (var=='9'):
        mtime=int(var2)
    else:
        mtime=0
    print ("Current Time:  ")
    print(mtime)
    print("First Team:")
    print(Team1name[:3])
    print("Second Team:")
    print(Team2name[:3])
    print("Team1_Score:")
    #print(Score)
    print(Score)#x)
    print("Team2_Score:")
    #print(Score[2])#y)
    time.sleep(1)
    #cpt+=1

    k=cv2.waitKey(10) & 0xFF
    if k==27:
        break
cap.release()
cv2.destroyAllWindows()