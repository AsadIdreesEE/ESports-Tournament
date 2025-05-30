

from pickle import TRUE
import cv2
import numpy as np
import time
from pytesseract import pytesseract

# Defining Variables
Team1name_prev='____'
Team2name_prev='____'
MatchTime=0
MatchTime_prev=0
f=0 # Flag to connect all data with showing the time 
x1=0
x1p=0
y1p=0
y1=0

#Opening HDMI
cap1 = cv2.VideoCapture(0)

#Adjusting the Resolution of ps5
cap1.set(3, 1920)
cap1.set(4, 1080)

#calling Required LIbrary
pytesseract.tesseract_cmd= "C:\\Program Files\\Tesseract-OCR\\tesseract.exe"

while True:
    ret,frame = cap1.read()
    frame = cv2.resize(frame,(3840,2160))
    frame=cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    #frame = cv2.cvtColor(frame, cv2.COLOR_GRAY2BGR)
    frameTime = frame[110:180, 285:460]
    frameTeam1_name = frame[110:180, 470:630]
    frameTeam2_name = frame[110:180, 660:800]
    frame_Score1= frame[185:315, 475:620]
    frame_Score2= frame[185:315, 675:820]
    #cv2.imshow('frame',frameTeam1_name)
    Game_Time= pytesseract.image_to_string(frameTime)
    Team1name = pytesseract.image_to_string(frameTeam1_name)
    Team1name=Team1name.rstrip('\n')# removing /n to add data after
    Team1name=Team1name+'1___'# adding data after that in case there is nothing to read 
    Team2name = pytesseract.image_to_string(frameTeam2_name)
    Team2name=Team2name.rstrip('\n')
    Team2name=Team2name+'1___'
    Score1=pytesseract.image_to_string(frame_Score1, config=("-c tessedit"
                  "_char_whitelist=abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"
                  " --psm 10"
                  " -l osd"
                  " "))
    Score1=Score1.rstrip('\n')# Removing /n from data 
    Score1=Score1+"AAA"
    Score2=pytesseract.image_to_string(frame_Score2, config=("-c tessedit"
                  "_char_whitelist=abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"
                  " --psm 10"
                  " -l osd"
                  " "))
    Score2=Score2.rstrip('\n')# Removing /n from data 
    Score2=Score2+"AAA"















    ret,frame1 = cap1.read()
    frame1 = cv2.resize(frame1,(3840,2160))
    frame1Time = frame1[110:180, 285:460]
    frame1Team1_name = frame1[110:180, 470:630]
    frame1Team1_name = cv2.cvtColor(frame1Team1_name, cv2.COLOR_BGR2GRAY)
    frame1Team1_name= cv2.cvtColor(frame1Team1_name, cv2.COLOR_GRAY2BGR)
    frame1Team2_name = frame1[110:180, 660:800]
    frame1Team2_name = cv2.cvtColor(frame1Team2_name, cv2.COLOR_BGR2GRAY)
    frame1Team2_name= cv2.cvtColor(frame1Team2_name, cv2.COLOR_GRAY2BGR)
    frame1_Score1= frame1[185:315, 475:620]
    frame1_Score1 = cv2.cvtColor(frame1_Score1, cv2.COLOR_BGR2GRAY)
    frame1_Score1= cv2.cvtColor(frame1_Score1, cv2.COLOR_GRAY2BGR)
    frame1_Score2= frame1[185:315, 675:820]
    frame1_Score2 = cv2.cvtColor(frame1_Score2, cv2.COLOR_BGR2GRAY)
    frame1_Score2= cv2.cvtColor(frame1_Score2, cv2.COLOR_GRAY2BGR)
    cv2.imshow('frame1',frame1_Score2)
    cv2.imshow('frame4',frame1_Score1)
    cv2.imshow('frame2',frame1Team1_name)
    cv2.imshow('frame3',frame1Team2_name)
    letter_boxes1 = pytesseract.image_to_string(frame1Time)
    Team1name1 = pytesseract.image_to_string(frame1Team1_name)
    Team1name1=Team1name1.rstrip('\n')
    Team1name1=Team1name1+'1___'
    Team2name1 = pytesseract.image_to_string(frame1Team2_name)
    Team2name1=Team2name1.rstrip('\n')
    Team2name1=Team2name1+'1___'

    Score1=pytesseract.image_to_string(frame1_Score1, config=("-c tessedit"
                  "_char_whitelist=abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"
                  " --psm 10"
                  " -l osd"
                  " "))#frame1_Score_ALL)
    Score1=Score1+"AAA"

    Score2=pytesseract.image_to_string(frame1_Score2, config=("-c tessedit"
                  "_char_whitelist=abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"
                  " --psm 10"
                  " -l osd"
                  " "))#frame1_Score_ALL)
    Score2=Score2+"AAA"
    
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
    if (Team1name1[3]!='1'):
        Team1name1= Team1name1p
    else:
        if (f1==1):
            Team1name1p=Team1name1[:3]
        else:
            Team1name1= Team1name1p

    if (Team2name1[3]!='1'):
        Team2name1= Team2name1p
    else:
       if (f1==1):
            Team2name1p=Team2name1[:3]
       else:
           Team2name1= Team2name1p


    # End Name of the teams
    #///////////////////////////////////////////////////////////////////////////

    # Showing the Scores:
    if (Score1[0]=='0') or (Score1[0]=='1') or (Score1[0]=='2') or (Score1[0]=='3') or (Score1[0]=='4') or (Score1[0]=='5') or (Score1[0]=='6') or (Score1[0]=='7') or (Score1[0]=='8') or (Score1[0]=='9'):
        if (int(Score1[0])<=(1+x1)):
            x1=x1p=int(Score1[0])
    elif (Score1[0]=='l'):
        if (x1<=1):
            x1=x1p=1
    else:
        x1=x1p
   


    if (Score2[0]=='0') or (Score2[0]=='1') or (Score2[0]=='2') or (Score2[0]=='3') or (Score2[0]=='4') or (Score2[0]=='5') or (Score2[0]=='6') or (Score2[0]=='7') or (Score2[0]=='8') or (Score2[0]=='9'):
        if (int(Score2[0])<=(1+y1)):
            y1=y1p=int(Score2[0])
    elif (Score2[0]=='l'):
        if (y1<=1):
            y1=y1p=1
    else:
        y1=y1p

    print("First Team:")
    print(Team1name1[:3])
    print("Second Team:")
    print(Team2name1[:3])
    print("Team1_Score:")
    print(x1)
    print("Team2_Score:")
    print(y1)
    time.sleep(1)

    k=cv2.waitKey(10) & 0xFF
    if k==27:
        break
cap1.release()
cv2.destroyAllWindows()
