
import random

alist = range(10)
random.shuffle(alist)

print(alist)

def merge1(alist):
  mid = len(alist) / 2
  left, right = alist[:mid], alist[mid:]

  if len(left) > 1:
    left = merge(left)
  if len(right) > 1:
    right = merge(right)

  res = []
  while left and right:
    if left[0] < right[0]:
      res.append(left.pop(0))
    else:
      res.append(right.pop(0))

  return res + (left or right)


def merge2(alist):
  mid = len(alist) / 2
  left, right = alist[:mid], alist[mid:]

  if len(left) > 1:
    left = merge(left)
  if len(right) > 1:
    right = merge(right)

  res = []
  while left and right:
    if left[-1] < right[-1]:
      res.append(right.pop())
    else:
      res.append(left.pop())

  res.reverse()
  return (left or right) + res

merge = merge1
#merge = merge2

print merge((alist))

