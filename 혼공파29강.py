#for 반복변수 in 리스트:
#  복합구문

a = [1, 2, 3, 4, 5]
for a_1 in a:
  print(a_1)

#총합 sum=0
sum = 0  #덧셈 연산의 항등원 0 10 + ? = 10
for a_i in a:
  sum += a_i
print(sum)
#sum 이라는 변수를 만들고 sum += a_i라고 입력하면 a[0]부터 마지막까지 반복

# 1.a = [1, 2, 3, 4, 5] 라는 리스트가 만들어짐
# 2. sum이라는 변수를 만들고 0이 들어감
# 3. for a_i in a: a에 있는 요소를 하나하나 꺼내서 a_i에 넣어주ㅜㅁ
# 4. 첫번째 a[0]인 1을 꺼냈기에 a_i엔 1이들어갈것이고 sum = sum + a_i로 이동하여 sum=0이므로 0+1이 되어 sum=1이 됨
# 5. 다시 for 반복문으로 이동하고 a_i에는 2가 들어가고 다시 sum에다 넣기때문에 sum =3이 됨 1+2
# 6. a_i =3 sum 3 + a_i 3 = 6
# 7. a_i = 4 sum 6 + a_i 4 = 10
# 8. a_i = 5 sum 10 + a_i 5 = 15 리스트 내부에 모든 요소를 돌았기 때문에 반복문을 벗어남

#총곱 prod=1
prod = 1  #곱셈 연산의 항등원 1 10 * ? = 10
for a_i in a:
  prod *= a_i
print(prod)

#a에 있는 요소를 하나하나 꺼내서 반복변수에 집어넣으므
#a의 요소가 무엇을 나타내는지 쉽게 이해 ㅎ하 수 있는 변수 이름
#for number in numbers for animal in animals
#for 반복변수(단수) in 리스트(복수)
#지을 게 없으면 i j k m n
#반복변수에 a[0]이 들어가고 출력하고 a[1]이 들어가고 출력하고 끝까지 반복

#항등원 임의의 원소에 특정연산을 했을 때 재귀시키는 원소
# A + ? = A
# A * ? = A 할 때 ?가 항등원

#10 + ? = 10 숫자 덧셈 연산의 항등원 0
#10 * ? = 10 숫자 곱셈 연산의 항등원 1

a = (10, 20, 30)
#총합 모든요소 더하기 시그마a
#총곱 모든요소 곱하기 대문자파이a
