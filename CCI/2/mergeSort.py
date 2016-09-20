def mergeSort(l):
    if len(l) < 2:
        return l
    mid = len(l) // 2
    left = mergeSort(l[:mid])
    right = mergeSort(l[mid:])

    return merge(left, right)


def merge(l, r):
    res = []
    while l and r:
        if l[0] < r[0]:
            res.append(l.pop(0))
        else:
            res.append(r.pop(0))
    return res + l if l else res + r


l = [9, 1]

print(mergeSort(l))
