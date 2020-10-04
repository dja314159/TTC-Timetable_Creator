#!/usr/bin/env python3

from ctypes import*

time = [[0] * 6]*18 # am9~pm6, mon~fri, 1 index = 30min

for i in time:
    for j in i:
          j = "0" # make array index all 0. 0 means there is no class in that time.

timealpa = [[0]*18] # transform the time (ex: 2A -> 10:00) we will save starting time.
timenum = [[0]*18]
startclass = 9
timeday = [[0]*6]
timeday[0][0] = '월'
timeday[0][1] = '화'
timeday[0][2] = '수'
timeday[0][3] = '목'
timeday[0][4] = '금'
timeday[0][5] = '토'
mainclass = 0
subclass = 0
timecount = 0
timecheck = list()
daycount = 0
daycheck = list()
data = list()

class class_info(Structure):
    _fields_ = [('classname',c_char*30),('classnum',c_char*30),('grade',c_char),('gradepoint',c_char),('classbeginf',c_char),('classendf',c_char),('classbegins',c_char),('classends',c_char),('classdatef',c_char*4),('classdates',c_char*4),('kind',c_char*30),('max',c_char),('now',c_char)]

#we will check the time using classbegin and classend. And first option is grade and kind, and then grade, time.

mainclass, subclass = input('write ur class(main sub):  ').split()

for i in range(1):
    for j in range(18):
            if j%2 == 0:
                timealpa[i][j] = str((j//2)+1) + 'A'
            else:
                timealpa[i][j] = str((j//2)+1) + 'B'

for i in range(1):
    for j in range(18):
        timenum[i][j] = str(startclass)
        startclass = startclass + 0.5

f = open("2020_CS.txt", 'r')

while True:
    line = f.readline()
    if not line:
        break
    for k in range(18):
        result = line.find(timealpa[0][k])
        if result == -1:
            continue
        else:
            for m in range(18):
                timecheck.append(timenum[0][k])
                timecount = timecount + 1

    for k in range(6):
        cuttingline = line.split("'")
        dayresult = cuttingline[35].find(timeday[0][k])
        if dayresult == -1:
            continue
        else:
            daycheck.append(timeday[0][k])
            daycount = daycount + 1
           
    if daycount == 2:
        data.append(class_info(cuttingline[15],cuttingline[11],cuttingline[3],cuttingline[23],timecheck[0],timecheck[2],timecheck[3],timecheck[5],daycheck[0],daycheck[1],cuttingline[7],cuttingline[47],cuttingline[43]))
    else:
        data.append(class_info(str(cuttingline[15]),str(cuttingline[11]),str(cuttingline[3]),str(cuttingline[23]),str(timecheck[0]),str(timecheck[2]),0,0,str(daycheck[1]),'none',str(cuttingline[7]),str(cuttingline[47]),str(cuttingline[43])))
    
    print(cuttingline[11])
    print(cuttingline[23])
    print(cuttingline[3])
    print(cuttingline[7])
    print(cuttingline[47])
    print(cuttingline[43])
    print(done)

f.close()

