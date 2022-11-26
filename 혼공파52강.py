# def test(a=10):
#   print(a)  #10


# test(20)  #20
# test(a=30)  # 30

def 함수(*가변, **딕셔너리):
  print(가변, 딕셔너리)

함수("안","녕","하", a=10, b=20, c=30)


def print_n_times(n, *values):
  for i in range(n):
    for value in values:
      print(value)
    print()

print_n_times(2, "ㅎㅇ", "ㅎ")


def print_n_times(*values,n):
  for i in range(n):
    for value in values:
      print(value)
    print()

print_n_times("ㅎㅇ", "ㅎ",n=2)