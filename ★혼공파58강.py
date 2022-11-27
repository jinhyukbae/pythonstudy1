# 피보나치 수열
# a_1 = 1
# a_2 = 1
# a_n = a {n-1} + a{n-2}
# a_3 = 1 + 1 = 2
# a_4 = a_3 + a_2 2 + 1 = 3
# a_5 = a_4 + a_3 3 + 2 = 5
# a_6 = a_5 + a_4 5 + 3 = 8
# a_7 = a_6 + a_5 8 + 5 = 13
# a_8 = a_7 + a_6 13 + 8 = 21
# a_9 = a_8 + a_7 21 + 13 = 34
# a_10 = a_9 + a_8 34 + 21 = 55


def f(n):
  if n == 1:
    return 1
  if n == 2:
    return 1
  else:
    return f(n - 1) + f(n - 2)


print(f(10))

#f(5) = f(4) + f(3) 3 + 2 = 5
#f(4) = f(3) + f(2) 2+1= 3
#f(3) = f(2) + f(1) 1+1 = 2

memo = {}
def g(n):
  if n in memo: #g(n)을 호출했는데 만약 n이 메모에 있으면
    return memo[n] #memo에 있는 n을 리턴해줘라
  if n == 1:
    return 1
  if n == 2:
    return 1
  else:
    temp = g(n - 1) + g(n - 2)
    memo[n] = temp
    return temp

print(g(50))

memo = {1:1, 2:1}
def h(n):
  if n in memo:
    return memo[n]
  else:
    temp = h(n - 1) + h(n - 2)
    memo[n] = temp
    return temp

print(h(50))

# memo = {1:1, 2:1}
# def i(n):
#   if n in memo:
#     return memo[n]
#   else:
#     return memo[n] :=i(n - 1) + i(n - 2)
#파이썬 최신 문법 := 바다사자 문법 

# print(i(50))