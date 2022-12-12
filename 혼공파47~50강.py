#점근표기법 빅오 표기법 란다우 표기법
#복잡도 앞에있는 거 빼고 다 없앤다음에 앞에 알파벳 o를 쓰고 괄호로 감쌈
#n! + n^2 nlogn + 1 = 0(n!)

#데이터 수가 적으면 n^2
#데이터 수가 많으면 n log n 정도가 현실적인 수

#n(n+1)/2

#함수 프로시저 + 리턴 값

output = 0


def f(x):
  return x**2 + 2 * x + 1


print(f(20))


def print_3_times(문자열, 횟수):
  if type(문자열) != str:
    print("첫번째 매개변수는 문자열을 입력해야 합니다.")
  if type(횟수) != int:
    print("두번째 매개변수는 정수를 입력해야 합니다")
  for i in range(횟수):
    print(문자열)


print_3_times("gㅎㅇ", "10")



  

def print_n_times(num, list):
  for i in range(num):
    for par in list:
      print(par)

print_n_times(3,["안녕"],["하세요"])
