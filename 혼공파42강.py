a = [52, 273, 32, 103, 57]

print(max(a))  #리스트 a에 있는 최대값을 구해줌
print(min(a))  #리스트 a에 있는 최소값을 구해줌

print(max(52, 273, 32, 103, 57))
print(max(*a))  #리스트 앞에다 별을 붙여주면 리스트를 전개해서 넣어줌
print(min(52, 273, 32, 103, 57))
print(min(*a))

print(sum(a))  #리스트 값을 다 더해줌

#reversed 결과를 한번만 사용 가능 두번 째 부턴 무시하고 출력됨

#for i in reversed(a): 같은 형태로 그냥 통째로 외우기

a = reversed(range(0, 10))

for i in a:
  print(i)

for i in a:
  print(i)

#enumerate 함수

fruits = ["바나나", "사과", "포도"]

i = 0

for fruit in fruits:
  print(f"{i}:{fruit}")
  i = i + 1

fruits = ["바나나", "사과", "포도"]
a = enumerate(fruits)
print(list(a))

#결과가 [(0, '바나나')] 같이 리스트안에 튜플로 감싸짐

# reversed와 마찬가지로
for fruit in enumerate(fruits):
  print(fruit[0], fruit[1])

  #fruit[0]은 print(f"{i}:{fruit}") 중에 {i}를 출력
  #fruit[1]은 {fruit}를 출력

for [i, fruit] in enumerate(fruits):
  print(i, fruit)

for i, fruit in enumerate(fruits):
  print(i, fruit)

# items()함수 딕셔너리 실전압축

a = {"이것": "바나나", "가격": 1500, "원산지": "말레이"}

for key in a:
  print(a[key])
  #프린트 a하면 전체 key하면 이것 가격 원산지 같은 키 값만 출력
  #a[key]를 하면 밸류값을 출력

print(a.items())

for i in a.items():
  print(i)

for i in a.items():
  print(i[0], i[1])

for 키, 값 in a.items():
  print(키, 값)
"""
함수형 프로그래밍 이념
reversed(a)
객체지향 프로그래밍 이념 
a.items()
"""
