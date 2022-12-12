# 입력 : inch 단위를 입력 입력함수 input
a = input("inch 단위를 입력해주세요: ")

# 처리 inch -> cm 변환하는 처리 inch는 cm 곱하기 2.54
#input은 무조건 문자열 이므로 int나 float로 숫자형으로 변환해줄 것 
a = float(a) * 2.54

# 출력 : cm 단위를 출력
print("cm 단위로는", a, "입니다")
