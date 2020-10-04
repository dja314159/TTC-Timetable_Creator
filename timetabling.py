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
    _fields_ = [('grade',c_int),('gradepoint',c_int),('classbeginf',c_int),('classendf',c_int),('classbegins',c_int),('classends',c_int),('classdatef',c_int),('classdates',c_int),('kind',c_int),('max',c_int),('now',c_int)]

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
            daycheck.append(k)
            daycount = daycount + 1

    if daycount == 2:
        data.append(class_info(int(cuttingline[3]),int(cuttingline[23]),int(timecheck[0]),int(timecheck[2]),int(timecheck[3]),int(timecheck[5]),int(daycheck[0]),int(daycheck[1]),1,int(cuttingline[47]),int(cuttingline[43])))
    else:
        data.append(class_info(int(cuttingline[3]),int(cuttingline[23]),int(timecheck[0]),int(timecheck[2]),0,0,int(daycheck[1]),10,0,int(cuttingline[47]),int(cuttingline[43])))

    print('asdf')

f.close()

