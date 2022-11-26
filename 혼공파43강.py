# 리스트 내포 comprehension 컴프레헨션
# 반복가능한 것을 기반으로 새로운 리스트를 만들어내는 문법
#An = 2n + 1 (0 <= n < 10)
#A = {1,3,5,7,9 ,,,,, 19}

A = []
for i in range(10):
  A.append(2 * i + 1)
print(A)

A = [2 * i + 1 for i in range(10) if i % 2 == 0]
print(A)

#달러를 원화로 환율 계산
달러 = [155.43, 302.71, 77.46, 131.28]
원화 = []

for dollar in 달러:
  원화.append(dollar * 1400)
print(원화)

원화 = [dollar * 1400 for dollar in 달러]
print(원화)