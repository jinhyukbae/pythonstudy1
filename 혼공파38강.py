# reversed()

print(list(reversed([1, 2, 3, 4, 5])))
#[5,4,3,2,1]

print(list(reversed(range(0, 10))))
#[9,8,7,6,5,4,3,2,1,0]

for i in reversed(range(0, 10)):
  print(i)
# 9876543210

#for i in range(1,10):
#print("*" * i)

N = 10
for i in range(1, N + 1):
  print(" " * (N - i) + "*" * i)

#크리스마스 트리
height = 10
for i in range(1, height + 1):
  result = ""
  for j in range(height - i):
    result = result + " "
  for j in range(2 * i - 1):
    result = result + "*"
  print(result)
