a = float(input("> 1번째 숫자:"))
b = float(input("> 2번째 숫자:"))
print()


if a>b:
  print("처음입력 했던 {}이 {}보다 큽니다".format(a,b))
if a<b:
  print("두번째로 입력했던 {}이 {}보다 큽니다".format(b,a))  














a = int(input("첫번째 숫자"))
b = int(input("두번째 숫자"))

if a > b:
  print("처음 입력한{}이 두번째로 입력한{}보다 큽니다".format(a,b))
if a < b:
  print("두번째로 입력한{}이 처음입력한 {}보다 큽니다".format(b,a))