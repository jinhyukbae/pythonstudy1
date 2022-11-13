# 홀수 짝수 구분
number = int(input("정수 입력 : "))

if number % 2 == 0: #2를 나눈 나머지가 0이 되면
  print("짝수")
else: #2를 나눈 나머지가 0이 안되면
  print("홀수")

# 양수 음수 0

# a가 0보다 크지 않으면서 elif a<0 조건에 해당한다면 음수 출력
# a가 0보다 크지 않으면서 elif a<0 도 아니면서 a == 0에 해당한다면 0출력   

a = int(input())
if a > 0: 
  print("양수")
elif a < 0:# a가 0보다 크지 않으면서 elif a<0 조건에 해당한다면 음수 출력
  print("음수")
#elif a == 0:
else:   #a가 0보다 크거나 작지 않으면 0 밖에 없으므로 else가 더 효율적 
  print("0")

# 봄 여름 가을 겨울

b = int(input())
if 3 <= b <= 5:
  print("봄")
elif 6 <= b <= 8:
  print("여름")
elif 9 <= b <= 11:
  print("가을")
#elif 1 <= b <= 2 or b == 12:
  #print("겨울")
# 3 <= b <= 5도 아니고 6 <= b <= 8도 아니고 9 <= b <= 11 아니면
# 1 <= b <= 2 or b == 12 밖에 없으므로 else로 하는 게 효율적
else:
  print("겨울")
  

# 오전 오후 구분
from pytz import timezone
from datetime import datetime
today = datetime.now(timezone('Asia/Seoul'))
print(today)

if today.hour < 12:
  print("오전")
else:
  print("오후")