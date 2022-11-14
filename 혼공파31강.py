# 100이상인 수만 출력 

numbers = [273,103,5,32,65,9,72,800,99]

#100이상의수
for number in numbers:
  if number >= 100:
    print("- 100 이상의 수:",number)

#홀 짝
for number in numbers:
  if number % 2 == 0:
    print(f"{number}는 짝수 입니다.")
  else:
    print(f"{number}는 홀수 입니다.")

#자리수 출력
for number in numbers:
  print(f"{number}는 {len(str(number))}자리 입니다") 
print()
# 273 ->str "273" -> len 3

#결과 [[1,4,7],[2,5,8],[3,6,9]]
   

# output[0]  = [1,4,7]
# output[1]  = [2,5,8]
# output[2]  = [3,6,9]
# 정수 주기 반복: 나머지 연산자 %
#      1 2 3 4 5 6 7 8 9 
#a_n = 0,1,2,0,1,2,0,1,2

numbers = [1,2,3,4,5,6,7,8,9]
output = [[], [], []]
for number in numbers:
  output[(number - 1) % 3].append(number)

  # number = 1이 들어가면 1 % 3 = 1, 원하는 값은 0
  # number = 2이 들어가면 2 % 3 = 2, 원하는 값은 1
  # number = 3이 들어가면 3 % 3 = 0, 원하는 값은 2
  
  #output[number % 3].append(number) #[[3,6,9],[1,4,7],[2,5,8]]
  
  # number % 1 하면 [[1,2,3,4,5,6,7,8,9],[],[]]이 됨 한 쪽에 쏠림
  # number % 2 하면 2등분 됨 [[2,4,6,8],[1,3,5,7,9],[]]
  # number % 3 해야 [[3,6,9],[1,4,7],[2,5,8]]같이 세등분 됨
  
  #output[(number - 1) % 3].append(number)

  # number = 1이 들어가면 1-1=0 % 3 = 0, 원하는 값은 0
  # number = 2이 들어가면 2-1=1 % 3 = 1, 원하는 값은 1
  # number = 3이 들어가면 3-1=2 % 3 = 2, 원하는 값은 2 0,1,2

  #output[(number % 3) - 1].append(number)
  
  # number = 1이 들어가면 1 % 3 = 1-1, 0 원하는 값은 0
  # number = 2이 들어가면 2 % 3 = 2-1, 1 원하는 값은 1
  # number = 3이 들어가면 3 % 3 = 0-1, -1 -1은 순서 거꾸로이므로 2랑 같음

print(output)