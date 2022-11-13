# 조건문

if 조건: 복합 문장

#복합 문장: 문장을 묶어 놓은 것 

#오전 오후 구분 프로그램
from pytz import timezone
from datetime import datetime

today = datetime.now(timezone('Asia/Seoul'))

print(f"{today.hour}시{today.minute}분{today.second}초 입니다!")
if today.hour < 12:
  print("오전입니다!")
if today.hour >= 12:
  print("오후입니다!")

# 계절 구분 프로그램

m = today.month

if 3 <= m <= 5:
  print("봄입니다!")

if 6 <= m <= 8:
  print("여름입니다!")

if 9 <= m <= 10:
  print("가을입니다!")

if (11 <= m <= 12) or (m == 1):
  print("겨울입니다!")

# if 조건문
#3 조건이 ture 일때만 들여스기 안쪽의 문장을 실행
#사용자가 입력한 숫자가
#양수 음스 0인지 판별하는 프로그램

a = input("정수를 입력해주세요: ")
a = int(a)

if a > 0:
  print("양수입니다!")
if a < 0:
  print("음수입니다!")
if a == 0:
  print("0입니다!")

  #탭으로 뒤로 밀거나 쉬프트 탭으로 앞으로 밀거나