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

    result = [0] * (len(left) + len(right))

    p1 = p2 = 0

    while p1 < len(left) and p2 < len(right):
        if left[p1] < right[p2]:
            result[p1 + p2] = left[p1]
            p1 += 1
        else:
            result[p1 + p2] = right[p2]
            p2 += 1

    while p1 < len(left):
        result[p1 + p2] = left[p1]
        p1 += 1

    while p2 < len(right):
        result[p1 + p2] = right[p2]
        p2 += 1
    return result

l = [1, 2, 2, 3, 4, 2, 12, 3, 12, 1, 23, 123, 2, 321, 21, 23, 2,
     31, 2, 3, 12, 31, 23, 1, 32443, 65, 7, 56, 22, 34, 2, 221]


print(mergeSort(l))
