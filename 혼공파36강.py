#a = [1,3,5,7,9]

##일반항
#a2-a1=2
#a3-a2=2
#an=2n-1
#a1 = 2 * 1 -1 = 1
#a2 = 2 * 2 -1 = 3
#a100 = 2 * 100 -1 = 99

#100번째 항을 구하고 싶다면
n = 100
a_n = 2 * n - 1

print(a_n)


#1번째 항부터 100번째 항까지 쭉 나열해서 출력하고 싶다면 
for n in range(1, 100+1):
  a_n = 2 * n - 1
  print(a_n)


#1번째 항부터 10번째 항까지 들어있는 리스트 
a = []
for n in range(1, 10+1):
  a_n = 2 * n - 1
  a.append(a_n)
print(a)

#
a = [None] #a에 None을 넣으면 a[0]이 None이라 뜨면서 수학에서 사용하는 인덱스처럼 사용 가능 
for n in range(1, 10+1):
  a_n = 2 * n - 1
  a.append(a_n)
print(a)
# a_1 = 1
# a_2 = 2
# a[0] = 1
# a[1] = 3

##점화식 이전항의 값을 기반으로 다음항의 값을 구함 
#an=a(n-1)+2

a = [None] #a에 None을 넣으면 a[0]이 None이라 뜨면서 수학에서 사용하는 인덱스처럼 사용 가능 
for n in range(1, 10+1):
 if n == 1:
   a_n = 1
 else:  
   a_n = a[n-1] + 2
 a.append(a_n)
print(a)

#1번째 항부터 100번째 항까지 들어있는 리스트 

N = 100
a = [None] * (N + 1) #101개의 항을 미리 만듬 아래에서 만들면 파이썬 특성상 느림
#N + 1을 하는 이유는 None이라는 요소를 쓰기위해 첫번째 항이 none이기때문에 요소 개수는 101개가 되므로 N + 1을 한 것 
for n in range(1, N + 1):
 if n == 1:
   a[1] = 1
 else:  
   a[n] = a[n-1] + 2
print(a)

#반복문으로 이전 항의 것을 기반으로 다음항의 값을 구해내는 방법 동적 계획법


#피보나치 

N = 100
a = [None] * (N + 1) 
for n in range(1, N + 1):
 if n == 1 or n == 2:
   a[n] = 1
 else:  
   a[n] = a[n-1] + a[n-2]
print(a)