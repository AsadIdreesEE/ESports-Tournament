

from ast import Try
from pickle import TRUE
import cv2
import numpy as np
import time
from pytesseract import pytesseract

# Defining Variables
Team1name0=Team1name1=Team1name2=Team1name3=Team1name4=Team1name5=Team1name6=Team1name7='____'
Team2name0=Team2name1=Team2name2=Team2name3=Team2name4=Team2name5=Team2name6=Team2name7='----'
Team1name_prev0=Team1name_prev1=Team1name_prev2=Team1name_prev3=Team1name_prev4=Team1name_prev5=Team1name_prev6=Team1name_prev7='____'
Team2name_prev0=Team2name_prev1=Team2name_prev2=Team2name_prev3=Team2name_prev4=Team2name_prev5=Team2name_prev6=Team2name_prev7='____'
MatchTime0=MatchTime1=MatchTime2=MatchTime3=MatchTime4=MatchTime5=MatchTime6=MatchTime7=0
MatchTime_prev0=MatchTime_prev1=MatchTime_prev2=MatchTime_prev3=MatchTime_prev4=MatchTime_prev5=MatchTime_prev6=MatchTime_prev7=0

f0=f1=f2=f3=f4=f5=f6=f7=fp1=fp2=fp3=fp4=fp5=fp6=fp7=0 # Flag to connect all data with showing the time 
i0=i1=i2=i3=i4=i5=i6=i7=i8=0
x10=x11=x12=x13=x14=x15=x16=x17=0
y10=y11=y12=y13=y14=y15=y16=y17=0
x1p0=x1p1=x1p2=x1p3=x1p4=x1p5=x1p6=x1p7=0
y1p0=y1p1=y1p2=y1p3=y1p4=y1p5=y1p6=y1p7=0


var="00000000"
#var='EEEEEEEE'

#Opening HDMI
cap0 = cv2.VideoCapture(0)

cap1 = cv2.VideoCapture(1)

cap2 = cv2.VideoCapture(2)

cap3 = cv2.VideoCapture(3)

cap4 = cv2.VideoCapture(4)

cap5 = cv2.VideoCapture(5)

cap6 = cv2.VideoCapture(6)
#cap7 = cv2.VideoCapture(7)
#Adjusting the Resolution of ps5

cap0.set(3, 1920)
cap0.set(4, 1080)



cap1.set(3, 1920)
cap1.set(4, 1080)


cap2.set(3, 1920)
cap2.set(4, 1080)


cap3.set(3, 1920)
cap3.set(4, 1080)


cap4.set(3, 1920)
cap4.set(4, 1080)


cap5.set(3, 1920)
cap5.set(4, 1080)


cap6.set(3, 1920)
cap6.set(4, 1080)
#cap7.set(3, 1920)
#cap7.set(4, 1080)
#calling Required LIbrary
pytesseract.tesseract_cmd= "C:\\Program Files\\Tesseract-OCR\\tesseract.exe"

while True:
   
    ret,frame0 = cap0.read()
    
    ret,frame1 = cap1.read()
 
    ret,frame2 = cap2.read()
   
    ret,frame3 = cap3.read()
 
    ret,frame4 = cap4.read()
   
    ret,frame5 = cap5.read()
    
    ret,frame6 = cap6.read()
      
    #ret,frame7 = cap0.read()

    frame0 = cv2.resize(frame0,(3840,2160))
    
    frame1 = cv2.resize(frame1,(3840,2160))
    
    frame2 = cv2.resize(frame2,(3840,2160))
    
    frame3 = cv2.resize(frame3,(3840,2160))
    
    frame4 = cv2.resize(frame4,(3840,2160))
   
    frame5 = cv2.resize(frame5,(3840,2160))
    
    frame6 = cv2.resize(frame6,(3840,2160))
    
    #frame7 = cv2.resize(frame7,(3840,2160))

    frame0=cv2.cvtColor(frame0, cv2.COLOR_BGR2GRAY)
    frame1=cv2.cvtColor(frame1, cv2.COLOR_BGR2GRAY)
    frame2=cv2.cvtColor(frame2, cv2.COLOR_BGR2GRAY)
    frame3=cv2.cvtColor(frame3, cv2.COLOR_BGR2GRAY)
    frame4=cv2.cvtColor(frame4, cv2.COLOR_BGR2GRAY)
    frame5=cv2.cvtColor(frame5, cv2.COLOR_BGR2GRAY)
    frame6=cv2.cvtColor(frame6, cv2.COLOR_BGR2GRAY)
    #frame7=cv2.cvtColor(frame7, cv2.COLOR_BGR2GRAY)
    f= open('D:\\TeamsPlaying.txt', 'r') 
    if (f.readable()==True):
            #f=open('D:\\TeamsPlaying.txt', 'r')
        var=f.read()+'00000000'
    print('Started')
    if (var[0]=='E'):
        frameTime0 = frame0[280:350, 420:615]
        frameTeam1_name0 = frame0[205:270, 230:390]
        frameTeam2_name0 = frame0[205:270, 630:815]
        frame_Score10= frame0[210:345, 440:585]
        frame_Score20= frame0[210:345, 440:585]
        #cv2.imshow('frame',frameTeam1_name)
        Game_Time0= pytesseract.image_to_string(frameTime0)
        Game_Time0=Game_Time0.rstrip('\n')
        Game_Tim0=Game_Time0+"AAA"
        Team1name0 = pytesseract.image_to_string(frameTeam1_name0)
        Team1name0=Team1name0.rstrip('\n')# removing /n to add data after
        Team1name0=Team1name0+'1___'# adding data after that in case there is nothing to read 
        Team2name0 = pytesseract.image_to_string(frameTeam2_name0)
        Team2name0=Team2name0.rstrip('\n')
        Team2name0=Team2name0+'1___'
        Score10=pytesseract.image_to_string(frame_Score10)
        Score10=Score10.rstrip('\n')# Removing /n from data 
        Score10=Score10+"AAA"
        Score20=pytesseract.image_to_string(frame_Score20)
        Score20=Score20.rstrip('\n')# Removing /n from data 
        Score20=Score20+"AAA"
    # Showing Time of the Match
        Char1_Time0= Game_Time0[:1] 
        Char2_Time0=Game_Time0[1:2] 
        Char3_Time0=Game_Time0[2:3]
        Char1_2_Time0= Game_Time0[:2] 
        if  (Char1_Time0 =='0') or (Char1_Time0 =='1') or (Char1_Time0=='2') or (Char1_Time0=='3') or (Char1_Time0=='4') or (Char1_Time0=='5') or (Char1_Time0=='6') or (Char1_Time0=='7')or (Char1_Time0=='8') or (Char1_Time0=='9'):
            if (Char2_Time0 =='0') or (Char2_Time0 =='1') or (Char2_Time0=='2') or (Char2_Time0=='3') or (Char2_Time0=='4') or (Char2_Time0=='5') or (Char2_Time0=='6') or (Char2_Time0=='7')or (Char2_Time0=='8') or (Char2_Time0=='9'):
                MatchTime0=MatchTime_prev0=int(Char1_2_Time0)
                f0=1
        else:
            MatchTime0=MatchTime_prev0
            f0=0
    # End Time of the Match
    
    #Showing the Name of the Teams
        if (Team1name0[3]!='1'):
            Team1name0= Team1name_prev0
        else:
            if (f0==1):
                Team1name_prev0=Team1name0[:3]
            else:
                Team1name0= Team1name_prev0

        if (Team2name0[3]!='1'):
            Team2name0= Team2name_prev0
        else:
            if (f0==1):
                Team2name_prev0=Team2name0[:3]
            else:
                Team2name0= Team2name_prev0
 
    # Showing the Scores:
        if (Score10[0]=='0') or (Score10[0]=='1') or (Score10[0]=='2') or (Score10[0]=='3') or (Score10[0]=='4') or (Score10[0]=='5') or (Score10[0]=='6') or (Score10[0]=='7') or (Score10[0]=='8') or (Score10[0]=='9'):
            if (int(Score10[0])<=(1+x10)):
                x10=x1p0=int(Score10[0])
        else:
            x10=x1p0
   
        if (Score20[2]=='0') or (Score20[2]=='1') or (Score20[2]=='2') or (Score20[2]=='3') or (Score20[2]=='4') or (Score20[2]=='5') or (Score20[2]=='6') or (Score20[2]=='7') or (Score20[2]=='8') or (Score20[2]=='9'):
            if (int(Score20[2])<=(1+y10)):
                y10=y1p0=int(Score20[2])
        else:
            y10=y1p0
        try:
            f= open('D:\\TeamData.txt', 'w') 
            if (f.writable()==True):
        #with open('D:\\TeamData.txt', 'w') as f:
                f.write('E0    '+ Team1name0[:3]+'    '+Team2name0[:3]+'    '+ str(x10)+'    '+str(y10))
        except:
            pass
        time.sleep(0.3)
        #print ("Current Time: "+ str(MatchTime))
        
    elif (var[0]=='S'):
        frameTime0 = frame0[122:212, 305:560]
        frameTeam1_name0 = frame0[130:190, 575:765]
        frameTeam2_name0 = frame0[130:190, 995:1175]
        frame_Score10= frame0[115:210,780:1165]
        frame_Score20= frame0[115:210,780:1165]
        #cv2.imshow('frame',frame_Score10)
        Game_Time0= pytesseract.image_to_string(frameTime0)
        Game_Time0=Game_Time0.rstrip('\n')
        Game_Tim0=Game_Time0+"AAA"
        Team1name0 = pytesseract.image_to_string(frameTeam1_name0)
        Team1name0=Team1name0.rstrip('\n')# removing /n to add data after
        Team1name0=Team1name0+'1___'# adding data after that in case there is nothing to read 
        Team2name0 = pytesseract.image_to_string(frameTeam2_name0)
        Team2name0=Team2name0.rstrip('\n')
        Team2name0=Team2name0+'1___'
        Score10=pytesseract.image_to_string(frame_Score10)
        Score10=Score10.rstrip('\n')# Removing /n from data 
        Score10=Score10+"AAA"
        Score20=pytesseract.image_to_string(frame_Score20)
        Score20=Score20.rstrip('\n')# Removing /n from data 
        Score20=Score20+"AAA"
    # Showing Time of the Match
        Char1_Time0= Game_Time0[:1] 
        Char2_Time0=Game_Time0[1:2] 
        Char3_Time0=Game_Time0[2:3]
        Char1_2_Time0= Game_Time0[:2] 
        if  (Char1_Time0 =='0') or (Char1_Time0 =='1') or (Char1_Time0=='2') or (Char1_Time0=='3') or (Char1_Time0=='4') or (Char1_Time0=='5') or (Char1_Time0=='6') or (Char1_Time0=='7')or (Char1_Time0=='8') or (Char1_Time0=='9'):
            if (Char2_Time0 =='0') or (Char2_Time0 =='1') or (Char2_Time0=='2') or (Char2_Time0=='3') or (Char2_Time0=='4') or (Char2_Time0=='5') or (Char2_Time0=='6') or (Char2_Time0=='7')or (Char2_Time0=='8') or (Char2_Time0=='9'):
                MatchTime0=MatchTime_prev0=int(Char1_2_Time0)
                f0=1
        else:
            MatchTime0=MatchTime_prev0
            f0=0
    # End Time of the Match
    
    #Showing the Name of the Teams
        if (Team1name0[3]!='1'):
            Team1name0= Team1name_prev0
        else:
            if (f0==1):
                Team1name_prev0=Team1name0[:3]
            else:
                Team1name0= Team1name_prev0

        if (Team2name0[3]!='1'):
            Team2name0= Team2name_prev0
        else:
            if (f0==1):
                Team2name_prev0=Team2name0[:3]
            else:
                Team2name0= Team2name_prev0
 
    # Showing the Scores:
        if (Score10[0]=='0') or (Score10[0]=='1') or (Score10[0]=='2') or (Score10[0]=='3') or (Score10[0]=='4') or (Score10[0]=='5') or (Score10[0]=='6') or (Score10[0]=='7') or (Score10[0]=='8') or (Score10[0]=='9'):
            if (int(Score10[0])<=(1+x10)):
                x10=x1p0=int(Score10[0])
        else:
            x10=x1p0
   
        if (Score20[2]=='0') or (Score20[2]=='1') or (Score20[2]=='2') or (Score20[2]=='3') or (Score20[2]=='4') or (Score20[2]=='5') or (Score20[2]=='6') or (Score20[2]=='7') or (Score20[2]=='8') or (Score20[2]=='9'):
            if (int(Score20[2])<=(1+y10)):
                y10=y1p0=int(Score20[2])
        else:
            y10=y1p0
        try:
            f= open('D:\\TeamData.txt', 'w') 
            if (f.writable()==True):
        #with open('D:\\TeamData.txt', 'w') as f:
                f.write('S0    '+ Team1name0[:3]+'    '+Team2name0[:3]+'    '+ str(x10)+'    '+str(y10))
        except:
            pass
        time.sleep(0.3)

    ##############################################################
    elif (var[0]=='I'):
        frameTime0 = frame0[130:215, 1180:1370]
        frameTeam1_name0 = frame0[130:220, 330:540]
        frameTeam2_name0 = frame0[130:220, 930:1100]
        frame_Score10= frame0[130:210, 650:800]
        frame_Score20= frame0[130:210, 650:800]
        Game_Time0= pytesseract.image_to_string(frameTime0)
        Game_Time0=Game_Time0.rstrip('\n')
        Game_Tim0=Game_Time0+"AAA"
        Team1name0 = pytesseract.image_to_string(frameTeam1_name0)
        Team1name0=Team1name0.rstrip('\n')# removing /n to add data after
        Team1name0=Team1name0+'1___'# adding data after that in case there is nothing to read 
        Team2name0 = pytesseract.image_to_string(frameTeam2_name0)
        Team2name0=Team2name0.rstrip('\n')
        Team2name0=Team2name0+'1___'
        Score10=pytesseract.image_to_string(frame_Score10)
        Score10=Score10.rstrip('\n')# Removing /n from data 
        Score10=Score10+"AAA"
        Score20=pytesseract.image_to_string(frame_Score20)
        Score20=Score20.rstrip('\n')# Removing /n from data 
        Score20=Score20+"AAA"

        Char1_Time0= Game_Time0[:1] 
        Char2_Time0=Game_Time0[1:2] 
        Char3_Time0=Game_Time0[2:3]
        Char1_2_Time0= Game_Time0[:2] 
        fp0=f0
        if  (Char1_Time0 =='0') or (Char1_Time0 =='1') or (Char1_Time0=='2') or (Char1_Time0=='3') or (Char1_Time0=='4') or (Char1_Time0=='5') or (Char1_Time0=='6') or (Char1_Time0=='7')or (Char1_Time0=='8') or (Char1_Time0=='9'):
            if (Char2_Time0 =='0') or (Char2_Time0 =='1') or (Char2_Time0=='2') or (Char2_Time0=='3') or (Char2_Time0=='4') or (Char2_Time0=='5') or (Char2_Time0=='6') or (Char2_Time0=='7')or (Char2_Time0=='8') or (Char2_Time0=='9'):
                MatchTime0=MatchTime_prev0=int(Char1_2_Time0)
                f0=1
        else:
            MatchTime0=MatchTime_prev0
            f0=0
        if (f0==1):
            if(fp0==0):
                i0=i0+1
        if (i0>=1):
            i0=i0+1
        if (i0>3):
            i0=0

        if (Team1name0[3]!='1'):
            Team1name0= Team1name_prev0
        else:
            if (f0==1):  
                Team1name_prev0=Team1name0[:3]    
            else:
                Team1name0= Team1name_prev0

        if (Team2name0[3]!='1'):
            Team2name0= Team2name_prev0
        else:
            if (f0==1):
                Team2name_prev0=Team2name0[:3]
            else:
                Team2name0= Team2name_prev0

       
    # End Name of the teams

    # Showing the Scores:
        if (f0==1):
            if (Score10[0]=='0') or (Score10[0]=='1') or (Score10[0]=='2') or (Score10[0]=='3') or (Score10[0]=='4') or (Score10[0]=='5') or (Score10[0]=='6') or (Score10[0]=='7') or (Score10[0]=='8') or (Score10[0]=='9'):
                if (int(Score10[0])<=(1+x10)):
                    x10=x1p0=int(Score10[0])
            else:
                x10=x1p0
        else:
            x10=x1p0
   

        if (f0==1):
            if (Score20[2]=='0') or (Score20[2]=='1') or (Score20[2]=='2') or (Score20[2]=='3') or (Score20[2]=='4') or (Score20[2]=='5') or (Score20[2]=='6') or (Score20[2]=='7') or (Score20[2]=='8') or (Score20[2]=='9'):
                if (int(Score20[2])<=(1+y10)):
                    y10=y1p0=int(Score20[2])
            else:
                y10=y1p0
        else:
            y10=y1p0
        try:
            f= open('D:\\TeamData.txt', 'w') 
            if (f.writable()==True):
        #with open('D:\\TeamData.txt', 'w') as f:
                f.write('I0    '+ Team1name0[:3]+'    '+Team2name0[:3]+'    '+ str(x10)+'    '+str(y10))
        except:
            pass
        time.sleep(0.3)

#########################################################################
    elif (var[0]=='G'):
        frameTime0 = frame0[110:180, 285:460]
        frameTeam1_name0 = frame0[110:180, 470:630]
        frameTeam2_name0 = frame0[110:180, 660:800]
        frame_Score10= frame0[185:315, 475:620]
        frame_Score20= frame0[185:315, 675:820]
        Game_Time0= pytesseract.image_to_string(frameTime0)
        Game_Time0=Game_Time0.rstrip('\n')
        Game_Time0=Game_Time0+"AAA"
        Team1name0 = pytesseract.image_to_string(frameTeam1_name0)
        Team1name0=Team1name0.rstrip('\n')# removing /n to add data after
        Team1name0=Team1name0+'1___'# adding data after that in case there is nothing to read 
        Team2name0 = pytesseract.image_to_string(frameTeam2_name0)
        Team2name0=Team2name0.rstrip('\n')
        Team2name0=Team2name0+'1___'
        Score10=pytesseract.image_to_string(frame_Score10, config=("-c tessedit"
                  "_char_whitelist=abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"
                  " --psm 10"
                  " -l osd"
                  " "))
        Score10=Score10.rstrip('\n')# Removing /n from data 
        Score10=Score10+"AAA"
        Score20=pytesseract.image_to_string(frame_Score20, config=("-c tessedit"
                  "_char_whitelist=abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"
                  " --psm 10"
                  " -l osd"
                  " "))
        Score20=Score20.rstrip('\n')# Removing /n from data 
        Score20=Score20+"AAA"

    #///////////////////////////////////////////////////////////////
    # Showing Time of the Match
        Char1_Time0= Game_Time0[:1] 
        Char2_Time0=Game_Time0[1:2] 
        Char3_Time0=Game_Time0[2:3]
        Char1_2_Time0= Game_Time0[:2] 
        if  (Char1_Time0 =='0') or (Char1_Time0 =='1') or (Char1_Time0=='2') or (Char1_Time0=='3') or (Char1_Time0=='4') or (Char1_Time0=='5') or (Char1_Time0=='6') or (Char1_Time0=='7')or (Char1_Time0=='8') or (Char1_Time0=='9'):
            if (Char2_Time0 =='0') or (Char2_Time0 =='1') or (Char2_Time0=='2') or (Char2_Time0=='3') or (Char2_Time0=='4') or (Char2_Time0=='5') or (Char2_Time0=='6') or (Char2_Time0=='7')or (Char2_Time0=='8') or (Char2_Time0=='9'):
                MatchTime0=MatchTime_prev0=int(Char1_2_Time0)
                f0=1
        else:
            MatchTime0=MatchTime_prev0
            f0=0

        if (Team1name0[3]!='1'):
            Team1name0= Team1name_prev0
        else:
            if (f0==1):
                Team1name_prev0=Team1name0[:3]
            else:
                Team1name0= Team1name_prev0

        if (Team2name0[3]!='1'):
            Team2name0= Team2name_prev0
        else:
            if (f0==1):
                Team2name_prev0=Team2name0[:3]
            else:
                Team2name0= Team2name_prev0

        if (Score10[0]=='0') or (Score10[0]=='1') or (Score10[0]=='2') or (Score10[0]=='3') or (Score10[0]=='4') or (Score10[0]=='5') or (Score10[0]=='6') or (Score10[0]=='7') or (Score10[0]=='8') or (Score10[0]=='9'):
            if (int(Score10[0])<=(1+x10)):
                x10=x1p0=int(Score10[0])
        elif (Score10[0]=='l'):
            if (x10<=1):
                x10=x1p0=1
        else:
            x10=x1p0
   


        if (Score20[0]=='0') or (Score20[0]=='1') or (Score20[0]=='2') or (Score20[0]=='3') or (Score20[0]=='4') or (Score20[0]=='5') or (Score20[0]=='6') or (Score20[0]=='7') or (Score20[0]=='8') or (Score20[0]=='9'):
            if (int(Score20[0])<=(1+y10)):
                y10=y1p0=int(Score20[0])
        elif (Score20[0]=='l'):
            if (y10<=1):
                y10=y1p0=1
        else:
            y10=y1p0
        try:
            f= open('D:\\TeamData.txt', 'w') 
            if (f.writable()==True):
        #with open('D:\\TeamData.txt', 'a') as f:
                f.write('\nG0    '+ Team1name0[:3]+'    '+Team2name0[:3]+'    '+ str(x10)+'    '+str(y10))
        except:
            pass
        time.sleep(0.3)

    elif (var[0]=='F'):
        frameTime0 = frame0[145:240, 200:445]
        frameTeam1_name0 = frame0[145:240, 500:820]
        frameTeam2_name0 = frame0[145:240, 1210:1570]
        frame_Score10= frame0[135:245,500:950]
        frame_Score20= frame0[135:245,1100:1570]
        Game_Time0= pytesseract.image_to_string(frameTime0)
        Game_Time0=Game_Time0.rstrip('\n')
        Game_Time0=Game_Time0+"AAA"
        Team1name0 = pytesseract.image_to_string(frameTeam1_name0)
        Team1name0=Team1name0.rstrip('\n')# removing /n to add data after
        Team1name0=Team1name0+'1___'# adding data after that in case there is nothing to read 
        Team2name0 = pytesseract.image_to_string(frameTeam2_name0)
        Team2name0=Team2name0.rstrip('\n')
        Team2name0=Team2name0+'1___'
        Score10=pytesseract.image_to_string(frame_Score10)
        Score10=Score10.rstrip('\n')# Removing /n from data 
        Score10='A'+Score10
        Score20=pytesseract.image_to_string(frame_Score20)
        Score20=Score20.rstrip('\n')# Removing /n from data 
        Score20=Score20+"AAA"

    #//////////////////////////////////////////////////////
    # Time of the game
        Char1_Time0= Game_Time0[:1] 
        Char2_Time0=Game_Time0[1:2] 
        Char3_Time0=Game_Time0[2:3]
        Char1_2_Time0= Game_Time0[:2] 
        if  (Char1_Time0 =='0') or (Char1_Time0 =='1') or (Char1_Time0=='2') or (Char1_Time0=='3') or (Char1_Time0=='4') or (Char1_Time0=='5') or (Char1_Time0=='6') or (Char1_Time0=='7')or (Char1_Time0=='8') or (Char1_Time0=='9'):
            if (Char2_Time0 =='0') or (Char2_Time0 =='1') or (Char2_Time0=='2') or (Char2_Time0=='3') or (Char2_Time0=='4') or (Char2_Time0=='5') or (Char2_Time0=='6') or (Char2_Time0=='7')or (Char2_Time0=='8') or (Char2_Time0=='9'):
                MatchTime0=MatchTime_prev0=int(Char1_2_Time0)
                f0=1
        else:
            MatchTime0=MatchTime_prev0
            f0=0

        if (Team1name0[0]=='1'):
            Team1name0= Team1name_prev0
        else:
            if (f0==1):
                Team1name_prev0=Team1name0[:3]
            else:
                Team1name0= Team1name_prev0

        if (Team2name0[0]=='1'):
            Team2name0= Team2name_prev0
        else:
            if (f0==1):
                Team2name_prev0=Team2name0[:3]
            else:
                Team2name0= Team2name_prev0

    
        if (Score10[-1]=='0') or (Score10[-1]=='1') or (Score10[-1]=='2') or (Score10[-1]=='3') or (Score10[-1]=='4') or (Score10[-1]=='5') or (Score10[-1]=='6') or (Score10[-1]=='7') or (Score10[-1]=='8') or (Score10[-1]=='9'):
            if (int(Score10[-1])<=(1+x10)):
                x10=x1p0=int(Score10[-1])

        elif(Score10[-1]=='G'):
             if ((x10<=4) and (x10>2)):
                x10=x1p0=4
        else:
            x10=x1p0
   
        if (Score20[0]=='0') or (Score20[0]=='1') or (Score20[0]=='2') or (Score20[0]=='3') or (Score20[0]=='4') or (Score20[0]=='5') or (Score20[0]=='6') or (Score20[0]=='7') or (Score20[0]=='8') or (Score20[0]=='9'):
            if (int(Score20[0])<=(1+y10)):
                y10=y1p0=int(Score20[0])

        elif(Score20[0]=='G'):
            if ((y10<=4) and (y10>2)):
                y10=y1p0=4
        else:
            y10=y1p0
        try: 
            f= open('D:\\TeamData.txt', 'w') 
            if (f.writable()==True):
        #with open('D:\\TeamData.txt', 'w') as f:
                f.write('F0    '+ Team1name0[:3]+'    '+Team2name0[:3]+'    '+ str(x10)+'    '+str(y10))
        except:
            pass

        time.sleep(0.3)

    elif (var[0]=='R'):
        frameTime0 = frame0[110:180, 200:400]
        frameTeam1_name0 = frame0[110:180, 470:640]
        frameTeam2_name0 = frame0[110:180, 850:1010]
        frame_Score10= frame0[110:180, 660:835]
        frame_Score20= frame0[110:180, 660:835]
        #cv2.imshow('frame',frameTeam1_name)
        Game_Time0= pytesseract.image_to_string(frameTime0)
        Game_Time0=Game_Time0.rstrip('\n')
        Game_Tim0=Game_Time0+"AAA"
        Team1name0 = pytesseract.image_to_string(frameTeam1_name0)
        Team1name0=Team1name0.rstrip('\n')# removing /n to add data after
        Team1name0=Team1name0+'1___'# adding data after that in case there is nothing to read 
        Team2name0 = pytesseract.image_to_string(frameTeam2_name0)
        Team2name0=Team2name0.rstrip('\n')
        Team2name0=Team2name0+'1___'
        Score10=pytesseract.image_to_string(frame_Score10)
        Score10=Score10.rstrip('\n')# Removing /n from data 
        Score10=Score10+"AAA"
        Score20=pytesseract.image_to_string(frame_Score20)
        Score20=Score20.rstrip('\n')# Removing /n from data 
        Score20=Score20+"AAA"
    # Showing Time of the Match
        Char1_Time0= Game_Time0[:1] 
        Char2_Time0=Game_Time0[1:2] 
        Char3_Time0=Game_Time0[2:3]
        Char1_2_Time0= Game_Time0[:2] 
        if  (Char1_Time0 =='0') or (Char1_Time0 =='1') or (Char1_Time0=='2') or (Char1_Time0=='3') or (Char1_Time0=='4') or (Char1_Time0=='5') or (Char1_Time0=='6') or (Char1_Time0=='7')or (Char1_Time0=='8') or (Char1_Time0=='9'):
            if (Char2_Time0 =='0') or (Char2_Time0 =='1') or (Char2_Time0=='2') or (Char2_Time0=='3') or (Char2_Time0=='4') or (Char2_Time0=='5') or (Char2_Time0=='6') or (Char2_Time0=='7')or (Char2_Time0=='8') or (Char2_Time0=='9'):
                MatchTime0=MatchTime_prev0=int(Char1_2_Time0)
                f0=1
        else:
            MatchTime0=MatchTime_prev0
            f0=0
    # End Time of the Match
    
    #Showing the Name of the Teams
        if (Team1name0[3]!='1'):
            Team1name0= Team1name_prev0
        else:
            if (f0==1):
                Team1name_prev0=Team1name0[:3]
            else:
                Team1name0= Team1name_prev0

        if (Team2name0[3]!='1'):
            Team2name0= Team2name_prev0
        else:
            if (f0==1):
                Team2name_prev0=Team2name0[:3]
            else:
                Team2name0= Team2name_prev0
 
    # Showing the Scores:
        if (Score10[0]=='0') or (Score10[0]=='1') or (Score10[0]=='2') or (Score10[0]=='3') or (Score10[0]=='4') or (Score10[0]=='5') or (Score10[0]=='6') or (Score10[0]=='7') or (Score10[0]=='8') or (Score10[0]=='9'):
            if (int(Score10[0])<=(1+x10)):
                x10=x1p0=int(Score10[0])
        else:
            x10=x1p0
   
        if (Score20[2]=='0') or (Score20[2]=='1') or (Score20[2]=='2') or (Score20[2]=='3') or (Score20[2]=='4') or (Score20[2]=='5') or (Score20[2]=='6') or (Score20[2]=='7') or (Score20[2]=='8') or (Score20[2]=='9'):
            if (int(Score20[2])<=(1+y10)):
                y10=y1p0=int(Score20[2])
        else:
            y10=y1p0
        try:
            f= open('D:\\TeamData.txt', 'w') 
            if (f.writable()==True):
        #with open('D:\\TeamData.txt', 'w') as f:
                f.write('R0    '+ Team1name0[:3]+'    '+Team2name0[:3]+'    '+ str(x10)+'    '+str(y10))
        except:
            pass
        time.sleep(0.3)

        
        #with open('D:\\TeamData.txt', 'w') as f:
            #f.write('___')
#################################################################################################################################
    if(var[1]=='E'):
        frameTime1 = frame1[280:350, 420:615]
        frameTeam1_name1 = frame1[205:270, 230:390]
        frameTeam2_name1 = frame1[205:270, 630:815]
        frame_Score11= frame1[210:345, 440:585]
        frame_Score21= frame1[210:345, 440:585]
        #cv2.imshow('frame',frameTeam1_name)
        Game_Time1= pytesseract.image_to_string(frameTime1)
        Game_Time1=Game_Time1.rstrip('\n')
        Game_Tim1=Game_Time1+"AAA"
        Team1name1 = pytesseract.image_to_string(frameTeam1_name1)
        Team1name1=Team1name1.rstrip('\n')# removing /n to add data after
        Team1name1=Team1name1+'1___'# adding data after that in case there is nothing to read 
        Team2name1 = pytesseract.image_to_string(frameTeam2_name1)
        Team2name1=Team2name1.rstrip('\n')
        Team2name1=Team2name1+'1___'
        Score11=pytesseract.image_to_string(frame_Score11)
        Score11=Score11.rstrip('\n')# Removing /n from data 
        Score11=Score11+"AAA"
        Score21=pytesseract.image_to_string(frame_Score21)
        Score21=Score21.rstrip('\n')# Removing /n from data 
        Score21=Score21+"AAA"

    # Showing Time of the Match
        Char1_Time1= Game_Time1[:1] 
        Char2_Time1=Game_Time1[1:2] 
        Char3_Time1=Game_Time1[2:3]
        Char1_2_Time1= Game_Time1[:2] 
        if  (Char1_Time1 =='0') or (Char1_Time1 =='1') or (Char1_Time1=='2') or (Char1_Time1=='3') or (Char1_Time1=='4') or (Char1_Time1=='5') or (Char1_Time1=='6') or (Char1_Time1=='7')or (Char1_Time1=='8') or (Char1_Time1=='9'):
            if (Char2_Time1 =='0') or (Char2_Time1 =='1') or (Char2_Time1=='2') or (Char2_Time1=='3') or (Char2_Time1=='4') or (Char2_Time1=='5') or (Char2_Time1=='6') or (Char2_Time1=='7')or (Char2_Time1=='8') or (Char2_Time1=='9'):
                MatchTime1=MatchTime_prev1=int(Char1_2_Time1)
                f1=1
        else:
            MatchTime1=MatchTime_prev1
            f1=0
    #Showing the Name of the Teams
        if (Team1name1[3]!='1'):
            Team1name1= Team1name_prev1
        else:
            if (f1==1):
                Team1name_prev1=Team1name1[:3]
            else:
                Team1name1= Team1name_prev1

        if (Team2name1[3]!='1'):
            Team2name1= Team2name_prev1
        else:
            if (f1==1):
                Team2name_prev1=Team2name1[:3]
            else:
                Team2name1= Team2name_prev1

    # Showing the Scores:
        if (Score11[0]=='0') or (Score11[0]=='1') or (Score11[0]=='2') or (Score11[0]=='3') or (Score11[0]=='4') or (Score11[0]=='5') or (Score11[0]=='6') or (Score11[0]=='7') or (Score11[0]=='8') or (Score11[0]=='9'):
            if (int(Score11[0])<=(1+x11)):
                x11=x1p1=int(Score11[0])
        else:
            x11=x1p1
   
        if (Score21[2]=='0') or (Score21[2]=='1') or (Score21[2]=='2') or (Score21[2]=='3') or (Score21[2]=='4') or (Score21[2]=='5') or (Score21[2]=='6') or (Score21[2]=='7') or (Score21[2]=='8') or (Score21[2]=='9'):
            if (int(Score21[2])<=(1+y11)):
                y11=y1p1=int(Score21[2])
        else:
            y11=y1p1
        try:
            f= open('D:\\TeamData.txt', 'a') 
            if (f.writable()==True):
        #with open('D:\\TeamData.txt', 'a') as f:
                f.write('\nE1    '+ Team1name1[:3]+'    '+Team2name1[:3]+'    '+ str(x11)+'    '+str(y11))
        except:
            pass
        #print('E1    '+ Team1name1[:3]+'    '+Team2name1[:3]+'    '+ str(x11)+'    '+str(y11))
        time.sleep(0.3)
#############################################################################################
    elif (var[1]=='S'):
        frameTime1 = frame1[122:212, 305:560]
        frameTeam1_name1 = frame1[130:190, 575:765]
        frameTeam2_name1 = frame1[130:190, 995:1175]
        frame_Score11= frame1[115:210,780:1165]
        frame_Score21= frame1[115:210,780:1165]
        #cv2.imshow('frame',frame_Score11)
        Game_Time1= pytesseract.image_to_string(frameTime1)
        Game_Time1=Game_Time1.rstrip('\n')
        Game_Tim1=Game_Time1+"AAA"
        Team1name1 = pytesseract.image_to_string(frameTeam1_name1)
        Team1name1=Team1name1.rstrip('\n')# removing /n to add data after
        Team1name1=Team1name1+'1___'# adding data after that in case there is nothing to read 
        Team2name1 = pytesseract.image_to_string(frameTeam2_name1)
        Team2name1=Team2name1.rstrip('\n')
        Team2name1=Team2name1+'1___'
        Score11=pytesseract.image_to_string(frame_Score11)
        Score11=Score11.rstrip('\n')# Removing /n from data 
        Score11=Score11+"AAA"
        Score21=pytesseract.image_to_string(frame_Score21)
        Score21=Score21.rstrip('\n')# Removing /n from data 
        Score21=Score21+"AAA"

    #///////////////////////////////////////////////////////////////
    # Showing Time of the Match
        Char1_Time1= Game_Time1[:1] 
        Char2_Time1=Game_Time1[1:2] 
        Char3_Time1=Game_Time1[2:3]
        Char1_2_Time1= Game_Time1[:2] 
        if  (Char1_Time1 =='0') or (Char1_Time1 =='1') or (Char1_Time1=='2') or (Char1_Time1=='3') or (Char1_Time1=='4') or (Char1_Time1=='5') or (Char1_Time1=='6') or (Char1_Time1=='7')or (Char1_Time1=='8') or (Char1_Time1=='9'):
            if (Char2_Time1 =='0') or (Char2_Time1 =='1') or (Char2_Time1=='2') or (Char2_Time1=='3') or (Char2_Time1=='4') or (Char2_Time1=='5') or (Char2_Time1=='6') or (Char2_Time1=='7')or (Char2_Time1=='8') or (Char2_Time1=='9'):
                MatchTime1=MatchTime_prev1=int(Char1_2_Time1)
                f1=1
        else:
            MatchTime1=MatchTime_prev1
            f1=0
    #Showing the Name of the Teams
        if (Team1name1[3]!='1'):
            Team1name1= Team1name_prev1
        else:
            if (f1==1):
                Team1name_prev1=Team1name1[:3]
            else:
                Team1name1= Team1name_prev1

        if (Team2name1[3]!='1'):
            Team2name1= Team2name_prev1
        else:
            if (f1==1):
                Team2name_prev1=Team2name1[:3]
            else:
                Team2name1= Team2name_prev1

    # Showing the Scores:
        if (Score11[0]=='0') or (Score11[0]=='1') or (Score11[0]=='2') or (Score11[0]=='3') or (Score11[0]=='4') or (Score11[0]=='5') or (Score11[0]=='6') or (Score11[0]=='7') or (Score11[0]=='8') or (Score11[0]=='9'):
            if (int(Score11[0])<=(1+x11)):
                x11=x1p1=int(Score11[0])
        else:
            x11=x1p1
   
        if (Score21[2]=='0') or (Score21[2]=='1') or (Score21[2]=='2') or (Score21[2]=='3') or (Score21[2]=='4') or (Score21[2]=='5') or (Score21[2]=='6') or (Score21[2]=='7') or (Score21[2]=='8') or (Score21[2]=='9'):
            if (int(Score21[2])<=(1+y11)):
                y11=y1p1=int(Score21[2])
        else:
            y11=y1p1
        try:
            f= open('D:\\TeamData.txt', 'a') 
            if (f.writable()==True):
        #with open('D:\\TeamData.txt', 'a') as f:
                f.write('\nS1    '+ Team1name1[:3]+'    '+Team2name1[:3]+'    '+ str(x11)+'    '+str(y11))
        except:
            pass
        time.sleep(0.3)
    elif (var[1]=='I'):
        frameTime1 = frame1[130:215, 1180:1370]
        frameTeam1_name1 = frame1[130:220, 330:540]
        frameTeam2_name1 = frame1[130:220, 930:1100]
        frame_Score11= frame1[130:210, 650:800]
        frame_Score21= frame1[130:210, 650:800]
        Game_Time1= pytesseract.image_to_string(frameTime1)
        Game_Time1=Game_Time1.rstrip('\n')
        Game_Tim1=Game_Time1+"AAA"
        Team1name1 = pytesseract.image_to_string(frameTeam1_name1)
        Team1name1=Team1name1.rstrip('\n')# removing /n to add data after
        Team1name1=Team1name1+'1___'# adding data after that in case there is nothing to read 
        Team2name1 = pytesseract.image_to_string(frameTeam2_name1)
        Team2name1=Team2name1.rstrip('\n')
        Team2name1=Team2name1+'1___'
        Score11=pytesseract.image_to_string(frame_Score11)
        Score11=Score11.rstrip('\n')# Removing /n from data 
        Score11=Score11+"AAA"
        Score21=pytesseract.image_to_string(frame_Score21)
        Score21=Score21.rstrip('\n')# Removing /n from data 
        Score21=Score21+"AAA"

        Char1_Time1= Game_Time1[:1] 
        Char2_Time1=Game_Time1[1:2] 
        Char3_Time1=Game_Time1[2:3]
        Char1_2_Time1= Game_Time1[:2] 
        fp1=f1
        if  (Char1_Time1 =='0') or (Char1_Time1 =='1') or (Char1_Time1=='2') or (Char1_Time1=='3') or (Char1_Time1=='4') or (Char1_Time1=='5') or (Char1_Time1=='6') or (Char1_Time1=='7')or (Char1_Time1=='8') or (Char1_Time1=='9'):
            if (Char2_Time1 =='0') or (Char2_Time1 =='1') or (Char2_Time1=='2') or (Char2_Time1=='3') or (Char2_Time1=='4') or (Char2_Time1=='5') or (Char2_Time1=='6') or (Char2_Time1=='7')or (Char2_Time1=='8') or (Char2_Time1=='9'):
                MatchTime1=MatchTime_prev1=int(Char1_2_Time1)
                f1=1
        else:
            MatchTime1=MatchTime_prev1
            f1=0
        if (f1==1):
            if(fp1==0):
                i1=i1+1
        if (i1>=1):
            i1=i1+1
        if (i1>3):
            i1=0

        if (Team1name1[3]!='1'):
            Team1name1= Team1name_prev1
        else:
            if (f1==1):  
                Team1name_prev1=Team1name1[:3]    
            else:
                Team1name1= Team1name_prev1

        if (Team2name1[3]!='1'):
            Team2name1= Team2name_prev1
        else:
            if (f1==1):
                Team2name_prev1=Team2name1[:3]
            else:
                Team2name1= Team2name_prev1

       
    # End Name of the teams

    # Showing the Scores:
        if (f1==1):
            if (Score11[0]=='0') or (Score11[0]=='1') or (Score11[0]=='2') or (Score11[0]=='3') or (Score11[0]=='4') or (Score11[0]=='5') or (Score11[0]=='6') or (Score11[0]=='7') or (Score11[0]=='8') or (Score11[0]=='9'):
                if (int(Score11[0])<=(1+x11)):
                    x11=x1p1=int(Score11[0])
            else:
                x11=x1p1
        else:
            x11=x1p1
   

        if (f1==1):
            if (Score21[2]=='0') or (Score21[2]=='1') or (Score21[2]=='2') or (Score21[2]=='3') or (Score21[2]=='4') or (Score21[2]=='5') or (Score21[2]=='6') or (Score21[2]=='7') or (Score21[2]=='8') or (Score21[2]=='9'):
                if (int(Score21[2])<=(1+y11)):
                    y11=y1p1=int(Score21[2])
            else:
                y11=y1p1
        else:
            y11=y1p1
        try:
            f= open('D:\\TeamData.txt', 'a') 
            if (f.writable()==True):
        #with open('D:\\TeamData.txt', 'a') as f:
                f.write('\nI1    '+ Team1name1[:3]+'    '+Team2name1[:3]+'    '+ str(x11)+'    '+str(y11))
        except:
            pass
        time.sleep(0.3)  
#####################################################################################

    elif (var[1]=='G'):
        frameTime1 = frame1[110:180, 285:460]
        frameTeam1_name1 = frame1[110:180, 470:630]
        frameTeam2_name1 = frame1[110:180, 660:800]
        frame_Score11= frame1[185:315, 475:620]
        frame_Score21= frame1[185:315, 675:820]
        Game_Time1= pytesseract.image_to_string(frameTime1)
        Game_Time1=Game_Time1.rstrip('\n')
        Game_Time1=Game_Time1+"AAA"
        Team1name1 = pytesseract.image_to_string(frameTeam1_name1)
        Team1name1=Team1name1.rstrip('\n')# removing /n to add data after
        Team1name1=Team1name1+'1___'# adding data after that in case there is nothing to read 
        Team2name1 = pytesseract.image_to_string(frameTeam2_name1)
        Team2name1=Team2name1.rstrip('\n')
        Team2name1=Team2name1+'1___'
        Score11=pytesseract.image_to_string(frame_Score11, config=("-c tessedit"
                  "_char_whitelist=abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"
                  " --psm 10"
                  " -l osd"
                  " "))
        Score11=Score11.rstrip('\n')# Removing /n from data 
        Score11=Score11+"AAA"
        Score21=pytesseract.image_to_string(frame_Score21, config=("-c tessedit"
                  "_char_whitelist=abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"
                  " --psm 10"
                  " -l osd"
                  " "))
        Score21=Score21.rstrip('\n')# Removing /n from data 
        Score21=Score21+"AAA"

    #///////////////////////////////////////////////////////////////
    # Showing Time of the Match
        Char1_Time1= Game_Time1[:1] 
        Char2_Time1=Game_Time1[1:2] 
        Char3_Time1=Game_Time1[2:3]
        Char1_2_Time1= Game_Time1[:2] 
        if  (Char1_Time1 =='0') or (Char1_Time1 =='1') or (Char1_Time1=='2') or (Char1_Time1=='3') or (Char1_Time1=='4') or (Char1_Time1=='5') or (Char1_Time1=='6') or (Char1_Time1=='7')or (Char1_Time1=='8') or (Char1_Time1=='9'):
            if (Char2_Time1 =='0') or (Char2_Time1 =='1') or (Char2_Time1=='2') or (Char2_Time1=='3') or (Char2_Time1=='4') or (Char2_Time1=='5') or (Char2_Time1=='6') or (Char2_Time1=='7')or (Char2_Time1=='8') or (Char2_Time1=='9'):
                MatchTime1=MatchTime_prev1=int(Char1_2_Time1)
                f1=1
        else:
            MatchTime1=MatchTime_prev1
            f1=0

        if (Team1name1[3]!='1'):
            Team1name1= Team1name_prev1
        else:
            if (f1==1):
                Team1name_prev1=Team1name1[:3]
            else:
                Team1name1= Team1name_prev1

        if (Team2name1[3]!='1'):
            Team2name1= Team2name_prev1
        else:
            if (f1==1):
                Team2name_prev1=Team2name1[:3]
            else:
                Team2name1= Team2name_prev1

        if (Score11[0]=='0') or (Score11[0]=='1') or (Score11[0]=='2') or (Score11[0]=='3') or (Score11[0]=='4') or (Score11[0]=='5') or (Score11[0]=='6') or (Score11[0]=='7') or (Score11[0]=='8') or (Score11[0]=='9'):
            if (int(Score11[0])<=(1+x11)):
                x11=x1p1=int(Score11[0])
        elif (Score11[0]=='l'):
            if (x11<=1):
                x11=x1p1=1
        else:
            x11=x1p1
   


        if (Score21[0]=='0') or (Score21[0]=='1') or (Score21[0]=='2') or (Score21[0]=='3') or (Score21[0]=='4') or (Score21[0]=='5') or (Score21[0]=='6') or (Score21[0]=='7') or (Score21[0]=='8') or (Score21[0]=='9'):
            if (int(Score21[0])<=(1+y11)):
                y11=y1p1=int(Score21[0])
        elif (Score21[0]=='l'):
            if (y11<=1):
                y11=y1p1=1
        else:
            y11=y1p1
        try:
            f= open('D:\\TeamData.txt', 'a') 
            if (f.writable()==True):
        #with open('D:\\TeamData.txt', 'a') as f:
                f.write('\nG1    '+ Team1name1[:3]+'    '+Team2name1[:3]+'    '+ str(x11)+'    '+str(y11))
        except:
            pass
        time.sleep(0.3)        
    
    elif (var[1]=='F'):
        frameTime1 = frame1[145:240, 200:445]
        frameTeam1_name1 = frame1[145:240, 500:820]
        frameTeam2_name1 = frame1[145:240, 1210:1570]
        frame_Score11= frame1[135:245,500:950]
        frame_Score21= frame1[135:245,1100:1570]
        Game_Time1= pytesseract.image_to_string(frameTime1)
        Game_Time1=Game_Time1.rstrip('\n')
        Game_Time1=Game_Time1+"AAA"
        Team1name1 = pytesseract.image_to_string(frameTeam1_name1)
        Team1name1=Team1name1.rstrip('\n')# removing /n to add data after
        Team1name1=Team1name1+'1___'# adding data after that in case there is nothing to read 
        Team2name1 = pytesseract.image_to_string(frameTeam2_name1)
        Team2name1=Team2name1.rstrip('\n')
        Team2name1=Team2name1+'1___'
        Score11=pytesseract.image_to_string(frame_Score11)
        Score11=Score11.rstrip('\n')# Removing /n from data 
        Score11='A'+Score11
        Score21=pytesseract.image_to_string(frame_Score21)
        Score21=Score21.rstrip('\n')# Removing /n from data 
        Score21=Score21+"AAA"

    #//////////////////////////////////////////////////////
    # Time of the game
        Char1_Time1= Game_Time1[:1] 
        Char2_Time1=Game_Time1[1:2] 
        Char3_Time1=Game_Time1[2:3]
        Char1_2_Time1= Game_Time1[:2] 
        if  (Char1_Time1 =='0') or (Char1_Time1 =='1') or (Char1_Time1=='2') or (Char1_Time1=='3') or (Char1_Time1=='4') or (Char1_Time1=='5') or (Char1_Time1=='6') or (Char1_Time1=='7')or (Char1_Time1=='8') or (Char1_Time1=='9'):
            if (Char2_Time1 =='0') or (Char2_Time1 =='1') or (Char2_Time1=='2') or (Char2_Time1=='3') or (Char2_Time1=='4') or (Char2_Time1=='5') or (Char2_Time1=='6') or (Char2_Time1=='7')or (Char2_Time1=='8') or (Char2_Time1=='9'):
                MatchTime1=MatchTime_prev1=int(Char1_2_Time1)
                f1=1
        else:
            MatchTime1=MatchTime_prev1
            f1=0

        if (Team1name1[0]=='1'):
            Team1name1= Team1name_prev1
        else:
            if (f1==1):
                Team1name_prev1=Team1name1[:3]
            else:
                Team1name1= Team1name_prev1

        if (Team2name1[0]=='1'):
            Team2name1= Team2name_prev1
        else:
            if (f1==1):
                Team2name_prev1=Team2name1[:3]
            else:
                Team2name1= Team2name_prev1

    
        if (Score11[-1]=='0') or (Score11[-1]=='1') or (Score11[-1]=='2') or (Score11[-1]=='3') or (Score11[-1]=='4') or (Score11[-1]=='5') or (Score11[-1]=='6') or (Score11[-1]=='7') or (Score11[-1]=='8') or (Score11[-1]=='9'):
            if (int(Score11[-1])<=(1+x11)):
                x11=x1p1=int(Score11[-1])

        elif(Score11[-1]=='G'):
             if ((x11<=4) and (x11>2)):
                x11=x1p1=4
        else:
            x11=x1p1
   
        if (Score21[0]=='0') or (Score21[0]=='1') or (Score21[0]=='2') or (Score21[0]=='3') or (Score21[0]=='4') or (Score21[0]=='5') or (Score21[0]=='6') or (Score21[0]=='7') or (Score21[0]=='8') or (Score21[0]=='9'):
            if (int(Score21[0])<=(1+y11)):
                y11=y1p1=int(Score21[0])

        elif(Score21[0]=='G'):
            if ((y11<=4) and (y11>2)):
                y11=y1p1=4
        else:
            y11=y1p1
        try:
            f= open('D:\\TeamData.txt', 'a') 
            if (f.writable()==True):
        #with open('D:\\TeamData.txt', 'a') as f:
                f.write('\nF1    '+ Team1name1[:3]+'    '+Team2name1[:3]+'    '+ str(x11)+'    '+str(y11))
        except:
            pass

        time.sleep(0.3)
    elif(var[1]=='R'):
        frameTime1 = frame1[110:180, 200:400]
        frameTeam1_name1 = frame1[110:180, 470:640]
        frameTeam2_name1 = frame1[110:180, 850:1010]
        frame_Score11= frame1[110:180, 660:835]
        frame_Score21= frame1[110:180, 660:835]
        #cv2.imshow('frame',frameTeam1_name)
        Game_Time1= pytesseract.image_to_string(frameTime1)
        Game_Time1=Game_Time1.rstrip('\n')
        Game_Tim1=Game_Time1+"AAA"
        Team1name1 = pytesseract.image_to_string(frameTeam1_name1)
        Team1name1=Team1name1.rstrip('\n')# removing /n to add data after
        Team1name1=Team1name1+'1___'# adding data after that in case there is nothing to read 
        Team2name1 = pytesseract.image_to_string(frameTeam2_name1)
        Team2name1=Team2name1.rstrip('\n')
        Team2name1=Team2name1+'1___'
        Score11=pytesseract.image_to_string(frame_Score11)
        Score11=Score11.rstrip('\n')# Removing /n from data 
        Score11=Score11+"AAA"
        Score21=pytesseract.image_to_string(frame_Score21)
        Score21=Score21.rstrip('\n')# Removing /n from data 
        Score21=Score21+"AAA"

    # Showing Time of the Match
        Char1_Time1= Game_Time1[:1] 
        Char2_Time1=Game_Time1[1:2] 
        Char3_Time1=Game_Time1[2:3]
        Char1_2_Time1= Game_Time1[:2] 
        if  (Char1_Time1 =='0') or (Char1_Time1 =='1') or (Char1_Time1=='2') or (Char1_Time1=='3') or (Char1_Time1=='4') or (Char1_Time1=='5') or (Char1_Time1=='6') or (Char1_Time1=='7')or (Char1_Time1=='8') or (Char1_Time1=='9'):
            if (Char2_Time1 =='0') or (Char2_Time1 =='1') or (Char2_Time1=='2') or (Char2_Time1=='3') or (Char2_Time1=='4') or (Char2_Time1=='5') or (Char2_Time1=='6') or (Char2_Time1=='7')or (Char2_Time1=='8') or (Char2_Time1=='9'):
                MatchTime1=MatchTime_prev1=int(Char1_2_Time1)
                f1=1
        else:
            MatchTime1=MatchTime_prev1
            f1=0
    #Showing the Name of the Teams
        if (Team1name1[3]!='1'):
            Team1name1= Team1name_prev1
        else:
            if (f1==1):
                Team1name_prev1=Team1name1[:3]
            else:
                Team1name1= Team1name_prev1

        if (Team2name1[3]!='1'):
            Team2name1= Team2name_prev1
        else:
            if (f1==1):
                Team2name_prev1=Team2name1[:3]
            else:
                Team2name1= Team2name_prev1

    # Showing the Scores:
        if (Score11[0]=='0') or (Score11[0]=='1') or (Score11[0]=='2') or (Score11[0]=='3') or (Score11[0]=='4') or (Score11[0]=='5') or (Score11[0]=='6') or (Score11[0]=='7') or (Score11[0]=='8') or (Score11[0]=='9'):
            if (int(Score11[0])<=(1+x11)):
                x11=x1p1=int(Score11[0])
        else:
            x11=x1p1
   
        if (Score21[2]=='0') or (Score21[2]=='1') or (Score21[2]=='2') or (Score21[2]=='3') or (Score21[2]=='4') or (Score21[2]=='5') or (Score21[2]=='6') or (Score21[2]=='7') or (Score21[2]=='8') or (Score21[2]=='9'):
            if (int(Score21[2])<=(1+y11)):
                y11=y1p1=int(Score21[2])
        else:
            y11=y1p1
        try:
            f= open('D:\\TeamData.txt', 'a') 
            if (f.writable()==True):
        #with open('D:\\TeamData.txt', 'a') as f:
                f.write('\nR1    '+ Team1name1[:3]+'    '+Team2name1[:3]+'    '+ str(x11)+'    '+str(y11))
        except:
            pass
        time.sleep(0.3)
    else:
        pass

########################################################################################################################################

    if (var[2]=='E'):
        frameTime2 = frame2[280:350, 420:615]
        frameTeam1_name2 = frame2[205:270, 230:390]
        frameTeam2_name2 = frame2[205:270, 630:815]
        frame_Score12= frame2[210:345, 440:585]
        frame_Score22= frame2[210:345, 440:585]
        #cv2.imshow('frame',frameTeam1_name)
        Game_Time2= pytesseract.image_to_string(frameTime2)
        Game_Time2=Game_Time2.rstrip('\n')
        Game_Tim2=Game_Time2+"AAA"
        Team1name2 = pytesseract.image_to_string(frameTeam1_name2)
        Team1name2=Team1name2.rstrip('\n')# removing /n to add data after
        Team1name2=Team1name2+'1___'# adding data after that in case there is nothing to read 
        Team2name2 = pytesseract.image_to_string(frameTeam2_name2)
        Team2name2=Team2name2.rstrip('\n')
        Team2name2=Team2name2+'1___'
        Score12=pytesseract.image_to_string(frame_Score12)
        Score12=Score12.rstrip('\n')# Removing /n from data 
        Score12=Score12+"AAA"
        Score22=pytesseract.image_to_string(frame_Score22)
        Score22=Score22.rstrip('\n')# Removing /n from data 
        Score22=Score22+"AAA"
    # Showing Time of the Match
        Char1_Time2= Game_Time2[:1] 
        Char2_Time2=Game_Time2[1:2] 
        Char3_Time2=Game_Time2[2:3]
        Char1_2_Time2= Game_Time2[:2] 
        if  (Char1_Time2 =='0') or (Char1_Time2 =='1') or (Char1_Time2=='2') or (Char1_Time2=='3') or (Char1_Time2=='4') or (Char1_Time2=='5') or (Char1_Time2=='6') or (Char1_Time2=='7')or (Char1_Time2=='8') or (Char1_Time2=='9'):
            if (Char2_Time2 =='0') or (Char2_Time2 =='1') or (Char2_Time2=='2') or (Char2_Time2=='3') or (Char2_Time2=='4') or (Char2_Time2=='5') or (Char2_Time2=='6') or (Char2_Time2=='7')or (Char2_Time2=='8') or (Char2_Time2=='9'):
                MatchTime2=MatchTime_prev2=int(Char1_2_Time2)
                f2=1
        else:
            MatchTime2=MatchTime_prev2
            f2=0
    # End Time of the Match
    
    #Showing the Name of the Teams
        if (Team1name2[3]!='1'):
            Team1name2= Team1name_prev2
        else:
            if (f2==1):
                Team1name_prev2=Team1name2[:3]
            else:
                Team1name2= Team1name_prev2

        if (Team2name2[3]!='1'):
            Team2name2= Team2name_prev2
        else:
            if (f2==1):
                Team2name_prev2=Team2name2[:3]
            else:
                Team2name2= Team2name_prev2
 
    # Showing the Scores:
        if (Score12[0]=='0') or (Score12[0]=='1') or (Score12[0]=='2') or (Score12[0]=='3') or (Score12[0]=='4') or (Score12[0]=='5') or (Score12[0]=='6') or (Score12[0]=='7') or (Score12[0]=='8') or (Score12[0]=='9'):
            if (int(Score12[0])<=(1+x12)):
                x12=x1p2=int(Score12[0])
        else:
            x12=x1p2
   
        if (Score22[2]=='0') or (Score22[2]=='1') or (Score22[2]=='2') or (Score22[2]=='3') or (Score22[2]=='4') or (Score22[2]=='5') or (Score22[2]=='6') or (Score22[2]=='7') or (Score22[2]=='8') or (Score22[2]=='9'):
            if (int(Score22[2])<=(1+y12)):
                y12=y1p2=int(Score22[2])
        else:
            y12=y1p2
        try:
            f= open('D:\\TeamData.txt', 'a') 
            if (f.writable()==True):
        #with open('D:\\TeamData.txt', 'a') as f:
                f.write('\nE2    '+ Team1name2[:3]+'    '+Team2name2[:3]+'    '+ str(x12)+'    '+str(y12))
        except:
            pass
        time.sleep(0.3)
        #print ("Current Time: "+ str(MatchTime))
        
    elif (var[2]=='S'):
        frameTime2 = frame2[122:212, 305:560]
        frameTeam1_name2 = frame2[130:190, 575:765]
        frameTeam2_name2 = frame2[130:190, 995:1175]
        frame_Score12= frame2[115:210,780:1165]
        frame_Score22= frame2[115:210,780:1165]
        Game_Time2= pytesseract.image_to_string(frameTime2)
        Game_Time2=Game_Time2.rstrip('\n')
        Game_Tim2=Game_Time2+"AAA"
        Team1name2 = pytesseract.image_to_string(frameTeam1_name2)
        Team1name2=Team1name2.rstrip('\n')# removing /n to add data after
        Team1name2=Team1name2+'1___'# adding data after that in case there is nothing to read 
        Team2name2 = pytesseract.image_to_string(frameTeam2_name2)
        Team2name2=Team2name2.rstrip('\n')
        Team2name2=Team2name2+'1___'
        Score12=pytesseract.image_to_string(frame_Score12)
        Score12=Score12.rstrip('\n')# Removing /n from data 
        Score12=Score12+"AAA"
        Score22=pytesseract.image_to_string(frame_Score22)
        Score22=Score22.rstrip('\n')# Removing /n from data 
        Score22=Score22+"AAA"
    # Showing Time of the Match
        Char1_Time2= Game_Time2[:1] 
        Char2_Time2=Game_Time2[1:2] 
        Char3_Time2=Game_Time2[2:3]
        Char1_2_Time2= Game_Time2[:2] 
        if  (Char1_Time2 =='0') or (Char1_Time2 =='1') or (Char1_Time2=='2') or (Char1_Time2=='3') or (Char1_Time2=='4') or (Char1_Time2=='5') or (Char1_Time2=='6') or (Char1_Time2=='7')or (Char1_Time2=='8') or (Char1_Time2=='9'):
            if (Char2_Time2 =='0') or (Char2_Time2 =='1') or (Char2_Time2=='2') or (Char2_Time2=='3') or (Char2_Time2=='4') or (Char2_Time2=='5') or (Char2_Time2=='6') or (Char2_Time2=='7')or (Char2_Time2=='8') or (Char2_Time2=='9'):
                MatchTime2=MatchTime_prev2=int(Char1_2_Time2)
                f2=1
        else:
            MatchTime2=MatchTime_prev2
            f2=0
    # End Time of the Match
    
    #Showing the Name of the Teams
        if (Team1name2[3]!='1'):
            Team1name2= Team1name_prev2
        else:
            if (f2==1):
                Team1name_prev2=Team1name2[:3]
            else:
                Team1name2= Team1name_prev2

        if (Team2name2[3]!='1'):
            Team2name2= Team2name_prev2
        else:
            if (f2==1):
                Team2name_prev2=Team2name2[:3]
            else:
                Team2name2= Team2name_prev2
 
    # Showing the Scores:
        if (Score12[0]=='0') or (Score12[0]=='1') or (Score12[0]=='2') or (Score12[0]=='3') or (Score12[0]=='4') or (Score12[0]=='5') or (Score12[0]=='6') or (Score12[0]=='7') or (Score12[0]=='8') or (Score12[0]=='9'):
            if (int(Score12[0])<=(1+x12)):
                x12=x1p2=int(Score12[0])
        else:
            x12=x1p2
   
        if (Score22[2]=='0') or (Score22[2]=='1') or (Score22[2]=='2') or (Score22[2]=='3') or (Score22[2]=='4') or (Score22[2]=='5') or (Score22[2]=='6') or (Score22[2]=='7') or (Score22[2]=='8') or (Score22[2]=='9'):
            if (int(Score22[2])<=(1+y12)):
                y12=y1p2=int(Score22[2])
        else:
            y12=y1p2
        try:
            f= open('D:\\TeamData.txt', 'a') 
            if (f.writable()==True):
        #with open('D:\\TeamData.txt', 'a') as f:
                f.write('\nS2    '+ Team1name2[:3]+'    '+Team2name2[:3]+'    '+ str(x12)+'    '+str(y12))
        except:
            pass
        time.sleep(0.3)

    ##############################################################
    elif (var[2]=='I'):
        frameTime2 = frame2[130:215, 1180:1370]
        frameTeam1_name2 = frame2[130:220, 330:540]
        frameTeam2_name2 = frame2[130:220, 930:1100]
        frame_Score12= frame2[130:210, 650:800]
        frame_Score22= frame2[130:210, 650:800]
        Game_Time2= pytesseract.image_to_string(frameTime2)
        Game_Time2=Game_Time2.rstrip('\n')
        Game_Tim2=Game_Time2+"AAA"
        Team1name2 = pytesseract.image_to_string(frameTeam1_name2)
        Team1name2=Team1name2.rstrip('\n')# removing /n to add data after
        Team1name2=Team1name2+'1___'# adding data after that in case there is nothing to read 
        Team2name2 = pytesseract.image_to_string(frameTeam2_name2)
        Team2name2=Team2name2.rstrip('\n')
        Team2name2=Team2name2+'1___'
        Score12=pytesseract.image_to_string(frame_Score12)
        Score12=Score12.rstrip('\n')# Removing /n from data 
        Score12=Score12+"AAA"
        Score22=pytesseract.image_to_string(frame_Score22)
        Score22=Score22.rstrip('\n')# Removing /n from data 
        Score22=Score22+"AAA"

        Char1_Time2= Game_Time2[:1] 
        Char2_Time2=Game_Time2[1:2] 
        Char3_Time2=Game_Time2[2:3]
        Char1_2_Time2= Game_Time2[:2] 
        fp2=f2
        if  (Char1_Time2 =='0') or (Char1_Time2 =='1') or (Char1_Time2=='2') or (Char1_Time2=='3') or (Char1_Time2=='4') or (Char1_Time2=='5') or (Char1_Time2=='6') or (Char1_Time2=='7')or (Char1_Time2=='8') or (Char1_Time2=='9'):
            if (Char2_Time2 =='0') or (Char2_Time2 =='1') or (Char2_Time2=='2') or (Char2_Time2=='3') or (Char2_Time2=='4') or (Char2_Time2=='5') or (Char2_Time2=='6') or (Char2_Time2=='7')or (Char2_Time2=='8') or (Char2_Time2=='9'):
                MatchTime2=MatchTime_prev2=int(Char1_2_Time2)
                f2=1
        else:
            MatchTime2=MatchTime_prev2
            f2=0
       

        if (Team1name2[3]!='1'):
            Team1name2= Team1name_prev2
        else:
            if (f2==1):  
                Team1name_prev2=Team1name2[:3]    
            else:
                Team1name2= Team1name_prev2

        if (Team2name2[3]!='1'):
            Team2name2= Team2name_prev2
        else:
            if (f2==1):
                Team2name_prev2=Team2name2[:3]
            else:
                Team2name2= Team2name_prev2

       
    # End Name of the teams

    # Showing the Scores:
        if (f2==1):
            if (Score12[0]=='0') or (Score12[0]=='1') or (Score12[0]=='2') or (Score12[0]=='3') or (Score12[0]=='4') or (Score12[0]=='5') or (Score12[0]=='6') or (Score12[0]=='7') or (Score12[0]=='8') or (Score12[0]=='9'):
                if (int(Score12[0])<=(1+x12)):
                    x12=x1p2=int(Score12[0])
            else:
                x12=x1p2
        else:
            x12=x1p2
   

        if (f2==1):
            if (Score22[2]=='0') or (Score22[2]=='1') or (Score22[2]=='2') or (Score22[2]=='3') or (Score22[2]=='4') or (Score22[2]=='5') or (Score22[2]=='6') or (Score22[2]=='7') or (Score22[2]=='8') or (Score22[2]=='9'):
                if (int(Score22[2])<=(1+y12)):
                    y12=y1p2=int(Score22[2])
            else:
                y12=y1p2
        else:
            y12=y1p2
        try:
            f= open('D:\\TeamData.txt', 'a') 
            if (f.writable()==True):
        #with open('D:\\TeamData.txt', 'a') as f:
                f.write('\nI2    '+ Team1name2[:3]+'    '+Team2name2[:3]+'    '+ str(x12)+'    '+str(y12))
        except:
            pass
        time.sleep(0.3)

#########################################################################
    elif (var[2]=='G'):
        frameTime2 = frame2[110:180, 285:460]
        frameTeam1_name2 = frame2[110:180, 470:630]
        frameTeam2_name2 = frame2[110:180, 660:800]
        frame_Score12= frame2[185:315, 475:620]
        frame_Score22= frame2[185:315, 675:820]
        Game_Time2= pytesseract.image_to_string(frameTime2)
        Game_Time2=Game_Time2.rstrip('\n')
        Game_Time2=Game_Time2+"AAA"
        Team1name2 = pytesseract.image_to_string(frameTeam1_name2)
        Team1name2=Team1name2.rstrip('\n')# removing /n to add data after
        Team1name2=Team1name2+'1___'# adding data after that in case there is nothing to read 
        Team2name2 = pytesseract.image_to_string(frameTeam2_name2)
        Team2name2=Team2name2.rstrip('\n')
        Team2name2=Team2name2+'1___'
        Score12=pytesseract.image_to_string(frame_Score12, config=("-c tessedit"
                  "_char_whitelist=abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"
                  " --psm 10"
                  " -l osd"
                  " "))
        Score12=Score12.rstrip('\n')# Removing /n from data 
        Score12=Score12+"AAA"
        Score22=pytesseract.image_to_string(frame_Score22, config=("-c tessedit"
                  "_char_whitelist=abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"
                  " --psm 10"
                  " -l osd"
                  " "))
        Score22=Score22.rstrip('\n')# Removing /n from data 
        Score22=Score22+"AAA"

    #///////////////////////////////////////////////////////////////
    # Showing Time of the Match
        Char1_Time2= Game_Time2[:1] 
        Char2_Time2=Game_Time2[1:2] 
        Char3_Time2=Game_Time2[2:3]
        Char1_2_Time2= Game_Time2[:2] 
        if  (Char1_Time2 =='0') or (Char1_Time2 =='1') or (Char1_Time2=='2') or (Char1_Time2=='3') or (Char1_Time2=='4') or (Char1_Time2=='5') or (Char1_Time2=='6') or (Char1_Time2=='7')or (Char1_Time2=='8') or (Char1_Time2=='9'):
            if (Char2_Time2 =='0') or (Char2_Time2 =='1') or (Char2_Time2=='2') or (Char2_Time2=='3') or (Char2_Time2=='4') or (Char2_Time2=='5') or (Char2_Time2=='6') or (Char2_Time2=='7')or (Char2_Time2=='8') or (Char2_Time2=='9'):
                MatchTime2=MatchTime_prev2=int(Char1_2_Time2)
                f2=1
        else:
            MatchTime2=MatchTime_prev2
            f2=0

        if (Team1name2[3]!='1'):
            Team1name2= Team1name_prev2
        else:
            if (f2==1):
                Team1name_prev2=Team1name2[:3]
            else:
                Team1name2= Team1name_prev2

        if (Team2name2[3]!='1'):
            Team2name2= Team2name_prev2
        else:
            if (f2==1):
                Team2name_prev2=Team2name2[:3]
            else:
                Team2name2= Team2name_prev2

        if (Score12[0]=='0') or (Score12[0]=='1') or (Score12[0]=='2') or (Score12[0]=='3') or (Score12[0]=='4') or (Score12[0]=='5') or (Score12[0]=='6') or (Score12[0]=='7') or (Score12[0]=='8') or (Score12[0]=='9'):
            if (int(Score12[0])<=(1+x12)):
                x12=x1p2=int(Score12[0])
        elif (Score12[0]=='l'):
            if (x12<=1):
                x12=x1p2=1
        else:
            x12=x1p2
   


        if (Score22[0]=='0') or (Score22[0]=='1') or (Score22[0]=='2') or (Score22[0]=='3') or (Score22[0]=='4') or (Score22[0]=='5') or (Score22[0]=='6') or (Score22[0]=='7') or (Score22[0]=='8') or (Score22[0]=='9'):
            if (int(Score22[0])<=(1+y12)):
                y12=y1p2=int(Score22[0])
        elif (Score22[0]=='l'):
            if (y12<=1):
                y12=y1p2=1
        else:
            y12=y1p2
        try:
            f= open('D:\\TeamData.txt', 'a') 
            if (f.writable()==True):
        #with open('D:\\TeamData.txt', 'a') as f:
                f.write('\nG2    '+ Team1name2[:3]+'    '+Team2name2[:3]+'    '+ str(x12)+'    '+str(y12))
        except:
            pass
        time.sleep(0.3)

    elif (var[2]=='F'):
        frameTime2 = frame2[145:240, 200:445]
        frameTeam1_name2 = frame2[145:240, 500:820]
        frameTeam2_name2 = frame2[145:240, 1210:1570]
        frame_Score12= frame2[135:245,500:950]
        frame_Score22= frame2[135:245,1100:1570]
        Game_Time2= pytesseract.image_to_string(frameTime2)
        Game_Time2=Game_Time2.rstrip('\n')
        Game_Time2=Game_Time2+"AAA"
        Team1name2 = pytesseract.image_to_string(frameTeam1_name2)
        Team1name2=Team1name2.rstrip('\n')# removing /n to add data after
        Team1name2=Team1name2+'1___'# adding data after that in case there is nothing to read 
        Team2name2 = pytesseract.image_to_string(frameTeam2_name2)
        Team2name2=Team2name2.rstrip('\n')
        Team2name2=Team2name2+'1___'
        Score12=pytesseract.image_to_string(frame_Score12)
        Score12=Score12.rstrip('\n')# Removing /n from data 
        Score12='A'+Score12
        Score22=pytesseract.image_to_string(frame_Score22)
        Score22=Score22.rstrip('\n')# Removing /n from data 
        Score22=Score22+"AAA"

    #//////////////////////////////////////////////////////
    # Time of the game
        Char1_Time2= Game_Time2[:1] 
        Char2_Time2=Game_Time2[1:2] 
        Char3_Time2=Game_Time2[2:3]
        Char1_2_Time2= Game_Time2[:2] 
        if  (Char1_Time2 =='0') or (Char1_Time2 =='1') or (Char1_Time2=='2') or (Char1_Time2=='3') or (Char1_Time2=='4') or (Char1_Time2=='5') or (Char1_Time2=='6') or (Char1_Time2=='7')or (Char1_Time2=='8') or (Char1_Time2=='9'):
            if (Char2_Time2 =='0') or (Char2_Time2 =='1') or (Char2_Time2=='2') or (Char2_Time2=='3') or (Char2_Time2=='4') or (Char2_Time2=='5') or (Char2_Time2=='6') or (Char2_Time2=='7')or (Char2_Time2=='8') or (Char2_Time2=='9'):
                MatchTime2=MatchTime_prev2=int(Char1_2_Time2)
                f2=1
        else:
            MatchTime2=MatchTime_prev2
            f2=0

        if (Team1name2[0]=='1'):
            Team1name2= Team1name_prev2
        else:
            if (f2==1):
                Team1name_prev2=Team1name2[:3]
            else:
                Team1name2= Team1name_prev2

        if (Team2name2[0]=='1'):
            Team2name2= Team2name_prev2
        else:
            if (f2==1):
                Team2name_prev2=Team2name2[:3]
            else:
                Team2name2= Team2name_prev2

    
        if (Score12[-1]=='0') or (Score12[-1]=='1') or (Score12[-1]=='2') or (Score12[-1]=='3') or (Score12[-1]=='4') or (Score12[-1]=='5') or (Score12[-1]=='6') or (Score12[-1]=='7') or (Score12[-1]=='8') or (Score12[-1]=='9'):
            if (int(Score12[-1])<=(1+x12)):
                x12=x1p2=int(Score12[-1])

        elif(Score12[-1]=='G'):
             if ((x12<=4) and (x12>2)):
                x12=x1p2=4
        else:
            x12=x1p2
   
        if (Score22[0]=='0') or (Score22[0]=='1') or (Score22[0]=='2') or (Score22[0]=='3') or (Score22[0]=='4') or (Score22[0]=='5') or (Score22[0]=='6') or (Score22[0]=='7') or (Score22[0]=='8') or (Score22[0]=='9'):
            if (int(Score22[0])<=(1+y12)):
                y12=y1p2=int(Score22[0])

        elif(Score22[0]=='G'):
            if ((y12<=4) and (y12>2)):
                y12=y1p2=4
        else:
            y12=y1p2
        try:
            f= open('D:\\TeamData.txt', 'a') 
            if (f.writable()==True):
        #with open('D:\\TeamData.txt', 'a') as f:
                f.write('\nF2    '+ Team1name2[:3]+'    '+Team2name2[:3]+'    '+ str(x12)+'    '+str(y12))
        except:
            pass

        time.sleep(0.3)

    elif (var[2]=='R'):
        frameTime2 = frame2[110:180, 200:400]
        frameTeam1_name2 = frame2[110:180, 470:640]
        frameTeam2_name2 = frame2[110:180, 850:1010]
        frame_Score12= frame2[110:180, 660:835]
        frame_Score22= frame2[110:180, 660:835]
        #cv2.imshow('frame',frameTeam1_name)
        Game_Time2= pytesseract.image_to_string(frameTime2)
        Game_Time2=Game_Time2.rstrip('\n')
        Game_Tim2=Game_Time2+"AAA"
        Team1name2 = pytesseract.image_to_string(frameTeam1_name2)
        Team1name2=Team1name2.rstrip('\n')# removing /n to add data after
        Team1name2=Team1name2+'1___'# adding data after that in case there is nothing to read 
        Team2name2 = pytesseract.image_to_string(frameTeam2_name2)
        Team2name2=Team2name2.rstrip('\n')
        Team2name2=Team2name2+'1___'
        Score12=pytesseract.image_to_string(frame_Score12)
        Score12=Score12.rstrip('\n')# Removing /n from data 
        Score12=Score12+"AAA"
        Score22=pytesseract.image_to_string(frame_Score22)
        Score22=Score22.rstrip('\n')# Removing /n from data 
        Score22=Score22+"AAA"
    # Showing Time of the Match
        Char1_Time2= Game_Time2[:1] 
        Char2_Time2=Game_Time2[1:2] 
        Char3_Time2=Game_Time2[2:3]
        Char1_2_Time2= Game_Time2[:2] 
        if  (Char1_Time2 =='0') or (Char1_Time2 =='1') or (Char1_Time2=='2') or (Char1_Time2=='3') or (Char1_Time2=='4') or (Char1_Time2=='5') or (Char1_Time2=='6') or (Char1_Time2=='7')or (Char1_Time2=='8') or (Char1_Time2=='9'):
            if (Char2_Time2 =='0') or (Char2_Time2 =='1') or (Char2_Time2=='2') or (Char2_Time2=='3') or (Char2_Time2=='4') or (Char2_Time2=='5') or (Char2_Time2=='6') or (Char2_Time2=='7')or (Char2_Time2=='8') or (Char2_Time2=='9'):
                MatchTime2=MatchTime_prev2=int(Char1_2_Time2)
                f2=1
        else:
            MatchTime2=MatchTime_prev2
            f2=0
    # End Time of the Match
    
    #Showing the Name of the Teams
        if (Team1name2[3]!='1'):
            Team1name2= Team1name_prev2
        else:
            if (f2==1):
                Team1name_prev2=Team1name2[:3]
            else:
                Team1name2= Team1name_prev2

        if (Team2name2[3]!='1'):
            Team2name2= Team2name_prev2
        else:
            if (f2==1):
                Team2name_prev2=Team2name2[:3]
            else:
                Team2name2= Team2name_prev2
 
    # Showing the Scores:
        if (Score12[0]=='0') or (Score12[0]=='1') or (Score12[0]=='2') or (Score12[0]=='3') or (Score12[0]=='4') or (Score12[0]=='5') or (Score12[0]=='6') or (Score12[0]=='7') or (Score12[0]=='8') or (Score12[0]=='9'):
            if (int(Score12[0])<=(1+x12)):
                x12=x1p2=int(Score12[0])
        else:
            x12=x1p2
   
        if (Score22[2]=='0') or (Score22[2]=='1') or (Score22[2]=='2') or (Score22[2]=='3') or (Score22[2]=='4') or (Score22[2]=='5') or (Score22[2]=='6') or (Score22[2]=='7') or (Score22[2]=='8') or (Score22[2]=='9'):
            if (int(Score22[2])<=(1+y12)):
                y12=y1p2=int(Score22[2])
        else:
            y12=y1p2
        try:
            f= open('D:\\TeamData.txt', 'a') 
            if (f.writable()==True):
        #with open('D:\\TeamData.txt', 'a') as f:
                f.write('\nR2    '+ Team1name2[:3]+'    '+Team2name2[:3]+'    '+ str(x12)+'    '+str(y12))
        except:
            pass
        time.sleep(0.3)

    else:
        pass

#######################################################################################################################

    if (var[3]=='E'):
        frameTime3 = frame3[280:350, 420:615]
        frameTeam1_name3 = frame3[205:270, 230:390]
        frameTeam2_name3 = frame3[205:270, 630:815]
        frame_Score13= frame3[210:345, 440:585]
        frame_Score23= frame3[210:345, 440:585]
        #cv2.imshow('frame',frameTeam1_name)
        Game_Time3= pytesseract.image_to_string(frameTime3)
        Game_Time3=Game_Time3.rstrip('\n')
        Game_Tim3=Game_Time3+"AAA"
        Team1name3 = pytesseract.image_to_string(frameTeam1_name3)
        Team1name3=Team1name3.rstrip('\n')# removing /n to add data after
        Team1name3=Team1name3+'1___'# adding data after that in case there is nothing to read 
        Team2name3 = pytesseract.image_to_string(frameTeam2_name3)
        Team2name3=Team2name3.rstrip('\n')
        Team2name3=Team2name3+'1___'
        Score13=pytesseract.image_to_string(frame_Score13)
        Score13=Score13.rstrip('\n')# Removing /n from data 
        Score13=Score13+"AAA"
        Score23=pytesseract.image_to_string(frame_Score23)
        Score23=Score23.rstrip('\n')# Removing /n from data 
        Score23=Score23+"AAA"
    # Showing Time of the Match
        Char1_Time3= Game_Time3[:1] 
        Char2_Time3=Game_Time3[1:2] 
        Char3_Time3=Game_Time3[2:3]
        Char1_2_Time3= Game_Time3[:2] 
        if  (Char1_Time3 =='0') or (Char1_Time3 =='1') or (Char1_Time3=='2') or (Char1_Time3=='3') or (Char1_Time3=='4') or (Char1_Time3=='5') or (Char1_Time3=='6') or (Char1_Time3=='7')or (Char1_Time3=='8') or (Char1_Time3=='9'):
            if (Char2_Time3 =='0') or (Char2_Time3 =='1') or (Char2_Time3=='2') or (Char2_Time3=='3') or (Char2_Time3=='4') or (Char2_Time3=='5') or (Char2_Time3=='6') or (Char2_Time3=='7')or (Char2_Time3=='8') or (Char2_Time3=='9'):
                MatchTime3=MatchTime_prev3=int(Char1_2_Time3)
                f3=1
        else:
            MatchTime3=MatchTime_prev3
            f3=0
    # End Time of the Match
    
    #Showing the Name of the Teams
        if (Team1name3[3]!='1'):
            Team1name3= Team1name_prev3
        else:
            if (f3==1):
                Team1name_prev3=Team1name3[:3]
            else:
                Team1name3= Team1name_prev3

        if (Team2name3[3]!='1'):
            Team2name3= Team2name_prev3
        else:
            if (f3==1):
                Team2name_prev3=Team2name3[:3]
            else:
                Team2name3= Team2name_prev3
 
    # Showing the Scores:
        if (Score13[0]=='0') or (Score13[0]=='1') or (Score13[0]=='2') or (Score13[0]=='3') or (Score13[0]=='4') or (Score13[0]=='5') or (Score13[0]=='6') or (Score13[0]=='7') or (Score13[0]=='8') or (Score13[0]=='9'):
            if (int(Score13[0])<=(1+x13)):
                x13=x1p3=int(Score13[0])
        else:
            x13=x1p3
   
        if (Score23[2]=='0') or (Score23[2]=='1') or (Score23[2]=='2') or (Score23[2]=='3') or (Score23[2]=='4') or (Score23[2]=='5') or (Score23[2]=='6') or (Score23[2]=='7') or (Score23[2]=='8') or (Score23[2]=='9'):
            if (int(Score23[2])<=(1+y13)):
                y13=y1p3=int(Score23[2])
        else:
            y13=y1p3
        try:
            f= open('D:\\TeamData.txt', 'a') 
            if (f.writable()==True):
        #with open('D:\\TeamData.txt', 'a') as f:
                f.write('\nE3    '+ Team1name3[:3]+'    '+Team2name3[:3]+'    '+ str(x13)+'    '+str(y13))
        except:
            pass
        time.sleep(0.3)
        #print ("Current Time: "+ str(MatchTime))
        
    elif (var[3]=='S'):
        frameTime3 = frame3[122:212, 305:560]
        frameTeam1_name3 = frame3[130:190, 575:765]
        frameTeam2_name3 = frame3[130:190, 995:1175]
        frame_Score13= frame3[115:210,780:1165]
        frame_Score23= frame3[115:210,780:1165]
        #cv2.imshow('frame',frame_Score10)
        Game_Time3= pytesseract.image_to_string(frameTime3)
        Game_Time3=Game_Time3.rstrip('\n')
        Game_Tim3=Game_Time3+"AAA"
        Team1name3 = pytesseract.image_to_string(frameTeam1_name3)
        Team1name3=Team1name3.rstrip('\n')# removing /n to add data after
        Team1name3=Team1name3+'1___'# adding data after that in case there is nothing to read 
        Team2name3 = pytesseract.image_to_string(frameTeam2_name3)
        Team2name3=Team2name3.rstrip('\n')
        Team2name3=Team2name3+'1___'
        Score13=pytesseract.image_to_string(frame_Score13)
        Score13=Score13.rstrip('\n')# Removing /n from data 
        Score13=Score13+"AAA"
        Score23=pytesseract.image_to_string(frame_Score23)
        Score23=Score23.rstrip('\n')# Removing /n from data 
        Score23=Score23+"AAA"
    # Showing Time of the Match
        Char1_Time3= Game_Time3[:1] 
        Char2_Time3=Game_Time3[1:2] 
        Char3_Time3=Game_Time3[2:3]
        Char1_2_Time3= Game_Time3[:2] 
        if  (Char1_Time3 =='0') or (Char1_Time3 =='1') or (Char1_Time3=='2') or (Char1_Time3=='3') or (Char1_Time3=='4') or (Char1_Time3=='5') or (Char1_Time3=='6') or (Char1_Time3=='7')or (Char1_Time3=='8') or (Char1_Time3=='9'):
            if (Char2_Time3 =='0') or (Char2_Time3 =='1') or (Char2_Time3=='2') or (Char2_Time3=='3') or (Char2_Time3=='4') or (Char2_Time3=='5') or (Char2_Time3=='6') or (Char2_Time3=='7')or (Char2_Time3=='8') or (Char2_Time3=='9'):
                MatchTime3=MatchTime_prev3=int(Char1_2_Time3)
                f3=1
        else:
            MatchTime3=MatchTime_prev3
            f3=0
    # End Time of the Match
    
    #Showing the Name of the Teams
        if (Team1name3[3]!='1'):
            Team1name3= Team1name_prev3
        else:
            if (f3==1):
                Team1name_prev3=Team1name3[:3]
            else:
                Team1name3= Team1name_prev3

        if (Team2name3[3]!='1'):
            Team2name3= Team2name_prev3
        else:
            if (f3==1):
                Team2name_prev3=Team2name3[:3]
            else:
                Team2name3= Team2name_prev3
 
    # Showing the Scores:
        if (Score13[0]=='0') or (Score13[0]=='1') or (Score13[0]=='2') or (Score13[0]=='3') or (Score13[0]=='4') or (Score13[0]=='5') or (Score13[0]=='6') or (Score13[0]=='7') or (Score13[0]=='8') or (Score13[0]=='9'):
            if (int(Score13[0])<=(1+x13)):
                x13=x1p3=int(Score13[0])
        else:
            x13=x1p3
   
        if (Score23[2]=='0') or (Score23[2]=='1') or (Score23[2]=='2') or (Score23[2]=='3') or (Score23[2]=='4') or (Score23[2]=='5') or (Score23[2]=='6') or (Score23[2]=='7') or (Score23[2]=='8') or (Score23[2]=='9'):
            if (int(Score23[2])<=(1+y13)):
                y13=y1p3=int(Score23[2])
        else:
            y13=y1p3
        try:
            f= open('D:\\TeamData.txt', 'a') 
            if (f.writable()==True):
        #with open('D:\\TeamData.txt', 'a') as f:
                f.write('\nS3    '+ Team1name3[:3]+'    '+Team2name3[:3]+'    '+ str(x13)+'    '+str(y13))
        except:
            pass
        time.sleep(0.3)

    ##############################################################
    elif (var[3]=='I'):
        frameTime3 = frame3[130:215, 1180:1370]
        frameTeam1_name3 = frame3[130:220, 330:540]
        frameTeam2_name3 = frame3[130:220, 930:1100]
        frame_Score13= frame3[130:210, 650:800]
        frame_Score23= frame3[130:210, 650:800]
        Game_Time3= pytesseract.image_to_string(frameTime3)
        Game_Time3=Game_Time3.rstrip('\n')
        Game_Tim3=Game_Time3+"AAA"
        Team1name3 = pytesseract.image_to_string(frameTeam1_name3)
        Team1name3=Team1name3.rstrip('\n')# removing /n to add data after
        Team1name3=Team1name3+'1___'# adding data after that in case there is nothing to read 
        Team2name3 = pytesseract.image_to_string(frameTeam2_name3)
        Team2name3=Team2name3.rstrip('\n')
        Team2name3=Team2name3+'1___'
        Score13=pytesseract.image_to_string(frame_Score13)
        Score13=Score13.rstrip('\n')# Removing /n from data 
        Score13=Score13+"AAA"
        Score23=pytesseract.image_to_string(frame_Score23)
        Score23=Score23.rstrip('\n')# Removing /n from data 
        Score23=Score23+"AAA"

        Char1_Time3= Game_Time3[:1] 
        Char2_Time3=Game_Time3[1:2] 
        Char3_Time3=Game_Time3[2:3]
        Char1_2_Time3= Game_Time3[:2] 
        fp3=f3
        if  (Char1_Time3 =='0') or (Char1_Time3 =='1') or (Char1_Time3=='2') or (Char1_Time3=='3') or (Char1_Time3=='4') or (Char1_Time3=='5') or (Char1_Time3=='6') or (Char1_Time3=='7')or (Char1_Time3=='8') or (Char1_Time3=='9'):
            if (Char2_Time3 =='0') or (Char2_Time3 =='1') or (Char2_Time3=='2') or (Char2_Time3=='3') or (Char2_Time3=='4') or (Char2_Time3=='5') or (Char2_Time3=='6') or (Char2_Time3=='7')or (Char2_Time3=='8') or (Char2_Time3=='9'):
                MatchTime3=MatchTime_prev3=int(Char1_2_Time3)
                f3=1
        else:
            MatchTime3=MatchTime_prev3
            f3=0
        

        if (Team1name3[3]!='1'):
            Team1name3= Team1name_prev3
        else:
            if (f3==1):  
                Team1name_prev3=Team1name3[:3]    
            else:
                Team1name3= Team1name_prev3

        if (Team2name3[3]!='1'):
            Team2name3= Team2name_prev3
        else:
            if (f3==1):
                Team2name_prev3=Team2name3[:3]
            else:
                Team2name3= Team2name_prev3

       
    # End Name of the teams

    # Showing the Scores:
        if (f3==1):
            if (Score13[0]=='0') or (Score13[0]=='1') or (Score13[0]=='2') or (Score13[0]=='3') or (Score13[0]=='4') or (Score13[0]=='5') or (Score13[0]=='6') or (Score13[0]=='7') or (Score13[0]=='8') or (Score13[0]=='9'):
                if (int(Score13[0])<=(1+x13)):
                    x13=x1p3=int(Score13[0])
            else:
                x13=x1p3
        else:
            x13=x1p3
   

        if (f3==1):
            if (Score23[2]=='0') or (Score23[2]=='1') or (Score23[2]=='2') or (Score23[2]=='3') or (Score23[2]=='4') or (Score23[2]=='5') or (Score23[2]=='6') or (Score23[2]=='7') or (Score23[2]=='8') or (Score23[2]=='9'):
                if (int(Score23[2])<=(1+y13)):
                    y13=y1p3=int(Score23[2])
            else:
                y13=y1p3
        else:
            y13=y1p3
        try:
            f= open('D:\\TeamData.txt', 'a') 
            if (f.writable()==True):
        #with open('D:\\TeamData.txt', 'a') as f:
                f.write('\nI3    '+ Team1name3[:3]+'    '+Team2name3[:3]+'    '+ str(x13)+'    '+str(y13))
        except:
            pass
        time.sleep(0.3)

#########################################################################
    elif (var[3]=='G'):
        frameTime3 = frame3[110:180, 285:460]
        frameTeam1_name3 = frame3[110:180, 470:630]
        frameTeam2_name3 = frame3[110:180, 660:800]
        frame_Score13= frame3[185:315, 475:620]
        frame_Score23= frame3[185:315, 675:820]
        Game_Time3= pytesseract.image_to_string(frameTime3)
        Game_Time3=Game_Time3.rstrip('\n')
        Game_Time3=Game_Time3+"AAA"
        Team1name3 = pytesseract.image_to_string(frameTeam1_name3)
        Team1name3=Team1name3.rstrip('\n')# removing /n to add data after
        Team1name3=Team1name3+'1___'# adding data after that in case there is nothing to read 
        Team2name3 = pytesseract.image_to_string(frameTeam2_name3)
        Team2name3=Team2name3.rstrip('\n')
        Team2name3=Team2name3+'1___'
        Score13=pytesseract.image_to_string(frame_Score13, config=("-c tessedit"
                  "_char_whitelist=abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"
                  " --psm 10"
                  " -l osd"
                  " "))
        Score13=Score13.rstrip('\n')# Removing /n from data 
        Score13=Score13+"AAA"
        Score23=pytesseract.image_to_string(frame_Score23, config=("-c tessedit"
                  "_char_whitelist=abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"
                  " --psm 10"
                  " -l osd"
                  " "))
        Score23=Score23.rstrip('\n')# Removing /n from data 
        Score23=Score23+"AAA"

    #///////////////////////////////////////////////////////////////
    # Showing Time of the Match
        Char1_Time3= Game_Time3[:1] 
        Char2_Time3=Game_Time3[1:2] 
        Char3_Time3=Game_Time3[2:3]
        Char1_2_Time3= Game_Time3[:2] 
        if  (Char1_Time3 =='0') or (Char1_Time3 =='1') or (Char1_Time3=='2') or (Char1_Time3=='3') or (Char1_Time3=='4') or (Char1_Time3=='5') or (Char1_Time3=='6') or (Char1_Time3=='7')or (Char1_Time3=='8') or (Char1_Time3=='9'):
            if (Char2_Time3 =='0') or (Char2_Time3 =='1') or (Char2_Time3=='2') or (Char2_Time3=='3') or (Char2_Time3=='4') or (Char2_Time3=='5') or (Char2_Time3=='6') or (Char2_Time3=='7')or (Char2_Time3=='8') or (Char2_Time3=='9'):
                MatchTime3=MatchTime_prev3=int(Char1_2_Time3)
                f3=1
        else:
            MatchTime3=MatchTime_prev3
            f3=0

        if (Team1name3[3]!='1'):
            Team1name3= Team1name_prev3
        else:
            if (f3==1):
                Team1name_prev3=Team1name3[:3]
            else:
                Team1name3= Team1name_prev3

        if (Team2name3[3]!='1'):
            Team2name3= Team2name_prev3
        else:
            if (f3==1):
                Team2name_prev3=Team2name3[:3]
            else:
                Team2name3= Team2name_prev3

        if (Score13[0]=='0') or (Score13[0]=='1') or (Score13[0]=='2') or (Score13[0]=='3') or (Score13[0]=='4') or (Score13[0]=='5') or (Score13[0]=='6') or (Score13[0]=='7') or (Score13[0]=='8') or (Score13[0]=='9'):
            if (int(Score13[0])<=(1+x13)):
                x13=x1p3=int(Score13[0])
        elif (Score13[0]=='l'):
            if (x13<=1):
                x13=x1p3=1
        else:
            x13=x1p3
   


        if (Score23[0]=='0') or (Score23[0]=='1') or (Score23[0]=='2') or (Score23[0]=='3') or (Score23[0]=='4') or (Score23[0]=='5') or (Score23[0]=='6') or (Score23[0]=='7') or (Score23[0]=='8') or (Score23[0]=='9'):
            if (int(Score23[0])<=(1+y13)):
                y13=y1p3=int(Score23[0])
        elif (Score23[0]=='l'):
            if (y13<=1):
                y13=y1p3=1
        else:
            y13=y1p3
        try:
            f= open('D:\\TeamData.txt', 'a') 
            if (f.writable()==True):
        #with open('D:\\TeamData.txt', 'a') as f:
                f.write('\nG3    '+ Team1name3[:3]+'    '+Team2name3[:3]+'    '+ str(x13)+'    '+str(y13))
        except:
            pass
        time.sleep(0.3)

    elif (var[3]=='F'):
        frameTime3 = frame3[145:240, 200:445]
        frameTeam1_name3 = frame3[145:240, 500:820]
        frameTeam2_name3 = frame3[145:240, 1210:1570]
        frame_Score13= frame3[135:245,500:950]
        frame_Score23= frame3[135:245,1100:1570]
        Game_Time3= pytesseract.image_to_string(frameTime3)
        Game_Time3=Game_Time3.rstrip('\n')
        Game_Time3=Game_Time3+"AAA"
        Team1name3 = pytesseract.image_to_string(frameTeam1_name3)
        Team1name3=Team1name3.rstrip('\n')# removing /n to add data after
        Team1name3=Team1name3+'1___'# adding data after that in case there is nothing to read 
        Team2name3 = pytesseract.image_to_string(frameTeam2_name3)
        Team2name3=Team2name3.rstrip('\n')
        Team2name3=Team2name3+'1___'
        Score13=pytesseract.image_to_string(frame_Score13)
        Score13=Score13.rstrip('\n')# Removing /n from data 
        Score13='A'+Score13
        Score23=pytesseract.image_to_string(frame_Score23)
        Score23=Score23.rstrip('\n')# Removing /n from data 
        Score23=Score23+"AAA"

    #//////////////////////////////////////////////////////
    # Time of the game
        Char1_Time3= Game_Time3[:1] 
        Char2_Time3=Game_Time3[1:2] 
        Char3_Time3=Game_Time3[2:3]
        Char1_2_Time3= Game_Time3[:2] 
        if  (Char1_Time3 =='0') or (Char1_Time3 =='1') or (Char1_Time3=='2') or (Char1_Time3=='3') or (Char1_Time3=='4') or (Char1_Time3=='5') or (Char1_Time3=='6') or (Char1_Time3=='7')or (Char1_Time3=='8') or (Char1_Time3=='9'):
            if (Char2_Time3 =='0') or (Char2_Time3 =='1') or (Char2_Time3=='2') or (Char2_Time3=='3') or (Char2_Time3=='4') or (Char2_Time3=='5') or (Char2_Time3=='6') or (Char2_Time3=='7')or (Char2_Time3=='8') or (Char2_Time3=='9'):
                MatchTime3=MatchTime_prev3=int(Char1_2_Time3)
                f3=1
        else:
            MatchTime3=MatchTime_prev3
            f3=0

        if (Team1name3[0]=='1'):
            Team1name3= Team1name_prev3
        else:
            if (f3==1):
                Team1name_prev3=Team1name3[:3]
            else:
                Team1name3= Team1name_prev3

        if (Team2name3[0]=='1'):
            Team2name3= Team2name_prev3
        else:
            if (f3==1):
                Team2name_prev3=Team2name3[:3]
            else:
                Team2name3= Team2name_prev3

    
        if (Score13[-1]=='0') or (Score13[-1]=='1') or (Score13[-1]=='2') or (Score13[-1]=='3') or (Score13[-1]=='4') or (Score13[-1]=='5') or (Score13[-1]=='6') or (Score13[-1]=='7') or (Score13[-1]=='8') or (Score13[-1]=='9'):
            if (int(Score13[-1])<=(1+x13)):
                x13=x1p3=int(Score13[-1])

        elif(Score13[-1]=='G'):
             if ((x13<=4) and (x13>2)):
                x13=x1p3=4
        else:
            x13=x1p3
   
        if (Score23[0]=='0') or (Score23[0]=='1') or (Score23[0]=='2') or (Score23[0]=='3') or (Score23[0]=='4') or (Score23[0]=='5') or (Score23[0]=='6') or (Score23[0]=='7') or (Score23[0]=='8') or (Score23[0]=='9'):
            if (int(Score23[0])<=(1+y13)):
                y13=y1p3=int(Score23[0])

        elif(Score23[0]=='G'):
            if ((y13<=4) and (y13>2)):
                y13=y1p3=4
        else:
            y13=y1p3
        try:
            f= open('D:\\TeamData.txt', 'a') 
            if (f.writable()==True):
        #with open('D:\\TeamData.txt', 'a') as f:
                f.write('\nF3    '+ Team1name3[:3]+'    '+Team2name3[:3]+'    '+ str(x13)+'    '+str(y13))
        except:
            pass

        time.sleep(0.3)

    elif (var[3]=='R'):
        frameTime3 = frame3[110:180, 200:400]
        frameTeam1_name3 = frame3[110:180, 470:640]
        frameTeam2_name3 = frame3[110:180, 850:1010]
        frame_Score13= frame3[110:180, 660:835]
        frame_Score23= frame3[110:180, 660:835]
        #cv2.imshow('frame',frameTeam1_name)
        Game_Time3= pytesseract.image_to_string(frameTime3)
        Game_Time3=Game_Time3.rstrip('\n')
        Game_Tim3=Game_Time3+"AAA"
        Team1name3 = pytesseract.image_to_string(frameTeam1_name3)
        Team1name3=Team1name3.rstrip('\n')# removing /n to add data after
        Team1name3=Team1name3+'1___'# adding data after that in case there is nothing to read 
        Team2name3 = pytesseract.image_to_string(frameTeam2_name3)
        Team2name3=Team2name3.rstrip('\n')
        Team2name3=Team2name3+'1___'
        Score13=pytesseract.image_to_string(frame_Score13)
        Score13=Score13.rstrip('\n')# Removing /n from data 
        Score13=Score13+"AAA"
        Score23=pytesseract.image_to_string(frame_Score23)
        Score23=Score23.rstrip('\n')# Removing /n from data 
        Score23=Score23+"AAA"
    # Showing Time of the Match
        Char1_Time3= Game_Time3[:1] 
        Char2_Time3=Game_Time3[1:2] 
        Char3_Time3=Game_Time3[2:3]
        Char1_2_Time3= Game_Time3[:2] 
        if  (Char1_Time3 =='0') or (Char1_Time3 =='1') or (Char1_Time3=='2') or (Char1_Time3=='3') or (Char1_Time3=='4') or (Char1_Time3=='5') or (Char1_Time3=='6') or (Char1_Time3=='7')or (Char1_Time3=='8') or (Char1_Time3=='9'):
            if (Char2_Time3 =='0') or (Char2_Time3 =='1') or (Char2_Time3=='2') or (Char2_Time3=='3') or (Char2_Time3=='4') or (Char2_Time3=='5') or (Char2_Time3=='6') or (Char2_Time3=='7')or (Char2_Time3=='8') or (Char2_Time3=='9'):
                MatchTime3=MatchTime_prev3=int(Char1_2_Time3)
                f3=1
        else:
            MatchTime3=MatchTime_prev3
            f3=0
    # End Time of the Match
    
    #Showing the Name of the Teams
        if (Team1name3[3]!='1'):
            Team1name3= Team1name_prev3
        else:
            if (f3==1):
                Team1name_prev3=Team1name3[:3]
            else:
                Team1name3= Team1name_prev3

        if (Team2name3[3]!='1'):
            Team2name3= Team2name_prev3
        else:
            if (f3==1):
                Team2name_prev3=Team2name3[:3]
            else:
                Team2name3= Team2name_prev3
 
    # Showing the Scores:
        if (Score13[0]=='0') or (Score13[0]=='1') or (Score13[0]=='2') or (Score13[0]=='3') or (Score13[0]=='4') or (Score13[0]=='5') or (Score13[0]=='6') or (Score13[0]=='7') or (Score13[0]=='8') or (Score13[0]=='9'):
            if (int(Score13[0])<=(1+x13)):
                x13=x1p3=int(Score13[0])
        else:
            x13=x1p3
   
        if (Score23[2]=='0') or (Score23[2]=='1') or (Score23[2]=='2') or (Score23[2]=='3') or (Score23[2]=='4') or (Score23[2]=='5') or (Score23[2]=='6') or (Score23[2]=='7') or (Score23[2]=='8') or (Score23[2]=='9'):
            if (int(Score23[2])<=(1+y13)):
                y13=y1p3=int(Score23[2])
        else:
            y13=y1p3
        try:
            f= open('D:\\TeamData.txt', 'a') 
            if (f.writable()==True):
        #with open('D:\\TeamData.txt', 'a') as f:
                f.write('\nR3    '+ Team1name3[:3]+'    '+Team2name3[:3]+'    '+ str(x13)+'    '+str(y13))
        except:
            pass
        time.sleep(0.3)

    else:
        pass
#####################################################################################################################################
    if (var[4]=='E'):
        frameTime4 = frame4[280:350, 420:615]
        frameTeam1_name4 = frame4[205:270, 230:390]
        frameTeam2_name4 = frame4[205:270, 630:815]
        frame_Score14= frame4[210:345, 440:585]
        frame_Score24= frame4[210:345, 440:585]
        #cv2.imshow('frame',frameTeam1_name)
        Game_Time4= pytesseract.image_to_string(frameTime4)
        Game_Time4=Game_Time4.rstrip('\n')
        Game_Tim4=Game_Time4+"AAA"
        Team1name4 = pytesseract.image_to_string(frameTeam1_name4)
        Team1name4=Team1name4.rstrip('\n')# removing /n to add data after
        Team1name4=Team1name4+'1___'# adding data after that in case there is nothing to read 
        Team2name4 = pytesseract.image_to_string(frameTeam2_name4)
        Team2name4=Team2name4.rstrip('\n')
        Team2name4=Team2name4+'1___'
        Score14=pytesseract.image_to_string(frame_Score14)
        Score14=Score14.rstrip('\n')# Removing /n from data 
        Score14=Score14+"AAA"
        Score24=pytesseract.image_to_string(frame_Score24)
        Score24=Score24.rstrip('\n')# Removing /n from data 
        Score24=Score24+"AAA"
    # Showing Time of the Match
        Char1_Time4= Game_Time4[:1] 
        Char2_Time4=Game_Time4[1:2] 
        Char3_Time4=Game_Time4[2:3]
        Char1_2_Time4= Game_Time4[:2] 
        if  (Char1_Time4 =='0') or (Char1_Time4 =='1') or (Char1_Time4=='2') or (Char1_Time4=='3') or (Char1_Time4=='4') or (Char1_Time4=='5') or (Char1_Time4=='6') or (Char1_Time4=='7')or (Char1_Time4=='8') or (Char1_Time4=='9'):
            if (Char2_Time4 =='0') or (Char2_Time4 =='1') or (Char2_Time4=='2') or (Char2_Time4=='3') or (Char2_Time4=='4') or (Char2_Time4=='5') or (Char2_Time4=='6') or (Char2_Time4=='7')or (Char2_Time4=='8') or (Char2_Time4=='9'):
                MatchTime4=MatchTime_prev4=int(Char1_2_Time4)
                f4=1
        else:
            MatchTime4=MatchTime_prev4
            f4=0
    # End Time of the Match
    
    #Showing the Name of the Teams
        if (Team1name4[3]!='1'):
            Team1name4= Team1name_prev4
        else:
            if (f4==1):
                Team1name_prev4=Team1name4[:3]
            else:
                Team1name4= Team1name_prev4

        if (Team2name4[3]!='1'):
            Team2name4= Team2name_prev4
        else:
            if (f4==1):
                Team2name_prev4=Team2name4[:3]
            else:
                Team2name4= Team2name_prev4
 
    # Showing the Scores:
        if (Score14[0]=='0') or (Score14[0]=='1') or (Score14[0]=='2') or (Score14[0]=='3') or (Score14[0]=='4') or (Score14[0]=='5') or (Score14[0]=='6') or (Score14[0]=='7') or (Score14[0]=='8') or (Score14[0]=='9'):
            if (int(Score14[0])<=(1+x14)):
                x14=x1p4=int(Score14[0])
        else:
            x14=x1p4
   
        if (Score24[2]=='0') or (Score24[2]=='1') or (Score24[2]=='2') or (Score24[2]=='3') or (Score24[2]=='4') or (Score24[2]=='5') or (Score24[2]=='6') or (Score24[2]=='7') or (Score24[2]=='8') or (Score24[2]=='9'):
            if (int(Score24[2])<=(1+y14)):
                y14=y1p4=int(Score24[2])
        else:
            y14=y1p4
        try:
            f= open('D:\\TeamData.txt', 'a') 
            if (f.writable()==True):
        #with open('D:\\TeamData.txt', 'a') as f:
                f.write('\nE4    '+ Team1name4[:3]+'    '+Team2name4[:3]+'    '+ str(x14)+'    '+str(y14))
        except:
            pass
        time.sleep(0.3)
        #print ("Current Time: "+ str(MatchTime))
        
    elif(var[4]=='S'):
        frameTime4 = frame4[122:212, 305:560]
        frameTeam1_name4 = frame4[130:190, 575:765]
        frameTeam2_name4 = frame4[130:190, 995:1175]
        frame_Score14= frame4[115:210,780:1165]
        frame_Score24= frame4[115:210,780:1165]
        #cv2.imshow('frame',frame_Score10)
        Game_Time4= pytesseract.image_to_string(frameTime4)
        Game_Time4=Game_Time4.rstrip('\n')
        Game_Tim4=Game_Time4+"AAA"
        Team1name4 = pytesseract.image_to_string(frameTeam1_name4)
        Team1name4=Team1name4.rstrip('\n')# removing /n to add data after
        Team1name4=Team1name4+'1___'# adding data after that in case there is nothing to read 
        Team2name4 = pytesseract.image_to_string(frameTeam2_name4)
        Team2name4=Team2name4.rstrip('\n')
        Team2name4=Team2name4+'1___'
        Score14=pytesseract.image_to_string(frame_Score14)
        Score14=Score14.rstrip('\n')# Removing /n from data 
        Score14=Score14+"AAA"
        Score24=pytesseract.image_to_string(frame_Score24)
        Score24=Score24.rstrip('\n')# Removing /n from data 
        Score24=Score24+"AAA"
    # Showing Time of the Match
        Char1_Time4= Game_Time4[:1] 
        Char2_Time4=Game_Time4[1:2] 
        Char3_Time4=Game_Time4[2:3]
        Char1_2_Time4= Game_Time4[:2] 
        if  (Char1_Time4 =='0') or (Char1_Time4 =='1') or (Char1_Time4=='2') or (Char1_Time4=='3') or (Char1_Time4=='4') or (Char1_Time4=='5') or (Char1_Time4=='6') or (Char1_Time4=='7')or (Char1_Time4=='8') or (Char1_Time4=='9'):
            if (Char2_Time4 =='0') or (Char2_Time4 =='1') or (Char2_Time4=='2') or (Char2_Time4=='3') or (Char2_Time4=='4') or (Char2_Time4=='5') or (Char2_Time4=='6') or (Char2_Time4=='7')or (Char2_Time4=='8') or (Char2_Time4=='9'):
                MatchTime0=MatchTime_prev4=int(Char1_2_Time4)
                f4=1
        else:
            MatchTime4=MatchTime_prev4
            f4=0
    # End Time of the Match
    
    #Showing the Name of the Teams
        if (Team1name4[3]!='1'):
            Team1name4= Team1name_prev4
        else:
            if (f4==1):
                Team1name_prev4=Team1name4[:3]
            else:
                Team1name4= Team1name_prev4

        if (Team2name4[3]!='1'):
            Team2name4= Team2name_prev4
        else:
            if (f4==1):
                Team2name_prev4=Team2name4[:3]
            else:
                Team2name4= Team2name_prev4
 
    # Showing the Scores:
        if (Score14[0]=='0') or (Score14[0]=='1') or (Score14[0]=='2') or (Score14[0]=='3') or (Score14[0]=='4') or (Score14[0]=='5') or (Score14[0]=='6') or (Score14[0]=='7') or (Score14[0]=='8') or (Score14[0]=='9'):
            if (int(Score14[0])<=(1+x14)):
                x14=x1p4=int(Score14[0])
        else:
            x14=x1p4
   
        if (Score24[2]=='0') or (Score24[2]=='1') or (Score24[2]=='2') or (Score24[2]=='3') or (Score24[2]=='4') or (Score24[2]=='5') or (Score24[2]=='6') or (Score24[2]=='7') or (Score24[2]=='8') or (Score24[2]=='9'):
            if (int(Score24[2])<=(1+y14)):
                y14=y1p4=int(Score24[2])
        else:
            y14=y1p4
        try:
            f= open('D:\\TeamData.txt', 'a') 
            if (f.writable()==True):
        #with open('D:\\TeamData.txt', 'a') as f:
                f.write('\nS4    '+ Team1name4[:3]+'    '+Team2name4[:3]+'    '+ str(x14)+'    '+str(y14))
        except:
            pass
        time.sleep(0.3)

    ##############################################################
    elif (var[4]=='I'):
        frameTime4 = frame4[130:215, 1180:1370]
        frameTeam1_name4 = frame4[130:220, 330:540]
        frameTeam2_name4 = frame4[130:220, 930:1100]
        frame_Score14= frame4[130:210, 650:800]
        frame_Score24= frame4[130:210, 650:800]
        Game_Time4= pytesseract.image_to_string(frameTime4)
        Game_Time4=Game_Time4.rstrip('\n')
        Game_Tim4=Game_Time4+"AAA"
        Team1name4 = pytesseract.image_to_string(frameTeam1_name4)
        Team1name4=Team1name4.rstrip('\n')# removing /n to add data after
        Team1name4=Team1name4+'1___'# adding data after that in case there is nothing to read 
        Team2name4 = pytesseract.image_to_string(frameTeam2_name4)
        Team2name4=Team2name4.rstrip('\n')
        Team2name4=Team2name4+'1___'
        Score14=pytesseract.image_to_string(frame_Score14)
        Score14=Score14.rstrip('\n')# Removing /n from data 
        Score14=Score14+"AAA"
        Score24=pytesseract.image_to_string(frame_Score24)
        Score24=Score24.rstrip('\n')# Removing /n from data 
        Score24=Score24+"AAA"

        Char1_Time4= Game_Time4[:1] 
        Char2_Time4=Game_Time4[1:2] 
        Char3_Time4=Game_Time4[2:3]
        Char1_2_Time4= Game_Time4[:2] 
        fp4=f4
        if  (Char1_Time4 =='0') or (Char1_Time4 =='1') or (Char1_Time4=='2') or (Char1_Time4=='3') or (Char1_Time4=='4') or (Char1_Time4=='5') or (Char1_Time4=='6') or (Char1_Time4=='7')or (Char1_Time4=='8') or (Char1_Time4=='9'):
            if (Char2_Time4 =='0') or (Char2_Time4 =='1') or (Char2_Time4=='2') or (Char2_Time4=='3') or (Char2_Time4=='4') or (Char2_Time4=='5') or (Char2_Time4=='6') or (Char2_Time4=='7')or (Char2_Time4=='8') or (Char2_Time4=='9'):
                MatchTime4=MatchTime_prev4=int(Char1_2_Time4)
                f4=1
        else:
            MatchTime4=MatchTime_prev4
            f4=0

        if (Team1name4[3]!='1'):
            Team1name4= Team1name_prev4
        else:
            if (f4==1):  
                Team1name_prev4=Team1name4[:3]    
            else:
                Team1name4= Team1name_prev4

        if (Team2name4[3]!='1'):
            Team2name4= Team2name_prev4
        else:
            if (f4==1):
                Team2name_prev4=Team2name4[:3]
            else:
                Team2name4= Team2name_prev4

       
    # End Name of the teams

    # Showing the Scores:
        if (f4==1):
            if (Score14[0]=='0') or (Score14[0]=='1') or (Score14[0]=='2') or (Score14[0]=='3') or (Score14[0]=='4') or (Score14[0]=='5') or (Score14[0]=='6') or (Score14[0]=='7') or (Score14[0]=='8') or (Score14[0]=='9'):
                if (int(Score14[0])<=(1+x14)):
                    x14=x1p4=int(Score14[0])
            else:
                x14=x1p4
        else:
            x14=x1p4
   

        if (f4==1):
            if (Score24[2]=='0') or (Score24[2]=='1') or (Score24[2]=='2') or (Score24[2]=='3') or (Score24[2]=='4') or (Score24[2]=='5') or (Score24[2]=='6') or (Score24[2]=='7') or (Score24[2]=='8') or (Score24[2]=='9'):
                if (int(Score24[2])<=(1+y14)):
                    y14=y1p4=int(Score24[2])
            else:
                y14=y1p4
        else:
            y14=y1p4
        try:
            f= open('D:\\TeamData.txt', 'a') 
            if (f.writable()==True):
        #with open('D:\\TeamData.txt', 'a') as f:
                f.write('\nI4    '+ Team1name4[:3]+'    '+Team2name4[:3]+'    '+ str(x14)+'    '+str(y14))
        except:
            pass
        time.sleep(0.3)

#########################################################################
    elif (var[4]=='G'):
        frameTime4 = frame4[110:180, 285:460]
        frameTeam1_name4 = frame4[110:180, 470:630]
        frameTeam2_name4 = frame4[110:180, 660:800]
        frame_Score14= frame4[185:315, 475:620]
        frame_Score24= frame4[185:315, 675:820]
        Game_Time4= pytesseract.image_to_string(frameTime4)
        Game_Time4=Game_Time4.rstrip('\n')
        Game_Time4=Game_Time4+"AAA"
        Team1name4 = pytesseract.image_to_string(frameTeam1_name4)
        Team1name4=Team1name4.rstrip('\n')# removing /n to add data after
        Team1name4=Team1name4+'1___'# adding data after that in case there is nothing to read 
        Team2name4 = pytesseract.image_to_string(frameTeam2_name4)
        Team2name4=Team2name4.rstrip('\n')
        Team2name4=Team2name4+'1___'
        Score14=pytesseract.image_to_string(frame_Score14, config=("-c tessedit"
                  "_char_whitelist=abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"
                  " --psm 10"
                  " -l osd"
                  " "))
        Score14=Score14.rstrip('\n')# Removing /n from data 
        Score14=Score14+"AAA"
        Score24=pytesseract.image_to_string(frame_Score24, config=("-c tessedit"
                  "_char_whitelist=abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"
                  " --psm 10"
                  " -l osd"
                  " "))
        Score24=Score24.rstrip('\n')# Removing /n from data 
        Score24=Score24+"AAA"

    #///////////////////////////////////////////////////////////////
    # Showing Time of the Match
        Char1_Time4= Game_Time4[:1] 
        Char2_Time4=Game_Time4[1:2] 
        Char3_Time4=Game_Time4[2:3]
        Char1_2_Time4= Game_Time4[:2] 
        if  (Char1_Time4 =='0') or (Char1_Time4 =='1') or (Char1_Time4=='2') or (Char1_Time4=='3') or (Char1_Time4=='4') or (Char1_Time4=='5') or (Char1_Time4=='6') or (Char1_Time4=='7')or (Char1_Time4=='8') or (Char1_Time4=='9'):
            if (Char2_Time4 =='0') or (Char2_Time4 =='1') or (Char2_Time4=='2') or (Char2_Time4=='3') or (Char2_Time4=='4') or (Char2_Time4=='5') or (Char2_Time4=='6') or (Char2_Time4=='7')or (Char2_Time4=='8') or (Char2_Time4=='9'):
                MatchTime4=MatchTime_prev4=int(Char1_2_Time4)
                f4=1
        else:
            MatchTime4=MatchTime_prev4
            f4=0

        if (Team1name4[3]!='1'):
            Team1name4= Team1name_prev4
        else:
            if (f4==1):
                Team1name_prev4=Team1name4[:3]
            else:
                Team1name4= Team1name_prev4

        if (Team2name4[3]!='1'):
            Team2name4= Team2name_prev4
        else:
            if (f4==1):
                Team2name_prev4=Team2name4[:3]
            else:
                Team2name4= Team2name_prev4

        if (Score14[0]=='0') or (Score14[0]=='1') or (Score14[0]=='2') or (Score14[0]=='3') or (Score14[0]=='4') or (Score14[0]=='5') or (Score14[0]=='6') or (Score14[0]=='7') or (Score14[0]=='8') or (Score14[0]=='9'):
            if (int(Score14[0])<=(1+x14)):
                x14=x1p4=int(Score14[0])
        elif (Score14[0]=='l'):
            if (x14<=1):
                x14=x1p4=1
        else:
            x14=x1p4
   


        if (Score24[0]=='0') or (Score24[0]=='1') or (Score24[0]=='2') or (Score24[0]=='3') or (Score24[0]=='4') or (Score24[0]=='5') or (Score24[0]=='6') or (Score24[0]=='7') or (Score24[0]=='8') or (Score24[0]=='9'):
            if (int(Score24[0])<=(1+y14)):
                y14=y1p4=int(Score24[0])
        elif (Score24[0]=='l'):
            if (y14<=1):
                y14=y1p4=1
        else:
            y14=y1p4
        try:
            f= open('D:\\TeamData.txt', 'a') 
            if (f.writable()==True):
        #with open('D:\\TeamData.txt', 'a') as f:
                f.write('\nG4    '+ Team1name4[:3]+'    '+Team2name4[:3]+'    '+ str(x14)+'    '+str(y14))
        except:
            pass
        time.sleep(0.3)

    elif (var[4]=='F'):
        frameTime4 = frame4[145:240, 200:445]
        frameTeam1_name4 = frame4[145:240, 500:820]
        frameTeam2_name4 = frame4[145:240, 1210:1570]
        frame_Score14= frame4[135:245,500:950]
        frame_Score24= frame4[135:245,1100:1570]
        Game_Time4= pytesseract.image_to_string(frameTime4)
        Game_Time4=Game_Time4.rstrip('\n')
        Game_Time4=Game_Time4+"AAA"
        Team1name4 = pytesseract.image_to_string(frameTeam1_name4)
        Team1name4=Team1name4.rstrip('\n')# removing /n to add data after
        Team1name4=Team1name4+'1___'# adding data after that in case there is nothing to read 
        Team2name4 = pytesseract.image_to_string(frameTeam2_name4)
        Team2name4=Team2name4.rstrip('\n')
        Team2name4=Team2name4+'1___'
        Score14=pytesseract.image_to_string(frame_Score14)
        Score14=Score14.rstrip('\n')# Removing /n from data 
        Score14='A'+Score14
        Score24=pytesseract.image_to_string(frame_Score24)
        Score24=Score24.rstrip('\n')# Removing /n from data 
        Score24=Score24+"AAA"

    #//////////////////////////////////////////////////////
    # Time of the game
        Char1_Time4= Game_Time4[:1] 
        Char2_Time4=Game_Time4[1:2] 
        Char3_Time4=Game_Time4[2:3]
        Char1_2_Time4= Game_Time4[:2] 
        if  (Char1_Time4 =='0') or (Char1_Time4 =='1') or (Char1_Time4=='2') or (Char1_Time4=='3') or (Char1_Time4=='4') or (Char1_Time4=='5') or (Char1_Time4=='6') or (Char1_Time4=='7')or (Char1_Time4=='8') or (Char1_Time4=='9'):
            if (Char2_Time4 =='0') or (Char2_Time4 =='1') or (Char2_Time4=='2') or (Char2_Time4=='3') or (Char2_Time4=='4') or (Char2_Time4=='5') or (Char2_Time4=='6') or (Char2_Time4=='7')or (Char2_Time4=='8') or (Char2_Time4=='9'):
                MatchTime4=MatchTime_prev4=int(Char1_2_Time4)
                f4=1
        else:
            MatchTime4=MatchTime_prev4
            f4=0

        if (Team1name4[0]=='1'):
            Team1name4= Team1name_prev4
        else:
            if (f4==1):
                Team1name_prev4=Team1name4[:3]
            else:
                Team1name4= Team1name_prev4

        if (Team2name4[0]=='1'):
            Team2name4= Team2name_prev4
        else:
            if (f4==1):
                Team2name_prev4=Team2name4[:3]
            else:
                Team2name4= Team2name_prev4

    
        if (Score14[-1]=='0') or (Score14[-1]=='1') or (Score14[-1]=='2') or (Score14[-1]=='3') or (Score14[-1]=='4') or (Score14[-1]=='5') or (Score14[-1]=='6') or (Score14[-1]=='7') or (Score14[-1]=='8') or (Score14[-1]=='9'):
            if (int(Score14[-1])<=(1+x14)):
                x14=x1p4=int(Score14[-1])

        elif(Score14[-1]=='G'):
             if ((x14<=4) and (x14>2)):
                x14=x1p4=4
        else:
            x14=x1p4
   
        if (Score24[0]=='0') or (Score24[0]=='1') or (Score24[0]=='2') or (Score24[0]=='3') or (Score24[0]=='4') or (Score24[0]=='5') or (Score24[0]=='6') or (Score24[0]=='7') or (Score24[0]=='8') or (Score24[0]=='9'):
            if (int(Score24[0])<=(1+y14)):
                y14=y1p4=int(Score24[0])

        elif(Score24[0]=='G'):
            if ((y14<=4) and (y14>2)):
                y14=y1p4=4
        else:
            y14=y1p4
        try:
            f= open('D:\\TeamData.txt', 'a') 
            if (f.writable()==True):
        #with open('D:\\TeamData.txt', 'a') as f:
                f.write('\nF4    '+ Team1name4[:3]+'    '+Team2name4[:3]+'    '+ str(x14)+'    '+str(y14))
        except:
            pass

        time.sleep(0.3)

    elif (var[4]=='R'):
        frameTime4 = frame4[110:180, 200:400]
        frameTeam1_name4 = frame4[110:180, 470:640]
        frameTeam2_name4 = frame4[110:180, 850:1010]
        frame_Score14= frame4[110:180, 660:835]
        frame_Score24= frame4[110:180, 660:835]
        #cv2.imshow('frame',frameTeam1_name)
        Game_Time4= pytesseract.image_to_string(frameTime4)
        Game_Time4=Game_Time4.rstrip('\n')
        Game_Tim4=Game_Time4+"AAA"
        Team1name4 = pytesseract.image_to_string(frameTeam1_name4)
        Team1name4=Team1name4.rstrip('\n')# removing /n to add data after
        Team1name4=Team1name4+'1___'# adding data after that in case there is nothing to read 
        Team2name4 = pytesseract.image_to_string(frameTeam2_name4)
        Team2name4=Team2name4.rstrip('\n')
        Team2name4=Team2name4+'1___'
        Score14=pytesseract.image_to_string(frame_Score14)
        Score14=Score14.rstrip('\n')# Removing /n from data 
        Score14=Score14+"AAA"
        Score24=pytesseract.image_to_string(frame_Score24)
        Score24=Score24.rstrip('\n')# Removing /n from data 
        Score24=Score24+"AAA"
    # Showing Time of the Match
        Char1_Time4= Game_Time4[:1] 
        Char2_Time4=Game_Time4[1:2] 
        Char3_Time4=Game_Time4[2:3]
        Char1_2_Time4= Game_Time4[:2] 
        if  (Char1_Time4 =='0') or (Char1_Time4 =='1') or (Char1_Time4=='2') or (Char1_Time4=='3') or (Char1_Time4=='4') or (Char1_Time4=='5') or (Char1_Time4=='6') or (Char1_Time4=='7')or (Char1_Time4=='8') or (Char1_Time4=='9'):
            if (Char2_Time4 =='0') or (Char2_Time4 =='1') or (Char2_Time4=='2') or (Char2_Time4=='3') or (Char2_Time4=='4') or (Char2_Time4=='5') or (Char2_Time4=='6') or (Char2_Time4=='7')or (Char2_Time4=='8') or (Char2_Time4=='9'):
                MatchTime4=MatchTime_prev4=int(Char1_2_Time4)
                f4=1
        else:
            MatchTime4=MatchTime_prev4
            f4=0
    # End Time of the Match
    
    #Showing the Name of the Teams
        if (Team1name4[3]!='1'):
            Team1name4= Team1name_prev4
        else:
            if (f4==1):
                Team1name_prev4=Team1name4[:3]
            else:
                Team1name4= Team1name_prev4

        if (Team2name4[3]!='1'):
            Team2name4= Team2name_prev4
        else:
            if (f4==1):
                Team2name_prev4=Team2name4[:3]
            else:
                Team2name4= Team2name_prev4
 
    # Showing the Scores:
        if (Score14[0]=='0') or (Score14[0]=='1') or (Score14[0]=='2') or (Score14[0]=='3') or (Score14[0]=='4') or (Score14[0]=='5') or (Score14[0]=='6') or (Score14[0]=='7') or (Score14[0]=='8') or (Score14[0]=='9'):
            if (int(Score14[0])<=(1+x14)):
                x14=x1p4=int(Score14[0])
        else:
            x14=x1p4
   
        if (Score24[2]=='0') or (Score24[2]=='1') or (Score24[2]=='2') or (Score24[2]=='3') or (Score24[2]=='4') or (Score24[2]=='5') or (Score24[2]=='6') or (Score24[2]=='7') or (Score24[2]=='8') or (Score24[2]=='9'):
            if (int(Score24[2])<=(1+y14)):
                y14=y1p4=int(Score24[2])
        else:
            y14=y1p4
        try:
            f= open('D:\\TeamData.txt', 'a') 
            if (f.writable()==True):
        #with open('D:\\TeamData.txt', 'a') as f:
                f.write('\nR4    '+ Team1name4[:3]+'    '+Team2name4[:3]+'    '+ str(x14)+'    '+str(y14))
        except:
            pass
        time.sleep(0.3)

    else:
        pass
###########################################################################################################################################

    if (var[5]=='E'):
        frameTime5 = frame5[280:350, 420:615]
        frameTeam1_name5 = frame5[205:270, 230:390]
        frameTeam2_name5 = frame5[205:270, 630:815]
        frame_Score15= frame5[210:345, 440:585]
        frame_Score25= frame5[210:345, 440:585]
        #cv2.imshow('frame',frameTeam1_name)
        Game_Time5= pytesseract.image_to_string(frameTime5)
        Game_Time5=Game_Time5.rstrip('\n')
        Game_Tim5=Game_Time5+"AAA"
        Team1name5 = pytesseract.image_to_string(frameTeam1_name5)
        Team1name5=Team1name5.rstrip('\n')# removing /n to add data after
        Team1name5=Team1name5+'1___'# adding data after that in case there is nothing to read 
        Team2name5 = pytesseract.image_to_string(frameTeam2_name5)
        Team2name5=Team2name5.rstrip('\n')
        Team2name5=Team2name5+'1___'
        Score15=pytesseract.image_to_string(frame_Score15)
        Score15=Score15.rstrip('\n')# Removing /n from data 
        Score15=Score15+"AAA"
        Score25=pytesseract.image_to_string(frame_Score25)
        Score25=Score25.rstrip('\n')# Removing /n from data 
        Score25=Score25+"AAA"
    # Showing Time of the Match
        Char1_Time5= Game_Time5[:1] 
        Char2_Time5=Game_Time5[1:2] 
        Char3_Time5=Game_Time5[2:3]
        Char1_2_Time5= Game_Time5[:2] 
        if  (Char1_Time5 =='0') or (Char1_Time5 =='1') or (Char1_Time5=='2') or (Char1_Time5=='3') or (Char1_Time5=='4') or (Char1_Time5=='5') or (Char1_Time5=='6') or (Char1_Time5=='7')or (Char1_Time5=='8') or (Char1_Time5=='9'):
            if (Char2_Time5 =='0') or (Char2_Time5 =='1') or (Char2_Time5=='2') or (Char2_Time5=='3') or (Char2_Time5=='4') or (Char2_Time5=='5') or (Char2_Time5=='6') or (Char2_Time5=='7')or (Char2_Time5=='8') or (Char2_Time5=='9'):
                MatchTime5=MatchTime_prev5=int(Char1_2_Time5)
                f5=1
        else:
            MatchTime5=MatchTime_prev5
            f5=0
    # End Time of the Match
    
    #Showing the Name of the Teams
        if (Team1name5[3]!='1'):
            Team1name5= Team1name_prev5
        else:
            if (f5==1):
                Team1name_prev5=Team1name5[:3]
            else:
                Team1name5= Team1name_prev5

        if (Team2name5[3]!='1'):
            Team2name5= Team2name_prev5
        else:
            if (f5==1):
                Team2name_prev5=Team2name5[:3]
            else:
                Team2name5= Team2name_prev5
 
    # Showing the Scores:
        if (Score15[0]=='0') or (Score15[0]=='1') or (Score15[0]=='2') or (Score15[0]=='3') or (Score15[0]=='4') or (Score15[0]=='5') or (Score15[0]=='6') or (Score15[0]=='7') or (Score15[0]=='8') or (Score15[0]=='9'):
            if (int(Score15[0])<=(1+x15)):
                x15=x1p5=int(Score15[0])
        else:
            x15=x1p5
   
        if (Score25[2]=='0') or (Score25[2]=='1') or (Score25[2]=='2') or (Score25[2]=='3') or (Score25[2]=='4') or (Score25[2]=='5') or (Score25[2]=='6') or (Score25[2]=='7') or (Score25[2]=='8') or (Score25[2]=='9'):
            if (int(Score25[2])<=(1+y15)):
                y15=y1p5=int(Score25[2])
        else:
            y15=y1p5
        try:
            f= open('D:\\TeamData.txt', 'a') 
            if (f.writable()==True):
        #with open('D:\\TeamData.txt', 'a') as f:
                f.write('\nE5    '+ Team1name5[:3]+'    '+Team2name5[:3]+'    '+ str(x15)+'    '+str(y15))
        except:
            pass
        time.sleep(0.3)
        #print ("Current Time: "+ str(MatchTime))
        
    elif (var[5]=='S'):
        frameTime5 = frame5[122:212, 305:560]
        frameTeam1_name5 = frame5[130:190, 575:765]
        frameTeam2_name5 = frame5[130:190, 995:1175]
        frame_Score15= frame5[115:210,780:1165]
        frame_Score25= frame5[115:210,780:1165]
        #cv2.imshow('frame',frame_Score10)
        Game_Time5= pytesseract.image_to_string(frameTime5)
        Game_Time5=Game_Time5.rstrip('\n')
        Game_Tim5=Game_Time5+"AAA"
        Team1name5 = pytesseract.image_to_string(frameTeam1_name5)
        Team1name5=Team1name5.rstrip('\n')# removing /n to add data after
        Team1name5=Team1name5+'1___'# adding data after that in case there is nothing to read 
        Team2name5 = pytesseract.image_to_string(frameTeam2_name5)
        Team2name5=Team2name5.rstrip('\n')
        Team2name5=Team2name5+'1___'
        Score15=pytesseract.image_to_string(frame_Score15)
        Score15=Score15.rstrip('\n')# Removing /n from data 
        Score15=Score15+"AAA"
        Score25=pytesseract.image_to_string(frame_Score25)
        Score25=Score25.rstrip('\n')# Removing /n from data 
        Score25=Score25+"AAA"
    # Showing Time of the Match
        Char1_Time5= Game_Time5[:1] 
        Char2_Time5=Game_Time5[1:2] 
        Char3_Time5=Game_Time5[2:3]
        Char1_2_Time5= Game_Time5[:2] 
        if  (Char1_Time5 =='0') or (Char1_Time5 =='1') or (Char1_Time5=='2') or (Char1_Time5=='3') or (Char1_Time5=='4') or (Char1_Time5=='5') or (Char1_Time5=='6') or (Char1_Time5=='7')or (Char1_Time5=='8') or (Char1_Time5=='9'):
            if (Char2_Time5 =='0') or (Char2_Time5 =='1') or (Char2_Time5=='2') or (Char2_Time5=='3') or (Char2_Time5=='4') or (Char2_Time5=='5') or (Char2_Time5=='6') or (Char2_Time5=='7')or (Char2_Time5=='8') or (Char2_Time5=='9'):
                MatchTime5=MatchTime_prev5=int(Char1_2_Time5)
                f5=1
        else:
            MatchTime5=MatchTime_prev5
            f5=0
    # End Time of the Match
    
    #Showing the Name of the Teams
        if (Team1name5[3]!='1'):
            Team1name5= Team1name_prev5
        else:
            if (f5==1):
                Team1name_prev5=Team1name5[:3]
            else:
                Team1name5= Team1name_prev5

        if (Team2name5[3]!='1'):
            Team2name5= Team2name_prev5
        else:
            if (f5==1):
                Team2name_prev5=Team2name5[:3]
            else:
                Team2name5= Team2name_prev5
 
    # Showing the Scores:
        if (Score15[0]=='0') or (Score15[0]=='1') or (Score15[0]=='2') or (Score15[0]=='3') or (Score15[0]=='4') or (Score15[0]=='5') or (Score15[0]=='6') or (Score15[0]=='7') or (Score15[0]=='8') or (Score15[0]=='9'):
            if (int(Score15[0])<=(1+x15)):
                x15=x1p5=int(Score15[0])
        else:
            x15=x1p5
   
        if (Score25[2]=='0') or (Score25[2]=='1') or (Score25[2]=='2') or (Score25[2]=='3') or (Score25[2]=='4') or (Score25[2]=='5') or (Score25[2]=='6') or (Score25[2]=='7') or (Score25[2]=='8') or (Score25[2]=='9'):
            if (int(Score25[2])<=(1+y15)):
                y15=y1p5=int(Score25[2])
        else:
            y15=y1p5
        try:
            f= open('D:\\TeamData.txt', 'a') 
            if (f.writable()==True):
        #with open('D:\\TeamData.txt', 'a') as f:
                f.write('\nS5    '+ Team1name5[:3]+'    '+Team2name5[:3]+'    '+ str(x15)+'    '+str(y15))
        except:
            pass
        time.sleep(0.3)

    ##############################################################
    elif (var[5]=='I'):
        frameTime5 = frame5[130:215, 1180:1370]
        frameTeam1_name5 = frame5[130:220, 330:540]
        frameTeam2_name5 = frame5[130:220, 930:1100]
        frame_Score15= frame5[130:210, 650:800]
        frame_Score25= frame5[130:210, 650:800]
        Game_Time5= pytesseract.image_to_string(frameTime5)
        Game_Time5=Game_Time5.rstrip('\n')
        Game_Tim5=Game_Time5+"AAA"
        Team1name5 = pytesseract.image_to_string(frameTeam1_name5)
        Team1name5=Team1name5.rstrip('\n')# removing /n to add data after
        Team1name5=Team1name5+'1___'# adding data after that in case there is nothing to read 
        Team2name5 = pytesseract.image_to_string(frameTeam2_name5)
        Team2name5=Team2name5.rstrip('\n')
        Team2name5=Team2name5+'1___'
        Score15=pytesseract.image_to_string(frame_Score15)
        Score15=Score15.rstrip('\n')# Removing /n from data 
        Score15=Score15+"AAA"
        Score25=pytesseract.image_to_string(frame_Score25)
        Score25=Score25.rstrip('\n')# Removing /n from data 
        Score25=Score25+"AAA"

        Char1_Time5= Game_Time5[:1] 
        Char2_Time5=Game_Time5[1:2] 
        Char3_Time5=Game_Time5[2:3]
        Char1_2_Time5= Game_Time5[:2] 
        fp5=f5
        if  (Char1_Time5 =='0') or (Char1_Time5 =='1') or (Char1_Time5=='2') or (Char1_Time5=='3') or (Char1_Time5=='4') or (Char1_Time5=='5') or (Char1_Time5=='6') or (Char1_Time5=='7')or (Char1_Time5=='8') or (Char1_Time5=='9'):
            if (Char2_Time5 =='0') or (Char2_Time5 =='1') or (Char2_Time5=='2') or (Char2_Time5=='3') or (Char2_Time5=='4') or (Char2_Time5=='5') or (Char2_Time5=='6') or (Char2_Time5=='7')or (Char2_Time5=='8') or (Char2_Time5=='9'):
                MatchTime5=MatchTime_prev5=int(Char1_2_Time5)
                f5=1
        else:
            MatchTime5=MatchTime_prev5
            f5=0
       

        if (Team1name5[3]!='1'):
            Team1name5= Team1name_prev5
        else:
            if (f5==1):  
                Team1name_prev5=Team1name5[:3]    
            else:
                Team1name5= Team1name_prev5

        if (Team2name5[3]!='1'):
            Team2name5= Team2name_prev5
        else:
            if (f5==1):
                Team2name_prev5=Team2name5[:3]
            else:
                Team2name5= Team2name_prev5

       
    # End Name of the teams

    # Showing the Scores:
        if (f5==1):
            if (Score15[0]=='0') or (Score15[0]=='1') or (Score15[0]=='2') or (Score15[0]=='3') or (Score15[0]=='4') or (Score15[0]=='5') or (Score15[0]=='6') or (Score15[0]=='7') or (Score15[0]=='8') or (Score15[0]=='9'):
                if (int(Score15[0])<=(1+x15)):
                    x15=x1p5=int(Score15[0])
            else:
                x15=x1p5
        else:
            x15=x1p5
   

        if (f5==1):
            if (Score25[2]=='0') or (Score25[2]=='1') or (Score25[2]=='2') or (Score25[2]=='3') or (Score25[2]=='4') or (Score25[2]=='5') or (Score25[2]=='6') or (Score25[2]=='7') or (Score25[2]=='8') or (Score25[2]=='9'):
                if (int(Score25[2])<=(1+y15)):
                    y15=y1p5=int(Score25[2])
            else:
                y15=y1p5
        else:
            y15=y1p5
        try:
            f= open('D:\\TeamData.txt', 'a') 
            if (f.writable()==True):
        #with open('D:\\TeamData.txt', 'a') as f:
                f.write('\nI5    '+ Team1name5[:3]+'    '+Team2name5[:3]+'    '+ str(x15)+'    '+str(y15))
        except:
            pass
        time.sleep(0.3)

#########################################################################
    elif (var[5]=='G'):
        frameTime5 = frame5[110:180, 285:460]
        frameTeam1_name5 = frame5[110:180, 470:630]
        frameTeam2_name5 = frame5[110:180, 660:800]
        frame_Score15= frame5[185:315, 475:620]
        frame_Score25= frame5[185:315, 675:820]
        Game_Time5= pytesseract.image_to_string(frameTime5)
        Game_Time5=Game_Time5.rstrip('\n')
        Game_Time5=Game_Time5+"AAA"
        Team1name5 = pytesseract.image_to_string(frameTeam1_name5)
        Team1name5=Team1name5.rstrip('\n')# removing /n to add data after
        Team1name5=Team1name5+'1___'# adding data after that in case there is nothing to read 
        Team2name5 = pytesseract.image_to_string(frameTeam2_name5)
        Team2name5=Team2name5.rstrip('\n')
        Team2name5=Team2name5+'1___'
        Score15=pytesseract.image_to_string(frame_Score15, config=("-c tessedit"
                  "_char_whitelist=abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"
                  " --psm 10"
                  " -l osd"
                  " "))
        Score15=Score15.rstrip('\n')# Removing /n from data 
        Score15=Score15+"AAA"
        Score25=pytesseract.image_to_string(frame_Score25, config=("-c tessedit"
                  "_char_whitelist=abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"
                  " --psm 10"
                  " -l osd"
                  " "))
        Score25=Score25.rstrip('\n')# Removing /n from data 
        Score25=Score25+"AAA"

    #///////////////////////////////////////////////////////////////
    # Showing Time of the Match
        Char1_Time5= Game_Time5[:1] 
        Char2_Time5=Game_Time5[1:2] 
        Char3_Time5=Game_Time5[2:3]
        Char1_2_Time5= Game_Time5[:2] 
        if  (Char1_Time5 =='0') or (Char1_Time5 =='1') or (Char1_Time5=='2') or (Char1_Time5=='3') or (Char1_Time5=='4') or (Char1_Time5=='5') or (Char1_Time5=='6') or (Char1_Time5=='7')or (Char1_Time5=='8') or (Char1_Time5=='9'):
            if (Char2_Time5 =='0') or (Char2_Time5 =='1') or (Char2_Time5=='2') or (Char2_Time5=='3') or (Char2_Time5=='4') or (Char2_Time5=='5') or (Char2_Time5=='6') or (Char2_Time5=='7')or (Char2_Time5=='8') or (Char2_Time5=='9'):
                MatchTime5=MatchTime_prev5=int(Char1_2_Time5)
                f5=1
        else:
            MatchTime5=MatchTime_prev5
            f5=0

        if (Team1name5[3]!='1'):
            Team1name5= Team1name_prev5
        else:
            if (f5==1):
                Team1name_prev5=Team1name5[:3]
            else:
                Team1name5= Team1name_prev5

        if (Team2name5[3]!='1'):
            Team2name5= Team2name_prev5
        else:
            if (f5==1):
                Team2name_prev5=Team2name5[:3]
            else:
                Team2name5= Team2name_prev5

        if (Score15[0]=='0') or (Score15[0]=='1') or (Score15[0]=='2') or (Score15[0]=='3') or (Score15[0]=='4') or (Score15[0]=='5') or (Score15[0]=='6') or (Score15[0]=='7') or (Score15[0]=='8') or (Score15[0]=='9'):
            if (int(Score15[0])<=(1+x15)):
                x15=x1p5=int(Score15[0])
        elif (Score15[0]=='l'):
            if (x15<=1):
                x15=x1p5=1
        else:
            x15=x1p5
   


        if (Score25[0]=='0') or (Score25[0]=='1') or (Score25[0]=='2') or (Score25[0]=='3') or (Score25[0]=='4') or (Score25[0]=='5') or (Score25[0]=='6') or (Score25[0]=='7') or (Score25[0]=='8') or (Score25[0]=='9'):
            if (int(Score25[0])<=(1+y15)):
                y15=y1p5=int(Score25[0])
        elif (Score25[0]=='l'):
            if (y15<=1):
                y15=y1p5=1
        else:
            y15=y1p5
        try:
            f= open('D:\\TeamData.txt', 'a') 
            if (f.writable()==True):
        #with open('D:\\TeamData.txt', 'a') as f:
                f.write('\nG5    '+ Team1name5[:3]+'    '+Team2name5[:3]+'    '+ str(x15)+'    '+str(y15))
        except:
            pass
        time.sleep(0.3)

    elif (var[5]=='F'):
        frameTime5 = frame5[145:240, 200:445]
        frameTeam1_name5 = frame5[145:240, 500:820]
        frameTeam2_name5 = frame5[145:240, 1210:1570]
        frame_Score15= frame5[135:245,500:950]
        frame_Score25= frame5[135:245,1100:1570]
        Game_Time5= pytesseract.image_to_string(frameTime5)
        Game_Time5=Game_Time5.rstrip('\n')
        Game_Time5=Game_Time5+"AAA"
        Team1name5 = pytesseract.image_to_string(frameTeam1_name5)
        Team1name5=Team1name5.rstrip('\n')# removing /n to add data after
        Team1name5=Team1name5+'1___'# adding data after that in case there is nothing to read 
        Team2name5 = pytesseract.image_to_string(frameTeam2_name5)
        Team2name5=Team2name5.rstrip('\n')
        Team2name5=Team2name5+'1___'
        Score15=pytesseract.image_to_string(frame_Score15)
        Score15=Score15.rstrip('\n')# Removing /n from data 
        Score15='A'+Score15
        Score25=pytesseract.image_to_string(frame_Score25)
        Score25=Score25.rstrip('\n')# Removing /n from data 
        Score25=Score25+"AAA"

    #//////////////////////////////////////////////////////
    # Time of the game
        Char1_Time5= Game_Time5[:1] 
        Char2_Time5=Game_Time5[1:2] 
        Char3_Time5=Game_Time5[2:3]
        Char1_2_Time5= Game_Time5[:2] 
        if  (Char1_Time5 =='0') or (Char1_Time5 =='1') or (Char1_Time5=='2') or (Char1_Time5=='3') or (Char1_Time5=='4') or (Char1_Time5=='5') or (Char1_Time5=='6') or (Char1_Time5=='7')or (Char1_Time5=='8') or (Char1_Time5=='9'):
            if (Char2_Time5 =='0') or (Char2_Time5 =='1') or (Char2_Time5=='2') or (Char2_Time5=='3') or (Char2_Time5=='4') or (Char2_Time5=='5') or (Char2_Time5=='6') or (Char2_Time5=='7')or (Char2_Time5=='8') or (Char2_Time5=='9'):
                MatchTime5=MatchTime_prev5=int(Char1_2_Time5)
                f5=1
        else:
            MatchTime5=MatchTime_prev5
            f5=0

        if (Team1name5[0]=='1'):
            Team1name5= Team1name_prev5
        else:
            if (f5==1):
                Team1name_prev5=Team1name5[:3]
            else:
                Team1name5= Team1name_prev5

        if (Team2name5[0]=='1'):
            Team2name5= Team2name_prev5
        else:
            if (f5==1):
                Team2name_prev5=Team2name5[:3]
            else:
                Team2name5= Team2name_prev5

    
        if (Score15[-1]=='0') or (Score15[-1]=='1') or (Score15[-1]=='2') or (Score15[-1]=='3') or (Score15[-1]=='4') or (Score15[-1]=='5') or (Score15[-1]=='6') or (Score15[-1]=='7') or (Score15[-1]=='8') or (Score15[-1]=='9'):
            if (int(Score15[-1])<=(1+x15)):
                x15=x1p5=int(Score15[-1])

        elif(Score15[-1]=='G'):
             if ((x15<=4) and (x15>2)):
                x15=x1p5=4
        else:
            x15=x1p5
   
        if (Score25[0]=='0') or (Score25[0]=='1') or (Score25[0]=='2') or (Score25[0]=='3') or (Score25[0]=='4') or (Score25[0]=='5') or (Score25[0]=='6') or (Score25[0]=='7') or (Score25[0]=='8') or (Score25[0]=='9'):
            if (int(Score25[0])<=(1+y15)):
                y15=y1p5=int(Score25[0])

        elif(Score25[0]=='G'):
            if ((y15<=4) and (y15>2)):
                y15=y1p5=4
        else:
            y15=y1p5
        try:
            f= open('D:\\TeamData.txt', 'a') 
            if (f.writable()==True):
        #with open('D:\\TeamData.txt', 'a') as f:
                f.write('\nF5    '+ Team1name5[:3]+'    '+Team2name5[:3]+'    '+ str(x15)+'    '+str(y15))
        except:
            pass

        time.sleep(0.3)

    elif (var[5]=='R'):
        frameTime5 = frame5[110:180, 200:400]
        frameTeam1_name5 = frame5[110:180, 470:640]
        frameTeam2_name5 = frame5[110:180, 850:1010]
        frame_Score15= frame5[110:180, 660:835]
        frame_Score25= frame5[110:180, 660:835]
        #cv2.imshow('frame',frameTeam1_name)
        Game_Time5= pytesseract.image_to_string(frameTime5)
        Game_Time5=Game_Time5.rstrip('\n')
        Game_Tim5=Game_Time5+"AAA"
        Team1name5 = pytesseract.image_to_string(frameTeam1_name5)
        Team1name5=Team1name5.rstrip('\n')# removing /n to add data after
        Team1name5=Team1name5+'1___'# adding data after that in case there is nothing to read 
        Team2name5 = pytesseract.image_to_string(frameTeam2_name5)
        Team2name5=Team2name5.rstrip('\n')
        Team2name5=Team2name5+'1___'
        Score15=pytesseract.image_to_string(frame_Score15)
        Score15=Score15.rstrip('\n')# Removing /n from data 
        Score15=Score15+"AAA"
        Score25=pytesseract.image_to_string(frame_Score25)
        Score25=Score25.rstrip('\n')# Removing /n from data 
        Score25=Score25+"AAA"
    # Showing Time of the Match
        Char1_Time5= Game_Time5[:1] 
        Char2_Time5=Game_Time5[1:2] 
        Char3_Time5=Game_Time5[2:3]
        Char1_2_Time5= Game_Time5[:2] 
        if  (Char1_Time5 =='0') or (Char1_Time5 =='1') or (Char1_Time5=='2') or (Char1_Time5=='3') or (Char1_Time5=='4') or (Char1_Time5=='5') or (Char1_Time5=='6') or (Char1_Time5=='7')or (Char1_Time5=='8') or (Char1_Time5=='9'):
            if (Char2_Time5 =='0') or (Char2_Time5 =='1') or (Char2_Time5=='2') or (Char2_Time5=='3') or (Char2_Time5=='4') or (Char2_Time5=='5') or (Char2_Time5=='6') or (Char2_Time5=='7')or (Char2_Time5=='8') or (Char2_Time5=='9'):
                MatchTime5=MatchTime_prev5=int(Char1_2_Time5)
                f5=1
        else:
            MatchTime5=MatchTime_prev5
            f5=0
    # End Time of the Match
    
    #Showing the Name of the Teams
        if (Team1name5[3]!='1'):
            Team1name5= Team1name_prev5
        else:
            if (f5==1):
                Team1name_prev5=Team1name5[:3]
            else:
                Team1name5= Team1name_prev5

        if (Team2name5[3]!='1'):
            Team2name5= Team2name_prev5
        else:
            if (f5==1):
                Team2name_prev5=Team2name5[:3]
            else:
                Team2name5= Team2name_prev5
 
    # Showing the Scores:
        if (Score15[0]=='0') or (Score15[0]=='1') or (Score15[0]=='2') or (Score15[0]=='3') or (Score15[0]=='4') or (Score15[0]=='5') or (Score15[0]=='6') or (Score15[0]=='7') or (Score15[0]=='8') or (Score15[0]=='9'):
            if (int(Score15[0])<=(1+x15)):
                x15=x1p5=int(Score15[0])
        else:
            x15=x1p5
   
        if (Score25[2]=='0') or (Score25[2]=='1') or (Score25[2]=='2') or (Score25[2]=='3') or (Score25[2]=='4') or (Score25[2]=='5') or (Score25[2]=='6') or (Score25[2]=='7') or (Score25[2]=='8') or (Score25[2]=='9'):
            if (int(Score25[2])<=(1+y15)):
                y15=y1p5=int(Score25[2])
        else:
            y15=y1p5
        try:
            f= open('D:\\TeamData.txt', 'a') 
            if (f.writable()==True):
        #with open('D:\\TeamData.txt', 'a') as f:
                f.write('\nR5    '+ Team1name5[:3]+'    '+Team2name5[:3]+'    '+ str(x15)+'    '+str(y15))
        except:
            pass
        time.sleep(0.3)

    else:
        pass
####################################################################################################################################

    if (var[6]=='E'):
        frameTime6 = frame6[280:350, 420:615]
        frameTeam1_name6 = frame6[205:270, 230:390]
        frameTeam2_name6 = frame6[205:270, 630:815]
        frame_Score16= frame6[210:345, 440:585]
        frame_Score26= frame6[210:345, 440:585]
        #cv2.imshow('frame',frameTeam1_name)
        Game_Time6= pytesseract.image_to_string(frameTime6)
        Game_Time6=Game_Time6.rstrip('\n')
        Game_Tim6=Game_Time6+"AAA"
        Team1name6 = pytesseract.image_to_string(frameTeam1_name6)
        Team1name6=Team1name6.rstrip('\n')# removing /n to add data after
        Team1name6=Team1name6+'1___'# adding data after that in case there is nothing to read 
        Team2name6 = pytesseract.image_to_string(frameTeam2_name6)
        Team2name6=Team2name6.rstrip('\n')
        Team2name6=Team2name6+'1___'
        Score16=pytesseract.image_to_string(frame_Score16)
        Score16=Score16.rstrip('\n')# Removing /n from data 
        Score16=Score16+"AAA"
        Score26=pytesseract.image_to_string(frame_Score26)
        Score26=Score26.rstrip('\n')# Removing /n from data 
        Score26=Score26+"AAA"
    # Showing Time of the Match
        Char1_Time6= Game_Time6[:1] 
        Char2_Time6=Game_Time6[1:2] 
        Char3_Time6=Game_Time6[2:3]
        Char1_2_Time6= Game_Time6[:2] 
        if  (Char1_Time6 =='0') or (Char1_Time6 =='1') or (Char1_Time6=='2') or (Char1_Time6=='3') or (Char1_Time6=='4') or (Char1_Time6=='5') or (Char1_Time6=='6') or (Char1_Time6=='7')or (Char1_Time6=='8') or (Char1_Time6=='9'):
            if (Char2_Time6 =='0') or (Char2_Time6 =='1') or (Char2_Time6=='2') or (Char2_Time6=='3') or (Char2_Time6=='4') or (Char2_Time6=='5') or (Char2_Time6=='6') or (Char2_Time6=='7')or (Char2_Time6=='8') or (Char2_Time6=='9'):
                MatchTime6=MatchTime_prev6=int(Char1_2_Time6)
                f6=1
        else:
            MatchTime6=MatchTime_prev6
            f6=0
    # End Time of the Match
    
    #Showing the Name of the Teams
        if (Team1name6[3]!='1'):
            Team1name6= Team1name_prev6
        else:
            if (f6==1):
                Team1name_prev6=Team1name6[:3]
            else:
                Team1name6= Team1name_prev6

        if (Team2name6[3]!='1'):
            Team2name6= Team2name_prev6
        else:
            if (f6==1):
                Team2name_prev6=Team2name6[:3]
            else:
                Team2name6= Team2name_prev6
 
    # Showing the Scores:
        if (Score16[0]=='0') or (Score16[0]=='1') or (Score16[0]=='2') or (Score16[0]=='3') or (Score16[0]=='4') or (Score16[0]=='5') or (Score16[0]=='6') or (Score16[0]=='7') or (Score16[0]=='8') or (Score16[0]=='9'):
            if (int(Score16[0])<=(1+x16)):
                x16=x1p6=int(Score16[0])
        else:
            x16=x1p6
   
        if (Score26[2]=='0') or (Score26[2]=='1') or (Score26[2]=='2') or (Score26[2]=='3') or (Score26[2]=='4') or (Score26[2]=='5') or (Score26[2]=='6') or (Score26[2]=='7') or (Score26[2]=='8') or (Score26[2]=='9'):
            if (int(Score26[2])<=(1+y16)):
                y16=y1p6=int(Score26[2])
        else:
            y16=y1p6
        try:
            f= open('D:\\TeamData.txt', 'a') 
            if (f.writable()==True):
        #with open('D:\\TeamData.txt', 'a') as f:
                f.write('\nE6    '+ Team1name6[:3]+'    '+Team2name6[:3]+'    '+ str(x16)+'    '+str(y16))
        except:
            pass
        time.sleep(0.3)
        #print ("Current Time: "+ str(MatchTime))
        
    elif (var[6]=='S'):
        frameTime6 = frame6[122:212, 305:560]
        frameTeam1_name6 = frame6[130:190, 575:765]
        frameTeam2_name6 = frame6[130:190, 995:1175]
        frame_Score16= frame6[115:210,780:1165]
        frame_Score26= frame6[115:210,780:1165]
        #cv2.imshow('frame',frame_Score10)
        Game_Time6= pytesseract.image_to_string(frameTime6)
        Game_Time6=Game_Time6.rstrip('\n')
        Game_Tim6=Game_Time6+"AAA"
        Team1name6 = pytesseract.image_to_string(frameTeam1_name6)
        Team1name6=Team1name6.rstrip('\n')# removing /n to add data after
        Team1name6=Team1name6+'1___'# adding data after that in case there is nothing to read 
        Team2name6 = pytesseract.image_to_string(frameTeam2_name6)
        Team2name6=Team2name6.rstrip('\n')
        Team2name6=Team2name6+'1___'
        Score16=pytesseract.image_to_string(frame_Score16)
        Score16=Score16.rstrip('\n')# Removing /n from data 
        Score16=Score16+"AAA"
        Score26=pytesseract.image_to_string(frame_Score26)
        Score26=Score26.rstrip('\n')# Removing /n from data 
        Score26=Score26+"AAA"
    # Showing Time of the Match
        Char1_Time6= Game_Time6[:1] 
        Char2_Time6=Game_Time6[1:2] 
        Char3_Time6=Game_Time6[2:3]
        Char1_2_Time6= Game_Time6[:2] 
        if  (Char1_Time6 =='0') or (Char1_Time6 =='1') or (Char1_Time6=='2') or (Char1_Time6=='3') or (Char1_Time6=='4') or (Char1_Time6=='5') or (Char1_Time6=='6') or (Char1_Time6=='7')or (Char1_Time6=='8') or (Char1_Time6=='9'):
            if (Char2_Time6 =='0') or (Char2_Time6 =='1') or (Char2_Time6=='2') or (Char2_Time6=='3') or (Char2_Time6=='4') or (Char2_Time6=='5') or (Char2_Time6=='6') or (Char2_Time6=='7')or (Char2_Time6=='8') or (Char2_Time6=='9'):
                MatchTime6=MatchTime_prev6=int(Char1_2_Time6)
                f6=1
        else:
            MatchTime6=MatchTime_prev6
            f6=0
    # End Time of the Match
    
    #Showing the Name of the Teams
        if (Team1name6[3]!='1'):
            Team1name6= Team1name_prev6
        else:
            if (f6==1):
                Team1name_prev6=Team1name6[:3]
            else:
                Team1name6= Team1name_prev6

        if (Team2name6[3]!='1'):
            Team2name6= Team2name_prev6
        else:
            if (f6==1):
                Team2name_prev6=Team2name6[:3]
            else:
                Team2name6= Team2name_prev6
 
    # Showing the Scores:
        if (Score16[0]=='0') or (Score16[0]=='1') or (Score16[0]=='2') or (Score16[0]=='3') or (Score16[0]=='4') or (Score16[0]=='5') or (Score16[0]=='6') or (Score16[0]=='7') or (Score16[0]=='8') or (Score16[0]=='9'):
            if (int(Score16[0])<=(1+x16)):
                x16=x1p6=int(Score16[0])
        else:
            x16=x1p6
   
        if (Score26[2]=='0') or (Score26[2]=='1') or (Score26[2]=='2') or (Score26[2]=='3') or (Score26[2]=='4') or (Score26[2]=='5') or (Score26[2]=='6') or (Score26[2]=='7') or (Score26[2]=='8') or (Score26[2]=='9'):
            if (int(Score26[2])<=(1+y16)):
                y16=y1p6=int(Score26[2])
        else:
            y16=y1p6
        try:
            f= open('D:\\TeamData.txt', 'a') 
            if (f.writable()==True):
        #with open('D:\\TeamData.txt', 'a') as f:
                f.write('\nS6    '+ Team1name6[:3]+'    '+Team2name6[:3]+'    '+ str(x16)+'    '+str(y16))
        except:
            pass
        time.sleep(0.3)

    ##############################################################
    elif (var[6]=='I'):
        frameTime6 = frame6[130:215, 1180:1370]
        frameTeam1_name6 = frame6[130:220, 330:540]
        frameTeam2_name6 = frame6[130:220, 930:1100]
        frame_Score16= frame6[130:210, 650:800]
        frame_Score26= frame6[130:210, 650:800]
        Game_Time6= pytesseract.image_to_string(frameTime6)
        Game_Time6=Game_Time6.rstrip('\n')
        Game_Tim6=Game_Time6+"AAA"
        Team1name6 = pytesseract.image_to_string(frameTeam1_name6)
        Team1name6=Team1name6.rstrip('\n')# removing /n to add data after
        Team1name6=Team1name6+'1___'# adding data after that in case there is nothing to read 
        Team2name6 = pytesseract.image_to_string(frameTeam2_name6)
        Team2name6=Team2name6.rstrip('\n')
        Team2name6=Team2name6+'1___'
        Score16=pytesseract.image_to_string(frame_Score16)
        Score16=Score16.rstrip('\n')# Removing /n from data 
        Score16=Score16+"AAA"
        Score26=pytesseract.image_to_string(frame_Score26)
        Score26=Score26.rstrip('\n')# Removing /n from data 
        Score26=Score26+"AAA"

        Char1_Time6= Game_Time6[:1] 
        Char2_Time6=Game_Time6[1:2] 
        Char3_Time6=Game_Time6[2:3]
        Char1_2_Time6= Game_Time6[:2] 
        fp6=f6
        if  (Char1_Time6 =='0') or (Char1_Time6 =='1') or (Char1_Time6=='2') or (Char1_Time6=='3') or (Char1_Time6=='4') or (Char1_Time6=='5') or (Char1_Time6=='6') or (Char1_Time6=='7')or (Char1_Time6=='8') or (Char1_Time6=='9'):
            if (Char2_Time6 =='0') or (Char2_Time6 =='1') or (Char2_Time6=='2') or (Char2_Time6=='3') or (Char2_Time6=='4') or (Char2_Time6=='5') or (Char2_Time6=='6') or (Char2_Time6=='7')or (Char2_Time6=='8') or (Char2_Time6=='9'):
                MatchTime6=MatchTime_prev6=int(Char1_2_Time6)
                f6=1
        else:
            MatchTime6=MatchTime_prev6
            f6=0
        
        if (Team1name6[3]!='1'):
            Team1name6= Team1name_prev6
        else:
            if (f6==1):  
                Team1name_prev6=Team1name6[:3]    
            else:
                Team1name6= Team1name_prev6

        if (Team2name6[3]!='1'):
            Team2name6= Team2name_prev6
        else:
            if (f6==1):
                Team2name_prev6=Team2name6[:3]
            else:
                Team2name6= Team2name_prev6

       
    # End Name of the teams

    # Showing the Scores:
        if (f6==1):
            if (Score16[0]=='0') or (Score16[0]=='1') or (Score16[0]=='2') or (Score16[0]=='3') or (Score16[0]=='4') or (Score16[0]=='5') or (Score16[0]=='6') or (Score16[0]=='7') or (Score16[0]=='8') or (Score16[0]=='9'):
                if (int(Score16[0])<=(1+x16)):
                    x16=x1p6=int(Score16[0])
            else:
                x16=x1p6
        else:
            x16=x1p6
   

        if (f6==1):
            if (Score26[2]=='0') or (Score26[2]=='1') or (Score26[2]=='2') or (Score26[2]=='3') or (Score26[2]=='4') or (Score26[2]=='5') or (Score26[2]=='6') or (Score26[2]=='7') or (Score26[2]=='8') or (Score26[2]=='9'):
                if (int(Score26[2])<=(1+y16)):
                    y16=y1p6=int(Score26[2])
            else:
                y16=y1p6
        else:
            y16=y1p6
        try:
            f= open('D:\\TeamData.txt', 'a') 
            if (f.writable()==True):
        #with open('D:\\TeamData.txt', 'a') as f:
                f.write('\nI6    '+ Team1name6[:3]+'    '+Team2name6[:3]+'    '+ str(x16)+'    '+str(y16))
        except:
            pass
        time.sleep(0.3)

#########################################################################
    elif (var[6]=='G'):
        frameTime6 = frame6[110:180, 285:460]
        frameTeam1_name6 = frame6[110:180, 470:630]
        frameTeam2_name6 = frame6[110:180, 660:800]
        frame_Score16= frame6[185:315, 475:620]
        frame_Score26= frame6[185:315, 675:820]
        Game_Time6= pytesseract.image_to_string(frameTime6)
        Game_Time6=Game_Time6.rstrip('\n')
        Game_Time6=Game_Time6+"AAA"
        Team1name6 = pytesseract.image_to_string(frameTeam1_name6)
        Team1name6=Team1name6.rstrip('\n')# removing /n to add data after
        Team1name6=Team1name6+'1___'# adding data after that in case there is nothing to read 
        Team2name6 = pytesseract.image_to_string(frameTeam2_name6)
        Team2name6=Team2name6.rstrip('\n')
        Team2name6=Team2name6+'1___'
        Score16=pytesseract.image_to_string(frame_Score16, config=("-c tessedit"
                  "_char_whitelist=abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"
                  " --psm 10"
                  " -l osd"
                  " "))
        Score16=Score16.rstrip('\n')# Removing /n from data 
        Score16=Score16+"AAA"
        Score26=pytesseract.image_to_string(frame_Score26, config=("-c tessedit"
                  "_char_whitelist=abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"
                  " --psm 10"
                  " -l osd"
                  " "))
        Score26=Score26.rstrip('\n')# Removing /n from data 
        Score26=Score26+"AAA"

    #///////////////////////////////////////////////////////////////
    # Showing Time of the Match
        Char1_Time6= Game_Time6[:1] 
        Char2_Time6=Game_Time6[1:2] 
        Char3_Time6=Game_Time6[2:3]
        Char1_2_Time6= Game_Time6[:2] 
        if  (Char1_Time6 =='0') or (Char1_Time6 =='1') or (Char1_Time6=='2') or (Char1_Time6=='3') or (Char1_Time6=='4') or (Char1_Time6=='5') or (Char1_Time6=='6') or (Char1_Time6=='7')or (Char1_Time6=='8') or (Char1_Time6=='9'):
            if (Char2_Time6 =='0') or (Char2_Time6 =='1') or (Char2_Time6=='2') or (Char2_Time6=='3') or (Char2_Time6=='4') or (Char2_Time6=='5') or (Char2_Time6=='6') or (Char2_Time6=='7')or (Char2_Time6=='8') or (Char2_Time6=='9'):
                MatchTime6=MatchTime_prev6=int(Char1_2_Time6)
                f6=1
        else:
            MatchTime6=MatchTime_prev6
            f6=0

        if (Team1name6[3]!='1'):
            Team1name6= Team1name_prev6
        else:
            if (f6==1):
                Team1name_prev6=Team1name6[:3]
            else:
                Team1name6= Team1name_prev6

        if (Team2name6[3]!='1'):
            Team2name6= Team2name_prev6
        else:
            if (f6==1):
                Team2name_prev6=Team2name6[:3]
            else:
                Team2name6= Team2name_prev6

        if (Score16[0]=='0') or (Score16[0]=='1') or (Score16[0]=='2') or (Score16[0]=='3') or (Score16[0]=='4') or (Score16[0]=='5') or (Score16[0]=='6') or (Score16[0]=='7') or (Score16[0]=='8') or (Score16[0]=='9'):
            if (int(Score16[0])<=(1+x16)):
                x16=x1p6=int(Score16[0])
        elif (Score16[0]=='l'):
            if (x16<=1):
                x16=x1p6=1
        else:
            x16=x1p6
   


        if (Score26[0]=='0') or (Score26[0]=='1') or (Score26[0]=='2') or (Score26[0]=='3') or (Score26[0]=='4') or (Score26[0]=='5') or (Score26[0]=='6') or (Score26[0]=='7') or (Score26[0]=='8') or (Score26[0]=='9'):
            if (int(Score26[0])<=(1+y16)):
                y16=y1p6=int(Score26[0])
        elif (Score26[0]=='l'):
            if (y16<=1):
                y16=y1p6=1
        else:
            y16=y1p6
        try:
            f= open('D:\\TeamData.txt', 'a') 
            if (f.writable()==True):
        #with open('D:\\TeamData.txt', 'a') as f:
                f.write('\nG6    '+ Team1name6[:3]+'    '+Team2name6[:3]+'    '+ str(x16)+'    '+str(y16))
        except:
            pass
        time.sleep(0.3)

    elif (var[6]=='F'):
        frameTime6 = frame6[145:240, 200:445]
        frameTeam1_name6 = frame6[145:240, 500:820]
        frameTeam2_name6 = frame6[145:240, 1210:1570]
        frame_Score16= frame6[135:245,500:950]
        frame_Score26= frame6[135:245,1100:1570]
        Game_Time6= pytesseract.image_to_string(frameTime6)
        Game_Time6=Game_Time6.rstrip('\n')
        Game_Time6=Game_Time6+"AAA"
        Team1name6 = pytesseract.image_to_string(frameTeam1_name6)
        Team1name6=Team1name6.rstrip('\n')# removing /n to add data after
        Team1name6=Team1name6+'1___'# adding data after that in case there is nothing to read 
        Team2name6 = pytesseract.image_to_string(frameTeam2_name6)
        Team2name6=Team2name6.rstrip('\n')
        Team2name6=Team2name6+'1___'
        Score16=pytesseract.image_to_string(frame_Score16)
        Score16=Score16.rstrip('\n')# Removing /n from data 
        Score16='A'+Score16
        Score26=pytesseract.image_to_string(frame_Score26)
        Score26=Score26.rstrip('\n')# Removing /n from data 
        Score26=Score26+"AAA"

    #//////////////////////////////////////////////////////
    # Time of the game
        Char1_Time6= Game_Time6[:1] 
        Char2_Time6=Game_Time6[1:2] 
        Char3_Time6=Game_Time6[2:3]
        Char1_2_Time6= Game_Time6[:2] 
        if  (Char1_Time6 =='0') or (Char1_Time6 =='1') or (Char1_Time6=='2') or (Char1_Time6=='3') or (Char1_Time6=='4') or (Char1_Time6=='5') or (Char1_Time6=='6') or (Char1_Time6=='7')or (Char1_Time6=='8') or (Char1_Time6=='9'):
            if (Char2_Time6 =='0') or (Char2_Time6 =='1') or (Char2_Time6=='2') or (Char2_Time6=='3') or (Char2_Time6=='4') or (Char2_Time6=='5') or (Char2_Time6=='6') or (Char2_Time6=='7')or (Char2_Time6=='8') or (Char2_Time6=='9'):
                MatchTime6=MatchTime_prev6=int(Char1_2_Time6)
                f6=1
        else:
            MatchTime6=MatchTime_prev6
            f6=0

        if (Team1name6[0]=='1'):
            Team1name6= Team1name_prev6
        else:
            if (f6==1):
                Team1name_prev6=Team1name6[:3]
            else:
                Team1name6= Team1name_prev6

        if (Team2name6[0]=='1'):
            Team2name6= Team2name_prev6
        else:
            if (f6==1):
                Team2name_prev6=Team2name6[:3]
            else:
                Team2name6= Team2name_prev6

    
        if (Score16[-1]=='0') or (Score16[-1]=='1') or (Score16[-1]=='2') or (Score16[-1]=='3') or (Score16[-1]=='4') or (Score16[-1]=='5') or (Score16[-1]=='6') or (Score16[-1]=='7') or (Score16[-1]=='8') or (Score16[-1]=='9'):
            if (int(Score16[-1])<=(1+x16)):
                x16=x1p6=int(Score16[-1])

        elif(Score16[-1]=='G'):
             if ((x16<=4) and (x16>2)):
                x16=x1p6=4
        else:
            x16=x1p6
   
        if (Score26[0]=='0') or (Score26[0]=='1') or (Score26[0]=='2') or (Score26[0]=='3') or (Score26[0]=='4') or (Score26[0]=='5') or (Score26[0]=='6') or (Score26[0]=='7') or (Score26[0]=='8') or (Score26[0]=='9'):
            if (int(Score26[0])<=(1+y16)):
                y16=y1p6=int(Score26[0])

        elif(Score26[0]=='G'):
            if ((y16<=4) and (y16>2)):
                y16=y1p6=4
        else:
            y16=y1p6
        try:
            f= open('D:\\TeamData.txt', 'a') 
            if (f.writable()==True):
        #with open('D:\\TeamData.txt', 'a') as f:
                f.write('\nF6    '+ Team1name6[:3]+'    '+Team2name6[:3]+'    '+ str(x16)+'    '+str(y16))
        except:
            pass

        time.sleep(0.3)

    elif (var[6]=='R'):
        frameTime6 = frame6[110:180, 200:400]
        frameTeam1_name6 = frame6[110:180, 470:640]
        frameTeam2_name6 = frame6[110:180, 850:1010]
        frame_Score16= frame6[110:180, 660:835]
        frame_Score26= frame6[110:180, 660:835]
        #cv2.imshow('frame',frameTeam1_name)
        Game_Time6= pytesseract.image_to_string(frameTime6)
        Game_Time6=Game_Time6.rstrip('\n')
        Game_Tim6=Game_Time6+"AAA"
        Team1name6 = pytesseract.image_to_string(frameTeam1_name6)
        Team1name6=Team1name6.rstrip('\n')# removing /n to add data after
        Team1name6=Team1name6+'1___'# adding data after that in case there is nothing to read 
        Team2name6 = pytesseract.image_to_string(frameTeam2_name6)
        Team2name6=Team2name6.rstrip('\n')
        Team2name6=Team2name6+'1___'
        Score16=pytesseract.image_to_string(frame_Score16)
        Score16=Score16.rstrip('\n')# Removing /n from data 
        Score16=Score16+"AAA"
        Score26=pytesseract.image_to_string(frame_Score26)
        Score26=Score26.rstrip('\n')# Removing /n from data 
        Score26=Score26+"AAA"
    # Showing Time of the Match
        Char1_Time6= Game_Time6[:1] 
        Char2_Time6=Game_Time6[1:2] 
        Char3_Time6=Game_Time6[2:3]
        Char1_2_Time6= Game_Time6[:2] 
        if  (Char1_Time6 =='0') or (Char1_Time6 =='1') or (Char1_Time6=='2') or (Char1_Time6=='3') or (Char1_Time6=='4') or (Char1_Time6=='5') or (Char1_Time6=='6') or (Char1_Time6=='7')or (Char1_Time6=='8') or (Char1_Time6=='9'):
            if (Char2_Time6 =='0') or (Char2_Time6 =='1') or (Char2_Time6=='2') or (Char2_Time6=='3') or (Char2_Time6=='4') or (Char2_Time6=='5') or (Char2_Time6=='6') or (Char2_Time6=='7')or (Char2_Time6=='8') or (Char2_Time6=='9'):
                MatchTime6=MatchTime_prev6=int(Char1_2_Time6)
                f6=1
        else:
            MatchTime6=MatchTime_prev6
            f6=0
    # End Time of the Match
    
    #Showing the Name of the Teams
        if (Team1name6[3]!='1'):
            Team1name6= Team1name_prev6
        else:
            if (f6==1):
                Team1name_prev6=Team1name6[:3]
            else:
                Team1name6= Team1name_prev6

        if (Team2name6[3]!='1'):
            Team2name6= Team2name_prev6
        else:
            if (f6==1):
                Team2name_prev6=Team2name6[:3]
            else:
                Team2name6= Team2name_prev6
 
    # Showing the Scores:
        if (Score16[0]=='0') or (Score16[0]=='1') or (Score16[0]=='2') or (Score16[0]=='3') or (Score16[0]=='4') or (Score16[0]=='5') or (Score16[0]=='6') or (Score16[0]=='7') or (Score16[0]=='8') or (Score16[0]=='9'):
            if (int(Score16[0])<=(1+x16)):
                x16=x1p6=int(Score16[0])
        else:
            x16=x1p6
   
        if (Score26[2]=='0') or (Score26[2]=='1') or (Score26[2]=='2') or (Score26[2]=='3') or (Score26[2]=='4') or (Score26[2]=='5') or (Score26[2]=='6') or (Score26[2]=='7') or (Score26[2]=='8') or (Score26[2]=='9'):
            if (int(Score26[2])<=(1+y16)):
                y16=y1p6=int(Score26[2])
        else:
            y16=y1p6
        try:
            f= open('D:\\TeamData.txt', 'a') 
            if (f.writable()==True):
        #with open('D:\\TeamData.txt', 'a') as f:
                f.write('\nR6    '+ Team1name6[:3]+'    '+Team2name6[:3]+'    '+ str(x16)+'    '+str(y16))
        except:
            pass
        time.sleep(0.3)

    else:
        pass

###########################################################################################################################################
    print('done')
    k=cv2.waitKey(10) & 0xFF
    if k==27:
        break
cap0.release()
cap1.release()
cap2.release()
cap3.release()
cap4.release()
cap5.release()
cap6.release()
#cap7.release()
cv2.destroyAllWindows()

