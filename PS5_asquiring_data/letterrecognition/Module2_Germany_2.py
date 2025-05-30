from pickle import TRUE
import cv2
import numpy as np
import time
from pytesseract import pytesseract
var=0
Team1name1p='____'
Team2name1p='____'
m1time=0
cap1 = cv2.VideoCapture(1)
cap1.set(3, 1920)
from pickle import TRUE
import cv2
import numpy as np
import time
from pytesseract import pytesseract
Team1name1p='____'
Team2name1p='____'
m1time=0
f1=0
x1=0
x1p=0
y1p=0
y1=0
x11=0
y11=0
m1timep=0
var=0

cap1 = cv2.VideoCapture(1)
cap1.set(3, 1920)
cap1.set(4, 1080)
pytesseract.tesseract_cmd= "C:\\Program Files\\Tesseract-OCR\\tesseract.exe"

while True:
    ret,frame1 = cap1.read()
    frame1 = cv2.resize(frame1,(3840,2160))
    frame1Time = frame1[110:178, 192:368]
    frame1Time=(255-frame1Time)
    frame1Team1_name = frame1[110:185, 420:540]
    frame1Team2_name = frame1[110:185, 900:1040]
    frame1_Score_ALL= frame1[110:185, 760:1220]
    cv2.imshow('frame1',frame1Team1_name)
    cv2.imshow('frame2',frame1Team2_name)
    cv2.imshow('frame3',frame1_Score_ALL)
    letter_boxes1 = pytesseract.image_to_string(frame1Time)
    Team1name1 = pytesseract.image_to_string(frame1Team1_name)
    Team1name1=Team1name1.rstrip('\n')
    Team1name1=Team1name1+'1____'
    Team2name1 = pytesseract.image_to_string(frame1Team2_name)
    Team2name1=Team2name1.rstrip('\n')
    Team2name1=Team2name1+'1____'
    Score1=pytesseract.image_to_string(frame1_Score_ALL)
    Score1=Score1+"AAA"    

    #///////////////////////////////////////////////////////////////
    # Showing Time of the Match
    var1= letter_boxes1[:1] 
    var11=letter_boxes1[1:2] 
    var111=letter_boxes1[2:3]
    var12= letter_boxes1[:2] 
    var13=letter_boxes1[:3]
    if  (var1 =='0') or (var1 =='1') or (var1=='2') or (var1=='3') or (var1=='4') or (var1=='5') or (var1=='6') or (var1=='7')or (var1=='8') or (var1=='9'):
        if (var11 =='0') or (var11 =='1') or (var11=='2') or (var11=='3') or (var11=='4') or (var11=='5') or (var11=='6') or (var11=='7')or (var11=='8') or (var11=='9'):
            m1time=m1timep=int(var12)
            f1=1
            if (var111 =='0') or (var111 =='1'):
                m1time=m1timep=int(var13)
    else:
        m1time=m1timep
        f1=0

    print ("Current Time: ")
    print(m1time)
    # End Time of the Match

    #//////////////////////////////////////////////////////////////
    #Showing the Name of the Teams
    if ((Team1name1[3]!='1') and (Team1name1[4]!='1')):
        Team1name1= Team1name1p
        Team2name1= Team2name1p
    else:
        if (f1==1):
            Team1name1p=Team1name1[:3]
            Team2name1p=Team2name1[:3]
        else:
            Team1name1= Team1name1p
            Team2name1= Team2name1p


    # End Name of the teams
    #///////////////////////////////////////////////////////////////////////////

    # Showing the Scores:
    if (Score1[0]=='0') or (Score1[0]=='1') or (Score1[0]=='2') or (Score1[0]=='3') or (Score1[0]=='4') or (Score1[0]=='5') or (Score1[0]=='6') or (Score1[0]=='7') or (Score1[0]=='8') or (Score1[0]=='9'):
        if (int(Score1[0])<=(1+x1)):
            x1=x1p=int(Score1[0])
    else:
        x1=x1p
   
    if (Score1[2]=='0') or (Score1[2]=='1') or (Score1[2]=='2') or (Score1[2]=='3') or (Score1[2]=='4') or (Score1[2]=='5') or (Score1[2]=='6') or (Score1[2]=='7') or (Score1[2]=='8') or (Score1[2]=='9'):
        if (int(Score1[2])<=(1+y1)):
            y1=y1p=int(Score1[2])
    else:
        y1=y1p

    print("First Team:")
    print(Team1name1[:3])
    print("Second Team:")
    print(Team2name1[:3])
    print("Team1_Score:")
    print(Score1)#x1)
    print("Team2_Score:")
    print(y1)
    time.sleep(1)

    k=cv2.waitKey(10) & 0xFF
    if k==27:
        break
cap1.release()
cv2.destroyAllWindows()

