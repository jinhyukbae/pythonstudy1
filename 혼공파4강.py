# 식별자 (identifier)
x y z i j h f m a c r
i j h
input output list print

# 식별자 파이썬 자체가 강제하는 규칙
1. 키워드를 사용하면 안 됨 if=3.14 x
2. 특수문자는 _ 만 허용 & = 3.14 x
3. 숫자로 시작하면 안 됨 10a = 3.14 x
4. 공백 쓰면 안 됨 a b c = 3.14 x

# 개발자들이 정한 규칙
1. 최대한 알파벳을 사용하자
2. 의미 없는 단어보단 의미있는 단어를 사용하자
file = 10
text = 20
3. 스네이크케이스와 캐멀케이스를 사용하자 
sendtouser
send_to_user #스네이크 케이스
SendToUser   # 캐멀 케이스
animal : 스네이크 케이스
Animal : 캐멀 케이스
캐멀케이스면 클래스
스네이크 케이스면 
뒤에 괄호가 있으면 함수
없으면 변수 

다음코드 식별자가 클래스인지 변수인지 함수인지 구분해보시오
1.print() 소문자로 시작하므로 스네이크 케이스 뒤에 괄호가 있으므로 함수
2.list() 함수
3.soup.select() 함수
4.math.pi 소문자로 시작하므로 스네이크 케이스 뒤에 괄호가 없으므로 변수
5.math.e 변수
6.class Animal: 클래스
7.BeautifulSoup() 클래스