# http://interactivepython.org/runestone/static/pythonds/SortSearch/TheBubbleSort.html

# bubblesort

alist = [7,3,5,2,6,1]

#import random
#alist = range(10)
#random.shuffle(alist)

def bubblesort(alist):
  for passnum in  range(len(alist) - 1, 0, -1):
    print('passnum: ', passnum)
    for i in range(passnum):
      if alist[i] > alist[i+1]:
        alist[i], alist[i+1] = alist[i+1], alist[i]

####################
if __name__ == '__main__':
  print("original:")
  print(alist)

  print("bubble sorted:")
  bubblesort(alist)
  print(alist)

