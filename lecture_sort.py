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

    # 지금은 bin 파일이 준비되어 있지 않으니 바로 긁어오자

    html_com = urlopen("http://my.knu.ac.kr/stpo/stpo/cour/listLectPln/list.action?search_open_crse_cde=1O02&sub=1O&search_open_yr_trm=20202")
    html_glso = urlopen("http://my.knu.ac.kr/stpo/stpo/cour/listLectPln/list.action?search_open_crse_cde=1O0204&sub=1O&search_open_yr_trm=20202")

    com = dict()
    glso = dict()
    test_data = list()

    major_imp = list()
    major = list()
    major_with_imp = list()
    culture = list()
    teacher = list()

    result_list = list()

    com_major_imp_list = ["수학 I","물리학 I","물리학실험 I","이산수학",\
                      "프로그래밍기초", "기초창의공학설계", "자료구조", "자바프로그래밍"\
                      "컴퓨터구조", "시스템프로그래밍", "운영체제", "알고리즘1", "종합설계프로젝트1",\
                      "종합설계프로젝트2"]

    glso_major_imp_list = ["프로그래밍기초", "자료구조", "알고리즘실습", "운영체제"]


    com = crawling(html_com)
    glso = crawling(html_glso)

    for lecture in com:
        test_data.append(lecture)

    for lecture in glso:
        test_data.append(lecture)

    test_data = sorted(test_data, key=(lambda x: x['교과목명']))


    #전공필수 저장
    for lecture in test_data:
        if lecture['교과목명'] in com_major_imp_list or lecture['교과목명'] in glso_major_imp_list: #일단 심컴, 글솝 전공필수 둘다 저장함
            major_imp.append(lecture)
        elif lecture['교과구분'] == '전공' or lecture['교과구분'] == '공학전공' or lecture['교과구분'] == '전공기반':
            major.append(lecture)
        elif lecture['교과구분'] == '교양' or lecture['교과구분'] == '일반선택' or lecture['교과구분'] == '기본소양':
            culture.append(lecture)
        else:
            teacher.append(lecture)

    major_with_imp = major_imp

    for lecture in major:
        major_with_imp.append(lecture)




    print("정렬기준을 입력하세요")
    print("전공필수 : a, 전공 : b, 교양 : c, 교직 : d")


    sel = input()



    if sel == "a": #전공필수 - 전공 - 교양 - 교직 순으로 정렬
        for lecture in major_imp:
            result_list.append(lecture)
        for lecture in major:
            result_list.append(lecture)
        for lecture in culture:
            result_list.append(lecture)
        for lecture in teacher:
            result_list.append(lecture)

    elif sel == "b": #전공 with 전공필수 - 교양 - 교직 순으로 정렬
        for lecture in major_with_imp:
            result_list.append(lecture)
        for lecture in culture:
            result_list.append(lecture)
        for lecture in teacher:
            result_list.append(lecture)

    elif sel == "c": #교양 - 전공 with 전공필수 - 교직 순으로 정렬
        for lecture in culture:
            result_list.append(lecture)
        for lecture in major_with_imp:
            result_list.append(lecture)
        for lecture in teacher:
            result_list.append(lecture)

    elif sel == "d": # 교직 - 교양 - 전공 with 전공필수 순으로 정렬
        for lecture in teacher:
            result_list.append(lecture)
        for lecture in major_with_imp:
            result_list.append(lecture)
        for lecture in culture:
            result_list.append(lecture)

    for lecture in result_list:
        print(lecture)










