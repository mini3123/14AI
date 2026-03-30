import requests
from bs4 import BeautifulSoup

def get_news_titles(keyword):
    # 1. URL 설정
    url = f"https://search.naver.com/search.naver?where=news&query={keyword}"
    
    # 2. 헤더 설정 (신분증 최신화)
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36"
    }
    
    try:
        response = requests.get(url, headers=headers)
        # 접속 성공 여부 확인 (200이면 성공)
        if response.status_code != 200:
            print(f"사이트 접속 실패! 에러코드: {response.status_code}")
            return

        soup = BeautifulSoup(response.text, "html.parser")
        
        # 3. 뉴스 제목 찾기 (클래스명이 바뀌었을 수 있으니 여러 시도)
        # 네이버 뉴스의 경우 보통 a 태그이면서 news_tit 클래스를 가집니다.
        titles = soup.select("a.news_tit")
        
        if not titles:
            print("데이터를 찾지 못했습니다. 네이버의 HTML 구조가 바뀌었을 수 있어요!")
            # 팁: 이럴 때 soup.text를 출력해보면 어떤 데이터가 왔는지 알 수 있습니다.
            return

        print(f"\n--- '{keyword}' 관련 최신 뉴스 제목 ---")
        for i, title in enumerate(titles, 1):
            print(f"{i}. {title.get_text()}")
            
    except Exception as e:
        print(f"오류 발생: {e}")

# 실행
search_word = input("검색어를 입력하세요: ")
get_news_titles(search_word)