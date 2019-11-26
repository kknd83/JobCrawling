from bs4 import BeautifulSoup
from urllib.request import urlopen


html = urlopen("https://programmers.co.kr/job?page=1")
bsObject = BeautifulSoup(html, "html.parser")

print(bsObject)