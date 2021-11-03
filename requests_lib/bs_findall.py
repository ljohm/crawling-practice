import requests
from bs4 import BeautifulSoup

# 메서드를 사용한 웹페이지 파싱 세번째
# bs.find_all(태그명, 속성 정보)
# -> 주어진 기준에 맞는 태그들을 모두 찾아옴


url="http://www.weather.go.kr/weather/forecast/mid-term-rss3.jsp"
res = requests.get(url)
res.raise_for_status()

soup = BeautifulSoup(res.text, "html.parser")
locations = soup.find_all('location') # location 태그를 전부 찾아서
for location in locations: # 각 location 태그를 돌며
    city = location.find('city') # city 태그를 찾아서 
    print(city.string) # 태그 제거한 문자열만 출력
    datas = location.find_all('data') # 해당 location의 data 태그를 전부 찾아
    for data in datas: # 각 data태그를 한개씩 돌며
        print(data.text) # 태그 제거한 문자열만 출력