import random

def sort(alist):
    if len(alist) < 2:
        return alist
    mid = len(alist) / 2
    return merge(sort(alist[:mid]), sort(alist[mid:]))

def merge(left, right):
    res = []
    while left and right:
        if left[0] < right[0]:
            res.append(left.pop(0))
        else:
            res.append(right.pop(0))
            
    if len(left) > 0:
        res.extend(left)
    if len(right) > 0:
        res.extend(right)

    return res

def mergesort(alist):
    if len(alist) < 2:
        return alist
    mid = len(alist) / 2

    left, right = alist[:mid], alist[mid:]

    if len(left) > 1:
        left = mergesort(left)
    if len(right) > 1:
        right = mergesort(right)

    res = []
    while left and right:
        if left[0] < right[0]:
            res.append(left.pop(0))
        else:
            res.append(right.pop(0))
            
    if len(left) > 0:
        res.extend(left)
    if len(right) > 0:
        res.extend(right)

    return res


def main():
#    alist = range(10)
    alist = [54,26,93,17,77,31,44,55,20]
    random.shuffle(alist)

    sorted_list = sort(alist)
    merge_sorted_list = mergesort(alist)

    print(alist)
    print(sorted_list)
    print(merge_sorted_list)

if __name__ == '__main__':
    main()
