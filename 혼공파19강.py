#날짜/시간 구하는 방법
import datetime
import pytz
seoul = pytz.timezone("Asia/Seoul")
now = datetime.datetime.now(seoul)

print("{}년 {}월 {}일 {}시 {}분 {}초".format(
  now.year,
  now.month,
  now.day,
  now.hour,
  now.minute,
  now.second,
))





# 비교 연산자
# = 하나는 할당연산자 
# == 두개는 비교연산자 
#10 == 20 두 대상이 같은 가 
#10 != 20 두 대상이 다른 가
#10 < 20 왼쪽이 더 작다
#10 <= 20 왼쪽것이 작거나 같다
#10 > 20 왼쪽이 더 크다
#10 >= 20 왼쪽이  크거나 같다 
# x = 20
# 10<x<30 은 true

#논리연산자

#단항 not
#not True # False
#not False # True
#"1020".isalnum() = true
#not"1020.isalnum() false

#이항 and
# 둘다 true 여야 true 하나라도 false면 false
#True and True #true
#True and False #False
#False and True #False
#False and False #False

#이항 or
# 하나라도 true 면 true
#True or True #True
#True or False #True
#False or True #True
#False or False #False

#예1
#어린이날에 호텔에서
#"호텔멤버쉽 회원"이면서
#"12세 이하의 어린이 동반"
#선물 
##is멤버쉽() and is어린이동반()

#예2
#배달 음식 앱에서
#"주문한 음식 가격 2만원 이상"이면서
#"거리 500m 이하의 경우"
#무료
##(가격 >= 20000) and (거리 <= 500)

#예3
#"우리카드"와 "신한카드"
#무이자 6개월
##is우리카드() or is신한카드()

#예4

#주차장에서
#"전기자동차" 와 "하이브리드자동차"
#주차할인
##is전기자동차() or is하이브리드자동차() 

