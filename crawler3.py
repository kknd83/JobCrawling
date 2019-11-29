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
html = BeautifulSoup(whole_source, 'html.parser')

#

#print(len(infos))


idx=0
for tag in html.select('#list-positions-wrapper'):
    company_names = tag.select("h5.company-name")
    position_names = tag.select("h4.position-title>a")
    experiences = tag.select("ul.company-info>li.experience")
    locations = tag.select("ul.company-info>li.location")
    
    #print(company_names)
    #print(position_names)

    for i in range(1, len(company_names),1):
        print(company_names[i].text +" , "+position_names[i].text +" , "+experiences[i].text.strip()+","+locations[i].text.strip())
        


#find_title = soup.select("h5.company-name")

#print(len(find_title))
#print(find_title)




# for info in infos:
#     company_name = info.select("h5.company-name")
#     position_name = info.select("h4.position-title>a")
    # print(company_name)
    # print(position_name)
    #print("#######")
    
    #print(company_name)
    #print(position_name)


# 여러데이터 한꺼번에 파싱하기
#https://book.coalastudy.com/data-crawling/week-5/pre

#19.11.29일  여러데이터 한꺼번에 파싱 좀더 좋은에제 - 네이버 블로그 크롤링 해보기 
#https://software-creator.tistory.com/20