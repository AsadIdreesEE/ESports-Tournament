
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
    frameTime = frame[145:240, 200:445]
    frameTeam1_name = frame[145:240, 500:820]
    frameTeam2_name = frame[145:240, 1210:1570]
    frame_Score1= frame[135:245,500:950]
    frame_Score2= frame[135:245,1100:1570]
    #cv2.imshow('frame',frame_Score1)
    Game_Time= pytesseract.image_to_string(frameTime)
    Game_Time=Game_Time.rstrip('\n')
    Game_Time=Game_Time+"AAA"
    Team1name = pytesseract.image_to_string(frameTeam1_name)
    Team1name=Team1name.rstrip('\n')# removing /n to add data after
    Team1name=Team1name+'1___'# adding data after that in case there is nothing to read 
    Team2name = pytesseract.image_to_string(frameTeam2_name)
    Team2name=Team2name.rstrip('\n')
    Team2name=Team2name+'1___'
    Score1=pytesseract.image_to_string(frame_Score1)
    Score1=Score1.rstrip('\n')# Removing /n from data 
    Score1='A'+Score1
    Score2=pytesseract.image_to_string(frame_Score2)
    Score2=Score2.rstrip('\n')# Removing /n from data 
    Score2=Score2+"AAA"

    #//////////////////////////////////////////////////////
    # Time of the game
    Char1_Time= Game_Time[:1] 
    Char2_Time=Game_Time[1:2] 
    Char3_Time=Game_Time[2:3]
    Char1_2_Time= Game_Time[:2] 
    if  (Char1_Time =='0') or (Char1_Time =='1') or (Char1_Time=='2') or (Char1_Time=='3') or (Char1_Time=='4') or (Char1_Time=='5') or (Char1_Time=='6') or (Char1_Time=='7')or (Char1_Time=='8') or (Char1_Time=='9'):
        if (Char2_Time =='0') or (Char2_Time =='1') or (Char2_Time=='2') or (Char2_Time=='3') or (Char2_Time=='4') or (Char2_Time=='5') or (Char2_Time=='6') or (Char2_Time=='7')or (Char2_Time=='8') or (Char2_Time=='9'):
            MatchTime=MatchTime_prev=int(Char1_2_Time)
            f=1
    else:
        MatchTime=MatchTime_prev
        f=0

    print ("Current Time: "+ str(MatchTime))
    
    # End Time of the Match

    #//////////////////////////////////////////////////////////////
    #Showing the Name of the Teams
    if (Team1name[0]=='1'):
        Team1name= Team1name_prev
    else:
        if (f==1):
            Team1name_prev=Team1name[:3]
        else:
            Team1name= Team1name_prev

    if (Team2name[0]=='1'):
        Team2name= Team2name_prev
    else:
       if (f==1):
            Team2name_prev=Team2name[:3]
       else:
           Team2name= Team2name_prev

    print("First Team:"+ Team1name[:3])
    print("Second Team:"+Team2name[:3])
    # End Name of the teams
    #///////////////////////////////////////////////////////////////////////////

    # Showing the Scores:
    if (Score1[-1]=='0') or (Score1[-1]=='1') or (Score1[-1]=='2') or (Score1[-1]=='3') or (Score1[-1]=='4') or (Score1[-1]=='5') or (Score1[-1]=='6') or (Score1[-1]=='7') or (Score1[-1]=='8') or (Score1[-1]=='9'):
        if (int(Score1[-1])<=(1+x1)):
            x1=x1p=int(Score1[-1])

    elif(Score1[-1]=='G'):
        if ((x1<=4) and (x1>2)):
            x1=x1p=4
    else:
        x1=x1p
   
    if (Score2[0]=='0') or (Score2[0]=='1') or (Score2[0]=='2') or (Score2[0]=='3') or (Score2[0]=='4') or (Score2[0]=='5') or (Score2[0]=='6') or (Score2[0]=='7') or (Score2[0]=='8') or (Score2[0]=='9'):
        if (int(Score2[0])<=(1+y1)):
            y1=y1p=int(Score2[0])

    elif(Score2[0]=='G'):
        if ((y1<=4) and (y1>2)):
            y1=y1p=4
    else:
        y1=y1p

    print("Team1_Score:"+str(x1))
    print("Team2_Score:"+str(y1))

    # End Showing the Scores

    time.sleep(1)
    k=cv2.waitKey(10) & 0xFF
    if k==27:
        break
cap1.release()
cv2.destroyAllWindows()

