from bs4 import BeautifulSoup
from urllib.request import urlopen


html = urlopen("https://programmers.co.kr/job?page=1")
bsObject = BeautifulSoup(html, "html.parser")


#print(bsObject) 


divList = bsObject.find("div",{'id':'list-positions-wrapper'})

#print(divList)


pcount = bsObject.select("#list-positions-wrapper>.list-positions-header>.label-list-positions")

ullist = bsObject.select("#list-positions-wrapper .list-positions")

print(ullist)

print("######################################")
print(pcount[0].get_text())