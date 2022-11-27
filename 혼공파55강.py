a = 10
b = [1, 2, 3, 4]


#위에거 출력후 값을 바꿔 출력하고 싶을 때
def function():
  global a, b  #전역변수 위에 걸 먼저 출력
  print(a)
  print(b)
  a = 20  #a= 20
  b = [5, 6, 7, 8]  #b= [5,6,7,8] 지정


function()

print(a)
print(b)


def function():
  a = 20  #a= 20
  #b = [5,6,7,8] #함수스택에 새로운 변수를 만들어 외부랑 완전히 분리
  b.extend = [5, 6, 7, 8]  #b = [1,2,3,4,5,6,7,8]
  # 함수 스택에 새로운 변수를 만드는 것이 아님 외부에 영향을 줌
  print(a)
  print(b)  #출력


function()  #함수 스택 날아감

print(a)  #10
print(b)  #1,2,3,4,5,6,7,8 expend는 함수 스택에 영향을 주는 함수가 아니므로

#함수는 호출할 때 마다 스택이 새로 만들어 진다
# def function():
#   a = 20
#   b = [5,6,7,8]
#   funciton()
# function()
#무한반복
