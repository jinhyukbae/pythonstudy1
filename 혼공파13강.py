#input() 함수 소문자 스네이크케이스 괄호 O 함수
#1.프롬프트(입력을 요청하는 문자열)를 출력
#2. 사용자로부터 입력을 받을 수 있게 일시정지
#3.입력을 받으면 계속진행

#print(input("입력해주세요: ")) #hello를 입력하면 곧바로 hello를 출력하고
##함수의 결과 = 함수의 리턴값 
#a = input(">>> ") #world를 입력하면 world를 변수에 저장하고 곧바로 출력 
#print(a)
#print(type(a)) #input함수는 무조건 문자열 숫자 10을 써도 str

a = input("숫자1: ")
b = input("숫자2: ")

print(a+b) #a에 10을 입력 b에 20을 입력하면 결과는 1020이 나온다 

a = input("숫자1: ")
b = input("숫자2: ")

a = int(a)
b = float(b)
c = str(a)

print(a+b) #str를 int로 바꿨으므로 a 10 b 20 입력하면 30이 나온다 
print(c, type(c)) #첫번째 입력 값 a를 문자열로 치환하고 그것을 c라고 했으므로
# a값은 str으로 나오게 된다. 

#문자->숫자
#int("52") #정수
#float("52.273") # 부동소수점

#숫자->문자

#c = str(a) # 첫번째 입력하는 a를 str로 바꿈 

#print(a+b)
#print(c, type(c))