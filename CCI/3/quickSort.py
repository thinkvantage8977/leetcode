def quickSort(l, begin, end):
    if begin >= end:
        return
    i = begin + 1
    j = end
    pivot = l[begin]

    while i <= j:
        if l[i] > pivot:
            l[i], l[j] = l[j], l[i]
            j -= 1
        else:
            i += 1
    l[begin], l[j] = l[j], l[begin]

    quickSort(l, begin, j - 1)
    quickSort(l, j + 1, end)


l = [12, 2, 32, 1, 2, 3, 1, 2, 2, 3, 2, 43, 1, 1, 2, 3, 1, 23, 124, 12312, 12, 31, 23, 23, 1, 2, 31, 23, 12, 3]



quickSort(l, 0, len(l) - 1)

print(l)
