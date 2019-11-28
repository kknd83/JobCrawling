from bs4 import BeautifulSoup
from urllib.request import urlopen
import requests



html = urlopen("https://programmers.co.kr/job?page=1")
soupObject = BeautifulSoup(html, "html.parser")


#print(bsObject) 


#divList = bsObject.find("div",{'id':'list-positions-wrapper'})

#print(divList)

#pcount = bsObject.select("#list-positions-wrapper>.list-positions-header>.label-list-positions")
#ullist = bsObject.select("#list-positions-wrapper .list-positions")
#print(ullist)
#print("######################################")
#print(pcount[0].get_text())




# page_list = soupObject.findAll('a', {'class': 'page-link'})
# print(page_list)

page_list = soupObject.findAll('a', {'class': 'page-link'})

#스트링에 숫자인지 아닌지 판별하는 함수
def is_number(num):
    try:
        judge = str(float(num))
        return False if(judge=='nan' or judge=='inf' or judge =='-inf') else True
    except ValueError: #num을 float으로 변환 할 수 없는 경우
        return False

maximum = 0
page = 1


for atag in page_list:
    str1 = atag.text
    if is_number(str1):
        tmp = int(str1)
        if maximum < tmp:
            maximum = tmp

print("총 " + str(maximum) + " 개의 페이지가 확인 됬습니다.")


whole_source = ""
for page_number in range(1, maximum+1):
    URL = 'https://programmers.co.kr/job?page=' + str(page_number)
    print(URL)
    response = requests.get(URL)
    whole_source = whole_source + response.text
soup = BeautifulSoup(whole_source, 'html.parser')

print(len(soup))
find_title = soup.select("h5.company-name")
#position_job = soup.select("h4.position-title>a")
print(len(find_title))
print(find_title)
for title in find_title:
 	print(title.text)


# 여러데이터 한꺼번에 파싱하기
#https://book.coalastudy.com/data-crawling/week-5/pre