#1RM 계산

#입력
a = input("5~8회 반복가능 무게를 입력해주세요: ")
b = input("반복 횟수를 입력해주세요: ")
a = float(a)
b = float(b)
#처리
c = a +(a*0.025*b)

#출력
print(f"당신의 1RM은 {c}입니다.")