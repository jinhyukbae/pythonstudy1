#입력한 숫자의 짝수 홀수를 구하는 법 
# 입력
raw = input("정수를 입력해주세요:")
#l = raw[-1] # 입력한 숫자의 맨끝자리를 구함 -1
raw = int(raw)

# 짝수 or 홀수
## 짝수 : 02468
#if l == "0" or l == "2" or l == "4" or l == "6" or l == "8":
  #print("짝수입니다")

if raw % 2 == 0: 
  print("짝수입니다")
  
#if l == "1" or l == "3" or l == "5" or l == "7" or l == "9":
  #print("홀수입니다")

if raw % 2 != 0:
  print("홀수입니다")


#if l in "02468":
  #print("짝수입니다")
#if l in "13579":
  #print("홀수입니다")


#자주하는 실수
#if l == "0" or "2" or "4" or "6" or "8": 
# or은 둘중 하나가 true면 전체를 true로 하기 때문에 틀림 사용할수없다 


