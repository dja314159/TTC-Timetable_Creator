import pickle

from urllib.request import urlopen
from bs4 import BeautifulSoup
import os

def crawling(html):
    soup = BeautifulSoup(html, "html.parser")

    data = soup.find_all('tr')

    table = []  # 크롤링한 데이터들을 담아 둘 리스트

    table_sliced = []  # 필요한것만 슬라이싱해서 담아 둘 리스트

    colInfo = []  # 학년, 과목명 등을 담은 첫번째 행

    subject = []  # 과목 정보를 담을 리스트

    # 첫 row에 있는걸 받아와서 리스트에 넣어두고, 그 다음줄부터 돌면서 리스트에 저장된걸 key 값으로해서 subject에 저장한다.

    for row in data:
        table.append(row.get_text().split())

    for line in table[0][0:9]:  # 필요없는 데이터 제거하는 과정
        colInfo.append(line)
    for line in table[0][-6:-1]:
        colInfo.append(line)

    del table[0]

    for line in table:  # 비고 부분 제거하고 필요없는 데이터 제거해서 저장
        if line[-1] != 'Y' and line[-1] != 'N':
            del line[-1]
        temp = []
        for data in line[0:9]:
            temp.append(data)
        for data in line[-5:-1]:
            temp.append(data)
        table_sliced.append(temp)

    for row in table_sliced:
        colNum = 0
        line = {}
        for col in row:
            key = colInfo[colNum]
            line[key] = col
            colNum += 1
        subject.append(line)

    return subject

if __name__ == "__main__":

    # html_com = urlopen(
    #     "http://my.knu.ac.kr/stpo/stpo/cour/listLectPln/list.action?search_open_crse_cde=1O02&sub=1O&search_open_yr_trm=20202")
    # html_glso = urlopen(
    #     "http://my.knu.ac.kr/stpo/stpo/cour/listLectPln/list.action?search_open_crse_cde=1O0204&sub=1O&search_open_yr_trm=20202")
    #
    # com = dict()
    # glso = dict()
    #
    # com = crawling(html_com)
    # glso = crawling(html_glso)

    # 읽어오기
    file = open("COM.bin", "rb")
    content_com = pickle.load(file)

    # 읽어오기
    file = open("GLSO.bin", "rb")
    content_glso = pickle.load(file)


    for i in range(0,len(content_com)):
        content_com[i]["selected"] = "N"


    for i in range(0,len(content_glso)):
        content_glso[i]["selected"] = "N"

    for lec in content_com:
        if lec["교과목번호"] == "MTED231002":
            lec["담당교수"] = "아난드 폴"
            lec["강의시간"] = "월2B,3A,3B수1A,1B,2A"
        elif lec["교과목번호"] == "COME301012":
            lec["담당교수"] = "아난드 폴"
            lec["강의시간"] = "월1A,1B,2A수2B,3A,3B"
        elif lec["교과목번호"] == "COMP432001":
            lec["교과목명"] = "소프트웨어 특강"
            lec["학점"] = "2"
            lec["강의"] = "2"
            lec["실습"] = "0"
            lec["담당교수"] = "정원일"
            lec["강의시간"] = "화5A,5B화6A,6B"

    for lec in content_glso:
        if lec["교과목번호"] == "STUP212002":
            lec["교과목명"] = "창업과 경영"
            lec["학점"] = "3"
            lec["강의"] = "3"
            lec["실습"] = "0"
            lec["담당교수"] = "박귀정"
            lec["강의시간"] = "화7A,7B,8A목7A,7B,8A"


    # 심컴 쓰기
    file = open("COM.bin", "wb+")
    pickle.dump(content_com, file)
    file.close()

    #글솝 쓰기
    file=open("GLSO.bin","wb+")
    pickle.dump(content_glso,file)
    file.close()




    #읽어오기
    file=open("COM.bin","rb")
    content_com = pickle.load(file)

    #읽어오기
    file=open("GLSO.bin","rb")
    content_glso = pickle.load(file)


    for lecture in content_com:
        print(lecture)

    for lecture in content_glso:
        print(lecture)



