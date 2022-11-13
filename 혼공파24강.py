학점 = float(input(">학점을 입력하세요: "))


#elif 구문에 도착했다는 건 이미 그 위에 있던 조건이 거짓이라는 뜻
#따라서 또 쓸 필요가 없다
if 학점 == 4.5:
  print("신")
elif 4.2 <= 학점: #학점 == 4.5가 아니라 아래로 내려왔으므로 <4.5를 쓸 필요 없다
  print("교수님의 사랑")
elif 3.5 <= 학점:
  print("현체제의수호자")
elif 2.8 <= 학점:
  print("일반인")
elif 2.3 <= 학점:
  print("일탈을 꿈꾸는 소시민")
elif 1.75 <= 학점:
  print("오락문화의 선구자")
elif 1.0 <= 학점:
  print("불가촉천민")
elif 0.5 <= 학점:
  print("자벌레")
elif 0.0 < 학점:
  print("플랑크톤")
else:
  print("시대를 앞서가는 혁명의 씨앗")

x = 10
y = 2
if x > 4:
  if y > 2: #같은 줄에 있는 한 쌍의 if else만 적용 얘는 아래에 쌍이 없으므로 else로 안 넘어가고 값을 미출력함 
    print(x * y)
else:
  print(x + y)

if x > 10 and x < 20:
  print("조건에 맞습니다")


a = int(input("태어난 해를 입력해주세요"))

print("원숭이,닭,개,돼지,쥐,소,범,토끼,용,뱀,말,양".split(",")[a % 12], "띠입니다.") #문자열을 split 한 다음 입력값 a 를 12로 나눴을 때 결과값에 따라 띠가 출력된다.

if a % 12 == 0: #ex 2004년은 12로 나눴을 때 나머지가 0이므로 원숭이 띠 이다.
  print("원숭이 띠")
elif a % 12 == 1:
  print("닭 띠")
elif a % 12 == 2:
  print("개 띠")
elif a % 12 == 3:
  print("돼지 띠")
elif a % 12 == 4:
  print("쥐 띠")
elif a % 12 == 5:
  print("소 띠")
elif a % 12 == 6:
  print("범 띠")
elif a % 12 == 7:
  print("토끼 띠")
elif a % 12 == 8: 
  print("용 띠")
elif a % 12 == 9:
  print("뱀 띠")
elif a % 12 == 10:
  print("말 띠")
elif a % 12 == 11:
  print("양 띠")


 




#if 학점 == 4.5:
  #print("신")
#if 4.2 <= 학점 < 4.5:
  #print("교수님의 사랑")
#if 3.5 <= 학점 < 4.2:
#  print("현체제의수호자")
#if 2.8 <= 학점 < 3.5:
#  print("일반인")
#if 2.3 <= 학점 < 2.8:
#  print("일탈을 꿈꾸는 소시민")
#if 1.75 <= 학점 < 2.3:
#  print("오락문화의 선구자")
#if 1.0 <= 학점 < 1.75:
#  print("불가촉천민")
#if 0.5 <= 학점 < 1.0:
#  print("자벌레")
#if 0.0 < 학점 < 0.5:
#  print("플랑크톤")
#if 학점 == 0.0:
#  print("시대를 앞서가는 혁명의 씨앗")