# coding = utf-8

from flask import Flask,render_template
import pickle


app = Flask(__name__)

def lecture_collect():
    #원래는 웹에서 정보를 받아오지만 test용으로 인자 미리 지정
    major = 2 #1: 심컴, 2: 글솝
    grade = 2
    avoid_day = 16 #2^4 -> 금요일
    avoid_time = 3 #2^0 + 2^1 -> 1A, 1B

    # if문으로 글솝, 심컴 결정하고 필요한 바이너리 파일 읽어오기
    if major == 1:
        # 읽어오기
        file = open("COM.bin", "rb")
        data = pickle.load(file)
    else:
        # 읽어오기
        file = open("GLSO.bin", "rb")
        data = pickle.load(file)


    #기피 요일과 시간 2진수로 바꾸고 리스트로 다시 전환
    avoid_day_bin = format(avoid_day,'b')
    avoid_time_bin = format(avoid_time,'b')

    avoid_day_list = list(str(avoid_day_bin))
    avoid_time_list = list(str(avoid_time_bin))

    day_len = len(avoid_day_list)
    time_len = len(avoid_time_list)




    # for문 돌면서 '학년'  =  grade 인거 리스트에 append
    temp_lecture = list()
    for lect in data:
        if lect["학년"] == str(grade):
            temp_lecture.append(lect)

    for lect in temp_lecture:
        print(lect)

    print("-----------------------------------------------------------------------------------------------")

    #바이너리로 만들어진 기피 요일 정보룰룰 while문돌면서 리스트에 넣기
    i=-1
    day_list = list()
    temp = ""
    while(True):
        if day_len+1 == -i:
            break
        if avoid_day_list[i] == '1':

            if -i == 1:
                temp = "월"
            elif -i == 2:
                temp = "화"
            elif -i == 3:
                temp = "수"
            elif -i == 4:
                temp = "목"
            elif -i == 5:
                temp = "금"

            day_list.append(temp)
        i -= 1


    i -= 1


    # for문 돌면서 강의 시간에 기피 요일 없는것만 새 리스트에 삽입
    temp_list = list()
    for lect in temp_lecture:
        check = 0
        for day in day_list:
            if lect["강의시간"].find(day) != -1:
                check += 1
        if check == 0:
            temp_list.append(lect)

    temp_lecture = temp_list

    for lect in temp_lecture:
        print(lect)

    print("---------------------------------------------------------------------------------------------------------------")



    # 바이너리로 만들어진 기피 시간 정보룰룰 while문돌면서 리스트에 넣기
    i = -1
    time_list = list()
    temp = ""
    while(True):
        if time_len+1 == -i:
            break
        if avoid_time_list[i] == '1':
            if -i == 1:
                temp = "1A"
            elif -i == 2:
                temp = "1B"
            elif -i == 3:
                temp = "2A"
            elif -i == 4:
                temp = "2B"
            elif -i == 5:
                temp = "3A"
            elif -i == 6:
                temp = "3B"
            elif -i == 7:
                temp = "4A"
            elif -i == 8:
                temp = "4B"
            elif -i == 9:
                temp = "5A"
            elif -i == 10:
                temp = "5B"
            elif -i == 11:
                temp = "6A"
            elif -i == 12:
                temp = "6B"
            elif -i == 13:
                temp = "7A"
            elif -i == 14:
                temp = "7B"
            elif -i == 15:
                temp = "8A"
            elif -i == 16:
                temp = "8B"
            elif -i == 17:
                temp = "9A"
            elif -i == 18:
                temp = "9B"
            elif -i == 19:
                temp = "10A"
            elif -i == 20:
                temp = "10B"
            elif -i == 21:
                temp = "11A"
            elif -i == 22:
                temp = "11B"
            elif -i == 23:
                temp = "12A"
            elif -i == 24:
                temp = "12B"
            elif -i == 25:
                temp = "13A"
            elif -i == 26:
                temp = "13B"
            elif -i == 27:
                temp = "14A"
            time_list.append(temp)
        i -= 1



    # for문 돌면서 강의 시간에 기피 시간 없는것만 새 리스트에 삽입
    temp_list = list()
    for lect in temp_lecture:
        check = 0
        for time in time_list:
            if lect["강의시간"].find(time) != -1:
                check += 1
        if check == 0:
            temp_list.append(lect)

    lecture = temp_list

    for lect in lecture:
        print(lect)










@app.route("/")
def init():
    return render_template("index.html")

@app.route("/index.html")
def home():
    return render_template("index.html")

@app.route("/TTC.html")
def option():
    return render_template("TTC.html")

@app.route("/table.html")
def table():
    return render_template("table.html")

@app.route("/List.html")
def list_():
    return render_template("List.html")




if __name__ == "__main__":
    lecture_collect()
    app.run()
