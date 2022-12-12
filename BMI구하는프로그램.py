# bmi 구하는 프로그램

#입력
a = input("키를 입력해주세요 : ")
b = input("몸무게를 입력해주세요: ")
a = float(a)
b = float(b)
#처리 
#bmi 공식 자신의 몸무게를 키의 제곱으로 나눔
c = b / (a ** 2)

#출력

print(f"BMI는 {c} 입니다.")