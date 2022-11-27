#팩토리얼 연산
#n! = n * (n-1) * (n-2)
#3! 3 * 2 * 1


#반복문으로 구현
def factorial(n):
  output = 1
  for i in range(1, n + 1):
    output *= i
  return output


print(factorial(2))
print(factorial(3))
print(factorial(4))
print(factorial(5))

#수학의 수열의 점화식
#이웃한 항의 관계를 통해 수열을 나타내는 것

#팩토리얼 점화식
#1! = 1
#n! = n * (n-1)!


#재귀함수
def factorial2(n):
  if n == 1:
    return 1  #1! = 1에 해당
  elif n >= 2:
    return n * factorial2(n - 1)


print(factorial2(5))

# factorial5는 n=5 5 * facotrial 5-1 = 4 factorial 4이고

#factorial4는 n = 4 4 * factorial 4-1 = 3 factorial3 이고 를

# 1까지 반복 n== 1이면 1이고

#2면 2 * 1 = 2 3이면 3 * 2 = 6 4면 4 * factorial3의 값 6 곱하면 24

#5면 5 * factorial4의 값 24를 곱하면 120
