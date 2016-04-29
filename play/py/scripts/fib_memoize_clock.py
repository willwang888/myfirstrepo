
import functools
import time

def clock(f):
  @functools.wraps(f)
  def clocked(*args, **kwargs):
    t0 = time.time()
    res = f(*args, **kwargs)
    elapsed = time.time() - t0
    name = f.__name__
    arg_list = []
    if args:
      arg_list.append(', '.join(repr(arg) for arg in args))
    if kwargs:
      pairs = ['%s=%r' % (k,w) for k, w in sorted(kwargs.items())]
      arg_list.append(', '.join(pairs))
    arg_str = ', '.join(arg_list)
    print('[%0.8f] %s(%s) -> %r ' % (elapsed, name,arg_str, res))
    return res
  return clocked

def memoize(f):
  cache = {}
  def wrapper(n):
    if n not in cache:
      cache[n] = f(n)
    return cache[n]
  return wrapper


@memoize
@clock
def fib(n):
  if n < 2:
    return n
  return fib(n-1) + fib(n-2)


print fib(6)

#for i in range(10):
#  print(i, fib(i))

