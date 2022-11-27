def sum_all(start,end):
  output = 0
  for i in range(start,end+1):
    output += i
  return output

print(sum_all(0,100))


def sum_all1(start,end):
  output = 0
  for i in range(start,end+1):
    output += i
  return output

print(sum_all1(1,10))

def sum_all2(start,end):
  output = 0
  for i in range(start,end+1):
    output += i
  return output

print(sum_all2(1, 1000))

def sum_all3(start,end,step):
  output = 0
  for i in range(start,end+1,step):
    output += i
  return output

print(sum_all3(1,100,2))
def f(x):
  return 2 * x + 1
print(f(10))  


def f(x):
  return (x ** 2) + x * 2 + 1
print(f(10))



def mul(*values):
  output = 1
  for i in values:
    output *= i
  return output

print(mul(5,7,9,10))


def function(*values, valueA, valueB):
  pass
function(1,2,3,4,5,valueA=2,valueB=5)  


def function(*values, valueA=10, valueB=20):
  pass  
function(1,2,3,4,5)

def function(valueA, valueB, *values):
  pass
function(1,2,3,4,5)  

def funciton(valueA=10, valueB=20, *values):
  pass  
function(1,2,3,4,5)