# None, 숫자 0, 빈 컨테이너 False

# 사용자로부터 입력
a = input("> 입력해주세요: ").strip() #strip 양쪽의 공백을 제거하는 함수

#최신
if a == "":
  print("프로그램을 다시 실행해주세요")
  exit() # 빈문자를 쳤으면 위가 실행되고 아니면 아래가 실행 됨 
print("입력한 내용:", a , "입니다.") 

#구식
if not(a == ""):
#if a != "":
  #프로그램의 주요 기능
  print("입력한 내용:", a , "입니다.")
else:
  #프로그램의 보완적 기능
  print("프로그램을 다시 실행해주세요")


if a: # 빈 문자열이 아닐 때 
  pass
  #raise NotImplementedError 구현 안 해논 거
  
  #if :다음엔 반드시 suite(복합구문)이 와야함
  #이렇게 아무것도 입력할 것 없을 땐 pass를 넣으면 됨
  # 나중에 입력하려고 임시로 만들었을 땐 raise NotImplementedError
  # raise는 강제로 오류를 발생시키는 코드 아직 구현이 되지 않았따
  print("입력한 내용:",a,"입니다.")
else: # 빈 문자열 일 때
  print("프로그램을 다시 실행해주세요")
    
# 입력을 그대로 출력
# 아무것도 입력하지 않았다면 프로그램을 다시 실행해주세요

# 입력에 hi나 hello가 들어가면 안녕하세요 출력 입력에 time이 들어가면 지금은 몇 시 입니다 출력 빈 문자열은 입력한 그대로 출력 하게하는 프로그램 

a = input("입력: ")

if ("hi" in a) or ("hello" in a):
  print("안녕하세요")
elif "time" in a:
  from pytz import timezone
  from datetime import datetime
  today = datetime.now(timezone('Asia/Seoul'))
  print(f"지금은 {today.hour}시 입니다.")
else:  
  print(a)


# 나누어 떨어지는 숫자 확인 프로그램

b = int(input("숫자를 입력하세요"))

if b % 2 == 0:
  print("2로 나누어 떨어지는 숫자")
else:
  print("2로 나누어 떨어지는 숫자가 아닙니다")
if b % 3 == 0:
  print("3로 나누어 떨어지는 숫자")
else:
  print("3로 나누어 떨어지는 숫자가 아닙니다")  
if b % 4 == 0:
  print("4로 나누어 떨어지는 숫자")
else:
  print("4로 나누어 떨어지는 숫자가 아닙니다")  
if b % 5 == 0:
  print("5로 나누어 떨어지는 숫자")
else:
  print("5로 나누어 떨어지는 숫자가 아닙니다")  
  
  