
def fib(n):
  a, b = 0, 1
  while b < n:
    yield a
    a, b = b, a+b

idx = 0
for i in fib(10 ** 12):
  print(idx, i)
  idx += 1



