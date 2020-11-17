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
usergrade = 0
timecount = 0
timecheck = [[0] * 9 ]* 100
daycount = 0
daycheck = [[-1]*7]*400
data = list()
classname = list()
classnum = list()
datacount = 0
gradelist = list()
mclass = list()
sclass = list()

class class_info(Structure):
    _fields_ = [('grade',c_int),('gradepoint',c_int),('classbeginf',c_float),('classendf',c_float),('classbegins',c_float),('classends',c_float),('classdatef',c_float),('classdates',c_int),('kind',c_int),('max',c_int),('now',c_int)]

#we will check the time using classbegin and classend. And first option is grade and kind, and then grade, time.

mainclass, subclass, usergrade= input('write ur class(main sub)and grade:  ').split()

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

print(timenum)

while True:
    line = f.readline()
    timeshort = 0
    if not line:
        break
    cuttingline = line.replace("월",",").replace("화",",").replace("수",",").replace("목",",").replace("금",",").replace("토",",").split(",")
    for m in cuttingline:
        for k in range(18):
            result = m.find(timealpa[0][k])
            if result == -1:
                continue
            else:
                timecheck[timecount][timeshort] = timenum[0][k]
                timeshort = timeshort + 1
    print(timecheck[timecount])
    
    timecount = timecount + 1

    daycount = 0

    for k in range(6):
        cuttingline = line.split("'")
        dayresult = cuttingline[35].find(timeday[0][k])
        if dayresult == -1:
            continue
        else:
            for m in range(daycount+1):
                if daycheck[datacount][m] == k:
                    continue
                else:
                    daycheck[datacount][daycount] = k
                    daycount = daycount + 1
    
    print(cuttingline[35])
    print()

    if daycount == 2:
        data.append(class_info(int(cuttingline[3]),int(cuttingline[23]),float(timecheck[timecount][0]),float(timecheck[timecount][2]),float(timecheck[timecount][3]), float(timecheck[timecount][5]),int(daycheck[datacount][0]),int(daycheck[datacount][1]),0,int(cuttingline[47]),int(cuttingline[43])))
    else:
        data.append(class_info(int(cuttingline[3]),int(cuttingline[23]),float(timecheck[timecount][0]),float(timecheck[timecount][7]),0,0,int(daycheck[datacount][0]),10,1,int(cuttingline[47]),int(cuttingline[43])))

    classname.append(cuttingline[15])
    classnum.append(cuttingline[11])

    datacount = datacount + 1

for i in range(int(datacount)):
    if int(usergrade) == data[i].grade:
        gradelist.append(i)

print(gradelist)

for i in gradelist:
    print(classnum[i])
    print(data[i].classbeginf)

for i in gradelist:
    if data[i].kind == 0:
        sclass.append(i)
    else:
        mclass.append(i)


f.close()

