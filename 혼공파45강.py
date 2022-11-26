f"{10:b}" # 2진수 1010
f"{10:o}" # 8진수 8
f"{10:x}" # 16진수 a


#10진수로 변환
int("1010", 2) 
int("12", 8)
int("a", 16)


a = []
for i in range(1, 100+1):
  변환 = f"{i:b}"
  if 변환.count("0") == 1: #변환에 0이 들어가 있으면 1(true)이므로 아래로
    print(변환) #위를 만족하면 출력
    a.append(i) #위를 만족하는 숫자를 10진수인 형태로 a 리스트에 저장 
print("합계:",sum(a))  




#위를 리스트 내포 

a = [i for i in range(1,100+1) if f"{i:b}".count("0") == 1 ]

for i in a:
  print(i, ":" f"{i:b}") #왼쪽은 10진법 i 오른쪽은 10진법 i를 2진법 변환
print("합계:", sum(a))