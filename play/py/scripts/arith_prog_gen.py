# Fluent Python

import sys
import itertools

def arith_prog_gen0(begin, step, end=None):
  result = type(begin + step)(begin)
  forever = end is None
  index = 0
  while forever or result < end:
    yield result
    index += 1
    result = begin + step * index

def arith_prog_gen1(begin, step, end=None):
  first = type(begin + step)(begin)
  ap_gen = itertools.count(first, step)
  if end is not None:
    ap_gen = itertools.takewhile(lambda n: n < end, ap_gen)
  return ap_gen

def arith_prog_gen2(begin, step, end=None):
  first = type(begin + step)(begin)
  return itertools.takewhile(lambda n: n < end, itertools.count(first, step))


#arith_prog_gen = arith_prog_gen0
#arith_prog_gen = arith_prog_gen1
#arith_prog_gen = arith_prog_gen2

if __name__ == '__main__':
  answer = input("Which func you choose? (0,1,2): ")
  arith_prog_gen = 'arith_prog_gen%d' % int(answer)
  print("Using %s" % arith_prog_gen)
  try:
    ap_gen = eval(arith_prog_gen)(1, .5, 3)
    print(list(ap_gen))
  except NameError as e:
    sys.stdout.write("Not a valid func.\n")
