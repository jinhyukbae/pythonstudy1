#while 반복문 > for 반복문
#for반복문으로 할수 있는 건 while 반복문으로도 구현 가능 반대는 불가

#while True:
#복합구문
#조건이 참이면 무한반복

i = 0
while i < 10:
  i = i + 1
  print(f"{i}번째 반복")

# 빵 10개를 먹어라 for 특정회수만큼 반복
# 바게트빵만 다먹어라, 내일아침까지 계속 먹어라 while 조건으로 반복

a = [1, 2, 1, 2]
value = 2

while value in a:  #밸류가 a에 있는 동안만 반복
  # a에 2가 있기 때문에 무한으로 돌아감
  a.remove(value)  #가장 처음발견한 value=2를 삭제
# a = [1,,1,2] 인상태로 2가 다시 있으므로  다시 반복

print(a)  #[1,1]

import time

시작시간 = time.time()
현재시간 = time.time()

while 현재시간 < 시작시간 + 5:  #현재시간이 시작시간 +5보다 작은동안 반복
  print(현재시간, 시작시간 + 5)
  현재시간 = time.time()
