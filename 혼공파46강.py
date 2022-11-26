A = [1,2,3,4,1,2,3,1,4,2,3,1,2,4]

count = {}

for i in A:
  if i not in count:
    count[i] = 0
  count[i] += 1

print(count)
print(f"사용된 숫자의 종류는 {len(count)}개 입니다.")


A = "abcdabcdabdcbacbadcbadcbadbcbadcbcadc"

count = {}


for i in range(0,len(A),3):
  print(i, i+3, A[i:i+3])




for i in range(0,len(A),3):
  a = A[i:i+3]
  if len(a) != 3:
    continue
if a not in count:
  count[a] = 0
count[a] += 1

print(count)
