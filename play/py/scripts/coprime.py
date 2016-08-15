import sys

# check if a and b are coprime
# the only common divisor is 1
def is_coprime(a, b):
  for i in range(2, min(a, b) + 1):
    if a % i == 0 and b % i == 0:
      return False
  return True


if __name__ == '__main__':
  a = int(sys.argv[1])
  b = int(sys.argv[2])
  print("%d, %d" % (a, b))
  if is_coprime(a, b):
    print("is coprime")
  else:
    print("is not coprime")
