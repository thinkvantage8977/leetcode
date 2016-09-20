
def merge(l, r):
    res = []

    while l and r:
        res.append(l.pop(0) if l[0] < r[0] else r.pop(0))

    res += l if l else r

    return res


def mergeSort(l):
    if len(l) == 1:
        return l
    mid = len(l) // 2
    left = mergeSort(l[:mid])
    right = mergeSort(l[mid:])

    return merge(left, right)

l = [12, 2, 32, 1, 2, 3, 1, 2, 2, 3, 2, 43, 1, 1, 2, 3, 1, 23, 124, 12312, 12, 31, 23, 23, 1, 2, 31, 23, 12, 3]


print(mergeSort(l))
