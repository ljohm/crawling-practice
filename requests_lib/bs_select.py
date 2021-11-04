import requests
from bs4 import BeautifulSoup

# 메서드를 사용한 웹페이지 파싱 첫번째
# bs.select(선택자)
# -> 선택자를 사용하여 html 문서의 트리구조를 적용하여 태그를 찾을 수 있음

url = "https://navercomp.wisereport.co.kr/v2/company/c1010001.aspx?cmp_cd=035720" #접속할 URL 주소
res = requests.get(url) #requests로 해당 URL주소에 정보 요청
res.raise_for_status() #응답이 OK로 오지않을 경우 에러발생

soup = BeautifulSoup(res.text, "html.parser") #응답으로 온 문서를 읽을 수 있게 parsing. (parsing 대상, parser 종류)
# parser 종류
# 1. lxml: c로 만들어져서 속도 빠름(별도 설치 필요) v
# 2. html4lib: 파이썬으로 만들어졌고 lxml보다는 느림
# 3. html.parser: 파이썬 버전을 확인하여 사용 v

per_value = soup.select("#wrapper > div.fund.fl_le > table > tbody > tr:nth-child(1) > td:nth-child(2)") #bs4의 select()를 이용해서 HTML 구문을 가져옴. select(선택자)
pbr_value = soup.select("#wrapper > div.fund.fl_le > table > tbody > tr:nth-child(2) > td:nth-child(2)")

print("PER : ", per_value[0].text) # .text === .get_text() # 차이가 있다면 get_text에 속성 추가하여 출력할 수 있다는 점
print("PBR : ", pbr_value[0].text)

# 주의 - 긁어오려는 문서 내용이 iframe 위에 있는지 확인 필요. iframe 위에 있다면 iframe의 주소를 가져와야함.