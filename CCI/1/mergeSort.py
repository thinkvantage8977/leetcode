def mergeSort(l):
    if len(l) <= 1:
        return l
    mid = len(l) // 2
    left = mergeSort(l[:mid])
    right = mergeSort(l[mid:])
    return merge(left, right)


def merge(left, right):
    if not left:
        return right
    if not right:
        return left

    res = []

    p1 = p2 = 0

    while p1 < len(left) and p2 < len(right):
        if left[p1] < right[p2]:
            res.append(left[p1])
            p1 += 1
        else:
            res.append(right[p2])
            p2 += 1

    while p1 < len(left):
        res.append(left[p1])
        p1 += 1

    while p2 < len(right):
        res.append(right[p2])
        p2 += 1

    return res


l = [1, 2, 3, 4, 1, 2, 2, 43, 1, 2, 3, 1, 2, 3, 1, 2, 1, 1, 23, 1, 3, 12, 3, 23, 2, 3, 1, 21, 23, 123, 1, 1, 23, 1, 3, 123, 12, 3]

print(mergeSort(l))
