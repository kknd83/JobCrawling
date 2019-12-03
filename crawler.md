# 웹크롤링 관련 자료 

https://www.slideshare.net/wangwonLee/2018-datayanolja-moreeffectivewebcrawling


https://nittaku.tistory.com/136?category=727207

https://webnautes.tistory.com/779

구글 검색 : 파이썬 동적 웹페이지 크롤링

네이버와 함께 정복하는 크롤링 스터디
https://book.coalastudy.com/data-crawling/week-3/stage-3

https://www.fun-coding.org/crawl_advance5.html  -xpath 를 이용한 크롤링 
https://fabl1106.github.io/python/2019/04/25/%ED%8C%8C%EC%9D%B4%EC%8D%AC-22.-%EB%8F%99%EC%A0%81%ED%81%AC%EB%A1%A4%EB%A7%81(Ajax,-JSON).html




# 프로그래머스 채용정보 사이트 분석 
- 정적웹크롤링이 가능함 
- https://programmers.co.kr/job?page=1 채용정보가 페이징 요청형태로 요청하며 렌더링되서 호출된다. 
- 페이지끝마지막 정보가 아래의 태그형태로 나타난다. 
```
<div  class="d-flex justify-content-center"  id="paginate">

<nav  class="pagination"><ul  class="pagination"><li  class="prev previous_page disabled page-item"><a  class="page-link"  href="#">이전</a></li>  <li  class="active page-item"><a  class="page-link"  href="/job?page=1">1</a></li>  <li  class="page-item"><a  rel="next"  class="page-link"  href="/job?page=2">2</a></li>  <li  class="page-item"><a  class="page-link"  href="/job?page=3">3</a></li>  <li  class="page-item"><a  class="page-link"  href="/job?page=4">4</a></li>  <li  class="page-item"><a  class="page-link"  href="/job?page=5">5</a></li>  <li  class="page-item disabled"><a  class="page-link"  href="#">…</a></li>  <li  class="page-item"><a  class="page-link"  href="/job?page=18">18</a></li>  <li  class="next next_page page-item"><a  class="page-link"  rel="next"  href="/job?page=2">다음</a></li></ul></nav>

</div>

```

# 파이썬 크롤링한 결과 엑셀에 저장하기 
http://blog.naver.com/PostView.nhn?blogId=kiddwannabe&logNo=221274278923&parentCategoryNo=&categoryNo=35&viewDate=&isShowPopularPosts=false&from=postView


# 웹크롤링 기본 - CSS Selector를 사용한 크롤링
https://www.fun-coding.org/crawl_basic4.html

# 파이썬 페이징 크롤링
https://l0o02.github.io/2018/06/14/python-crawling-pagination-1/

# 웹사이트 크롤링 DB에 저장하기
https://uslifelog.tistory.com/54


# 파이썬 예외처리
https://wayhome25.github.io/python/2017/02/26/py-12-exception/

# 파이썬 들여쓰기 오류
unindent does not match any outer indentation level
https://programmers.co.kr/learn/questions/477


# 파이썬 가상환경 
https://woolbro.tistory.com/25
https://woolbro.tistory.com/26
https://woolbro.tistory.com/27

# 파이썬 가상환경 설치방법
- python -m venv "가상환경이름"
- python -p python3 "가상환경이름"
- cmd 창을 열어서 가상환경 설치디렉토리로 이동후 activate 실행한다. (windows)
- source 디렉토리명/activate (mac)
- 패키지 검색 (pythonBasic)pip search simplejson
- 패지시 설치 (pythonBasic)pip install simplejson
- 패키지 리스트 출력 (pythonBasic)pip list
- 가상환경 사용하기 가상환경 실행후 (pythonBasic) code   VSCode를 실행한다.
- 패키지 목록 저장하기 (pythonBasic)pip freeze > fileList.txt
- 패키지 목록-> 재설치 (pythonBasic)pip install -r fileList.txt

