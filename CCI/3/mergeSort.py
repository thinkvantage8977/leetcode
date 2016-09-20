

def merge(left, right):
    res = []
    while left and right:
        if left[0] < right[0]:
            res.append(left.pop(0))
        else:
            res.append(right.pop(0))
    res += left if left else right
    return res


def mergeSort(l):
    if len(l) < 2:
        return l
    mid = len(l) // 2
    left = mergeSort(l[:mid])
    right = mergeSort(l[mid:])

    return merge(left, right)


l = [12, 2, 32, 1, 2, 3, 1, 2, 2, 3, 2, 43, 1, 1, 2, 3, 1, 23, 124, 12312, 12, 31, 23, 23, 1, 2, 31, 23, 12, 3]


print(mergeSort(l))
