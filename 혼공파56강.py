a = 10
b = [1, 2, 3, 4]
print(a, b)


def function_a(c, d):
  c = 20
  d = [5, 6, 7, 8]


function_a(a, b)  #함수의 실행이 끝나면 c=20 d =[5,6,7,8] 같은 메모리의 내용이 모두 날라감
print(a, b)


def function_b(c, d):
  c = 30
  d.extend([9, 10])


function_b(
  a, b)  #위와 마찬가지로 c = 30 메모리 초기화 extend는 전역변수에 직접 영향을 끼치므로 메모리 초기화의 영향 없음
print(a, b)
