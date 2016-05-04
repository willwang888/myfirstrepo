import random


def qsort(list):
    if not list:
        return []
    else:
        pivot = list[0]
        less = [x for x in list     if x <  pivot]
        more = [x for x in list[1:] if x >= pivot]
        return qsort(less) + [pivot] + qsort(more)



a = range(10)
random.shuffle(a)

#a = [9,4,6,2,9,1]
print a

print qsort(a)
