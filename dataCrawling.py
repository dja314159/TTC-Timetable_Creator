from urllib.request import urlopen
from bs4 import BeautifulSoup
import os

def crawling(f,html):
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
    print(colInfo)

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

    for line in subject:
        print(line)
        f.write(str(line))
        f.write("\n")

    f.close()

def com_com():
    f = open("data/2020_심컴.txt", 'w', encoding='utf-8')
    html = urlopen("http://my.knu.ac.kr/stpo/stpo/cour/listLectPln/list.action?search_open_crse_cde=1O02&sub=1O&search_open_yr_trm=20202")
    crawling(f,html)

def com_glso():
    f = open("data/2020_글솝.txt", 'w', encoding='utf-8')
    html = urlopen("http://my.knu.ac.kr/stpo/stpo/cour/listLectPln/list.action?search_open_crse_cde=1O0204&sub=1O&search_open_yr_trm=20202")
    crawling(f,html)

def cul_read():
    f = open("data/2020_첨성인기초_독서와토론.txt", 'w', encoding='utf-8')
    html = urlopen("http://my.knu.ac.kr/stpo/stpo/cour/listLectPln/list.action?search_subj_area_cde=1A01&search_open_yr_trm=20202")
    crawling(f,html)

def cul_think():
    f = open("data/2020_첨성인기초_사고교육.txt", 'w', encoding='utf-8')
    html = urlopen("http://my.knu.ac.kr/stpo/stpo/cour/listLectPln/list.action?search_subj_area_cde=1A02&search_open_yr_trm=20202")
    crawling(f,html)

def cul_write():
    f = open("data/2020_첨성인기초_글쓰기.txt", 'w', encoding='utf-8')
    html = urlopen("http://my.knu.ac.kr/stpo/stpo/cour/listLectPln/list.action?search_subj_area_cde=1A03&search_open_yr_trm=20202")
    crawling(f,html)

def cul_eng():
    f = open("data/2020_첨성인기초_실용영어.txt", 'w', encoding='utf-8')
    html = urlopen("http://my.knu.ac.kr/stpo/stpo/cour/listLectPln/list.action?search_subj_area_cde=1A04&search_open_yr_trm=20202")
    crawling(f,html)

def cul_sw():
    f = open("data/2020_첨성인기초_소프트웨어.txt", 'w', encoding='utf-8')
    html = urlopen("http://my.knu.ac.kr/stpo/stpo/cour/listLectPln/list.action?search_subj_area_cde=1A05&search_open_yr_trm=20202")
    crawling(f,html)

def cul():
    cul_sw()
    cul_think()
    cul_eng()
    cul_write()
    cul_read()

if __name__ == "__main__":

    path = "/data"

    if not os.path.exists(path):
        os.makedirs("data", exist_ok=True)  # 분석정보를 저장하기 위한 폴더 생성
    com_com()
    com_glso()
    #cul()






