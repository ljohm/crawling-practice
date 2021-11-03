import requests
from bs4 import BeautifulSoup

# 메서드를 사용한 웹페이지 파싱 두번째
# bs.find(태그명, 속성 정보)
# -> 주어진 기준에 맞는 태그를 찾아옴

url = "https://navercomp.wisereport.co.kr/v2/company/c1010001.aspx?cmp_cd=035720"
res = requests.get(url)
res.raise_for_status()

soup = BeautifulSoup(res.text, "html.parser")
crawling = soup.find("tbody")

print("해당 태그 내용만: ", crawling)
print("태그 제외한 텍스트만: ", crawling.get_text()) # .string과는 다르게 유니코드 형식으로 텍스트를 문자열로 반환하기 때문에 태그 안에 내용이 없으면 공백으로 출력됨
print("문자열만: ", crawling.string) # .get_text()와는 다르게 태그 안에 내용이 없으면 None으로 출력됨
print("응답객체 페이지의 태그: ", res.content)