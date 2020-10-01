#!/usr/bin/env python3

time = [[0] * 6]*18 # am9~pm6, mon~fri, 1 index = 30min

for i in time:
    for j in i:
          j = "0" # make array index all 0. 0 means there is no class in that time.

timealpa = [[0]*18] # transform the time (ex: 2A -> 10:00) we will save starting time.
timenum = [[0]*18]
startclass = 9

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
            print(timealpa[0][k])
    print()

f.close()

