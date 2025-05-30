
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
    frame = cv2.cvtColor(frame, cv2.COLOR_GRAY2BGR)
    frameTime = frame[280:350, 420:615]
    frameTeam1_name = frame[205:270, 230:390]
    frameTeam2_name = frame[205:270, 630:815]
    frame_Score1= frame[210:345, 440:585]
    frame_Score2= frame[210:345, 440:585]
    cv2.imshow('frame',frameTeam1_name)
    cv2.imwrite('frame.jpg',frameTeam1_name)
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
    Score1=Score1+"AAA"
    Score2=pytesseract.image_to_string(frame_Score2)
    Score2=Score2.rstrip('\n')# Removing /n from data 
    Score2=Score2+"AAA"

    #///////////////////////////////////////////////////////////////
    # Showing Time of the Match
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
    if (Team1name[3]!='1'):
        Team1name= Team1name_prev
    else:
        if (f==1):
            Team1name_prev=Team1name[:3]
        else:
            Team1name= Team1name_prev

    if (Team2name[3]!='1'):
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
    if (Score1[0]=='0') or (Score1[0]=='1') or (Score1[0]=='2') or (Score1[0]=='3') or (Score1[0]=='4') or (Score1[0]=='5') or (Score1[0]=='6') or (Score1[0]=='7') or (Score1[0]=='8') or (Score1[0]=='9'):
        if (int(Score1[0])<=(1+x1)):
            x1=x1p=int(Score1[0])
    else:
        x1=x1p
   


    if (Score2[2]=='0') or (Score2[2]=='1') or (Score2[2]=='2') or (Score2[2]=='3') or (Score2[2]=='4') or (Score2[2]=='5') or (Score2[2]=='6') or (Score2[2]=='7') or (Score2[2]=='8') or (Score2[2]=='9'):
        if (int(Score2[2])<=(1+y1)):
            y1=y1p=int(Score2[2])
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