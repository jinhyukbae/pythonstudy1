def hi_3_times(num, str1, str2):
  for i in range(num):
    print(str1, str2)


hi_3_times(2, "안녕", "하세요")


def print_n_times(num, list):
  for i in range(num):
    for par in list:
      print(par)


print_n_times(3, ["안녕", "하세요"])

#가변매개변수 앞에 *이 붙으면 자동으로 리스트로 변환해서 받게 됨


def print_n_times(num, *list):
  for i in range(num):
    for par in list:
      print(par)


print_n_times(3, "안녕", "하세요")


def print_n_times(num, *list):
  for i in range(num):
    for par in list:
      print(par)


문자열목록 = ["안녕", "하세요"]
#앞에 #을 붙이면 문자열목록[0],문자열목록[1] 할필요 없이 자동으로 전개 된다.
print_n_times(3, *문자열목록)

print_n_times(3, "안녕", "하세요")


def print_n_times(*list, num):
  for i in range(num):
    for par in list:
      print(par)


print_n_times("안녕", "하세요", num=2)
