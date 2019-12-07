import time

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.wait import WebDriverWait


options = Options()
options.headless = True
browser = webdriver.Chrome(executable_path="./chromedriver",options=options)
browser.get("https://datalab.naver.com/shoppingInsight/sCategory.naver")


time.sleep(3)

tag_names = browser.find_elements_by_css_selector(".rank_top1000_list li")
#find_element_by_css_selector(".rank_top1000_list").
print(tag_names)
for tag in tag_names:
    print(tag.text)



# from selenium import webdriver
# from selenium.webdriver.chrome.options import Options
# from selenium.webdriver.support.wait import WebDriverWait
# import time
# options = Options()
# options.headless = True
# browser = webdriver.Chrome(executable_path="./chromedriver",options=options)
# browser.get("http://python.org")
 
# menus = browser.find_elements_by_css_selector('#top ul.menu li')
# print(menus)
# pypi = None
# for m in menus:
#     if m.text == "PyPI":
#         pypi = m
#     print(m.text)
 
# pypi.click()  # 클릭
 
# time.sleep(5) # 5초 대기
# browser.quit() # 브라우저 종료