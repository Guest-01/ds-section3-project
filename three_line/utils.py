import os

import requests
from dotenv import load_dotenv

load_dotenv(verbose=True)

session = requests.Session()

CLIENT_ID = os.getenv("NAVER_CLIENT_ID")
CLIENT_SECRET = os.getenv("NAVER_CLIENT_SECRET")

URL = "https://naveropenapi.apigw.ntruss.com/text-summary/v1/summarize"


def api_call(text, title="null", model="general"):
    headers = {
        "X-NCP-APIGW-API-KEY-ID": CLIENT_ID,
        "X-NCP-APIGW-API-KEY": CLIENT_SECRET,
        "Content-Type": "application/json",
    }
    body = {
        "document": {"content": text, "title": title},
        "option": {"language": "ko", "model": model},
    }

    res = session.post(URL, headers=headers, json=body)
    return res.json()


if __name__ == "__main__":
    text = "이것은 글 요약을 얼마나 잘하는가에 대한 글이다. 내가 얼마나 길게 쓸지는 모르겠지만, 이 API를 이용하면 글을 세 문장으로 줄여준다고 한다. 검수를 거치지 않고 쓴 이 글도 적절하게 잘 요약이 될까? 맞춤법이나 띄어쓰기가 완벽하지 않더라도 잘 요약해주는지 궁금하다. API의 출처는 네이버 클라우드 플랫폼이라서 기대가 된다. 중간에 전혀 상관없는 문장도 한번 넣어보겠다. 오늘 날씨가 참 맑다. 요약하기란 사람만이 할 수 있는 일이었는데 컴퓨터로 할 수 있게된다면 참 편리할 것 같다. 이런 서비스를 제공해준 네이버에게 감사하다."
    print(api_call(text))
