#break 반복문 전체 벗어날 때
#continue 현재 반복만 넘어감 


"""i = 0

while 1:
  print(f"{i}번 째 반복입니다.")
  i += 1

  a = input("종료하시겠습니까 (y/n)")
  if a in("y","Y"):
    print("반복문을 종료")
    break
"""


numbers = [5,15,6,20,7,25]

for i in numbers:
  if i >= 10:
    print(i)



for i in numbers:
  if i < 10:
    continue
  print(i)  


key_list = ["name", "hp", "mp", "level"]
value_list = ["기사", 200, 50, 10]
c = {}

for i in range(4):
  c[key_list[i]] = value_list[i]

print(c)  


limit = 10000

i = 1
sum_value = 0


while sum_value < limit:
  sum_value = sum_value + i
  i = i + 1




print(f"{i-1}을 더할 때 {limit}을 넘으며 그때의 값은 {sum_value}입니다.")



#최대값 구하기 

a = [27, 53, 103 ,273, 32]

현재최대값 = a[0]

for i in a:
  if i > 현재최대값:
    현재최대값 = i

print(현재최대값)   


#최소값 구하기 

a = [27, 53, 103 ,273, 32]

현재최소값 = a[0]

for i in a:
  if i < 현재최소값:
    현재최소값 = i

print(현재최소값) 
    


#최대값 구하기 
a =[]
for i in range(1,100):
  j = 100 - i
  a.append(i*j)
  현재최대값 = a[0]
  if a > 현재최대값:
    현재최대값 = a
  print(현재최대값)  



a = [27, 53, 103 ,273, 32]

현재최대값 = a[0]

for i in a:
  if i > 현재최대값:
    현재최대값 = i

print(현재최대값)



max_value = 0

a = 0
b = 0



a = []
for i in range(1, 100):
  j = 100 - i
  a.append([i*j])


현재최대값 = a[0]
for i in a:
  if 현재최대값 < i:
    현재최대값 = i
print(현재최대값)  



a = []
for i in range(1, 100):
  j = 100 - i
  a.append([i,j, i*j])

최대리스트 = a[0]
현재최대값 = 최대리스트[2]
for i in a:
  if 현재최대값 < i[2]:
    최대리스트 = i
    현재최대값 = 최대리스트[2]
print(최대리스트)



현재최대값 = 0
a = 0
b = 0

for i in range(1, 99 + 1):
  j = 100 - i
  if 현재최대값 < i * j: #현재최대값이 i*j보다 작냐 작으면
    a = i
    b = j
    현재최대값 = i * j
print(f"최대가 되는 경우: {a} * {b} = {현재최대값}")
print(a)
print(b)
print(현재최대값)