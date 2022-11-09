a = "         안녕하세요           "
a.strip()  #비파괴적이라 변함 없음
#a.rstrip() 라이트 오른쪽 공백 제거
#a.lstrip() 레프트 왼쪽 공백 제거
#print(a.strip()) #이 코드만 일시적으로 변화함
#a = a.strip() # a = a.strip 으로 파괴적으로 변화했으므로
#print(a) #영구적으로 a.strip이 적용
#is 함수 a.isalpha a라는 문자열이 알파벳인지 확인하는 함수 true false
a.isalpha()  # 비파괴적이므로 참 거짓 관계없이 그대로 출력
print(a)
print(a.isalpha())  # 일시적 변환
a = a.isalpha()  # a = a.isalpha로 영구적인 변환
print(a)

a = "abcdabcdbcd"

#find함수

print(a.find("b"))  #왼쪽부터 탐색 1번째
print(a.rfind("b"))  #오른쪽부터 탐색 8번째 왼쪽부터 셈
print(a.find("z"))  #a에 없는 걸 찾으면 -1 출력

#in 연산자 문자열 내부에 어떤 문자가 있는지 확인 true false
# 앞에있는 것이 뒤에 있느냐 확인

print("안녕" in "안녕하세요")  #오른쪽에 있는 안녕하세요에 안녕이 있으므로 true
print("bow" in "rainbow")  #true
print("black" in "white")  #false

#split 함수

a = "HeLLo PytHoN"

a.split()  #split은 비파괴적(피연산자를 바꾸지않는)이라 결과는 그대로임
a.format()  # format함수도 비파괴적
#파괴적으로 바꿀려면 a = a.split() 처럼 바꿔야함

#upper lower 함수 비파괴적
a = a.upper()  #대문자 변경
a = a.lower()  #소문자 변경
print(a.upper())  # 대문자로 출력은 하나..
print(a)  # a 값이 변경된 건 아니기 때문에 a 값을 출력한다.

#format() 함수 고급
# 정수를 규격화해서 출력 콜론d :d 쓰고 뒤에 정수를 입력
print("{:d}".format(52))  #그냥 52 출력
# 특정 칸만큼 출력
print("{:5d}".format(52))  #5칸을 잡고 앞에 공백 뒤에 52출력
print("{:10d}".format(52))  #10칸만큼 잡고 앞에 공백 뒤에 52출력
print("{:05d}".format(52))  #5칸을 잡고 앞에 0 뒤에 52
print("{:010d}".format(52))  #10칸을 잡고 앞에 0 뒤에 52
# 부호
print("{:5d}".format(-52))
print("{:=5d}".format(-52))  #부호를 앞쪽으로 밀어서 출력
print("{:=+5d}".format(52))  #+부호를 앞쪽으로 밀어서 출력
print("{:=+05d}".format(52))  #+0052
# 부동소수점
print("{:.1f}".format(
  52.273))  #.1f은 소수점 1번째 자리까지 출력 자동으로 반올림 해서 52.273 -> 52.3이 된다.
print("{:.2f}".format(
  52.273))  #.5f은 소수점 5번째 자리까지 출력 자동으로 반올림 해서 52.273 -> 52.27이 된다.

b = 10
print(b + 10)  # 10 + 10 = 20
print(b)  # b = 10이므로 10

# + - % * / // ** 연산자 피연산자를 바꾸지 않음
#비파괴적

# = 연산자 피연산자를 바꿈
#파괴적
#a = 10
#a = a + 10
#a = 20
#a = 30
