# 웹크롤링 관련 자료 

https://www.slideshare.net/wangwonLee/2018-datayanolja-moreeffectivewebcrawling


https://nittaku.tistory.com/136?category=727207

https://webnautes.tistory.com/779

구글 검색 : 파이썬 동적 웹페이지 크롤링



https://l0o02.github.io/2018/06/09/python-crawling-1_copy0/



https://www.fun-coding.org/crawl_advance5.html  -xpath 를 이용한 크롤링 
https://fabl1106.github.io/python/2019/04/25/%ED%8C%8C%EC%9D%B4%EC%8D%AC-22.-%EB%8F%99%EC%A0%81%ED%81%AC%EB%A1%A4%EB%A7%81(Ajax,-JSON).html



# 웹크롤링 기본 - CSS Selector를 사용한 크롤링
https://www.fun-coding.org/crawl_basic4.html


# 웹사이트 크롤링 DB에 저장하기
https://uslifelog.tistory.com/54


# 프로그래머스 채용정보 사이트 분석 
- 정적웹크롤링이 가능함 
- https://programmers.co.kr/job?page=1 채용정보가 페이징 요청형태로 요청하며 렌더링되서 호출된다. 
- 페이지끝마지막 정보가 아래의 태그형태로 나타난다. 
```
<div  class="d-flex justify-content-center"  id="paginate">

<nav  class="pagination"><ul  class="pagination"><li  class="prev previous_page disabled page-item"><a  class="page-link"  href="#">이전</a></li>  <li  class="active page-item"><a  class="page-link"  href="/job?page=1">1</a></li>  <li  class="page-item"><a  rel="next"  class="page-link"  href="/job?page=2">2</a></li>  <li  class="page-item"><a  class="page-link"  href="/job?page=3">3</a></li>  <li  class="page-item"><a  class="page-link"  href="/job?page=4">4</a></li>  <li  class="page-item"><a  class="page-link"  href="/job?page=5">5</a></li>  <li  class="page-item disabled"><a  class="page-link"  href="#">…</a></li>  <li  class="page-item"><a  class="page-link"  href="/job?page=18">18</a></li>  <li  class="next next_page page-item"><a  class="page-link"  rel="next"  href="/job?page=2">다음</a></li></ul></nav>

</div>

```