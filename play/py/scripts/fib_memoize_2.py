
memo = {}

def fib(n):
  if n in memo:
    return memo[n]

  if n < 2:
    memo[n] = n
    return n

  memo[n] = fib(n-1) + fib(n-2)

  return memo[n]


for i in range(50):
  print(i, fib(i))
