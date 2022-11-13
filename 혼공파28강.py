#요소 추가: append(), insert(), extend()
a = [1,2,3,4]
a.append(10)#마지막 위치에 요소 하나 추가
#4 뒤에 10 추가
print(a)
a.insert(0,20) # 원하는 위치에 요소 하나 추가
#0번째인 1 앞에 20 추가
print(a)
a.extend([5,6,7,8]) # 마지막에 요소 여러개 추가
#10 뒤에 5 6 7 8 추가
print(a)
#비파괴적연산자인 +를 extend처럼 사용하려면 
#a = a + [5,6,7,8]

#요소 제거: del, pop(), remove(), clear()
a = [1,2,3]
del a[0] #제거하고 싶은 인덱스 입력 [2,3]
print(a) #[2,3]
a.pop(0)#제거하고 싶은 인덱스 입력 입력하지 않으면 기본값-1 
print(a) # [3]
a.remove(3) # 제거하고 싶은 요소 입력 1 2 3 이 있으면 1 2 3을 입력
print(a) # 3이라는 요소를 제거했기 때문에 빈 리스트 []
a.clear()# 아무 것도 입력하지 않고 사용 모든 요소를 제거
print(a) # 클리어를 하면 어차피 빈 리스트 []

#요소 정렬 sort()
a = [52, 273, 1, 7, 9, 103, 58, 201]
a.sort() #오름차순
print(a)
a.sort(reverse=True) #괄호 안을 매개변수 라 함 내림차순
print(a)
#요소 존재 확인 : in, not in
print(52 in a) #true
print(0 in a) # false
print(52 not in a) #false
print(0 not in a) # true


#리스트 함수는 파괴적이라 = 안써도 됨 


#요소 정렬 sort()
#요소 존재 확인 : in, not in


#파괴 연산 후에 피연산자가 변형
#a = 10
# = 할당연산자
#print(a) # a=10
#a = 20
#print(a) # a= 20 a의 값이 파괴 됨 
#비파괴 연산 후에 피연산자가 변형되지 않음
# + - * / 연산자

#a = 10
#print(a) # a = 10
#a + 20 # a의 값을 파괴하지 못함 파괴적인 결과를 만들고 싶으면 = 연산자를 써야함 a = a+20 같은 
#print(a) # a = 10