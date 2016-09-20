
def quickSort(l, start, end):
    if start >= end:
        return
    left = start + 1
    right = end
    mid = left + right // 2

    pivot = l[start]

    while left <= right:
        if l[left] > pivot:
            l[left], l[right] = l[right], l[left]
            right -= 1
        else:
            left += 1
    l[right], l[start] = l[start], l[right]

    quickSort(l, start, right - 1)
    quickSort(l, right + 1, end)


l = [12, 2, 32, 1, 2, 3, 1, 2, 2, 3, 2, 43, 1, 1, 2, 3, 1, 23, 124, 12312, 12, 31, 23, 23, 1, 2, 31, 23, 12, 3]


quickSort(l, 0, len(l) - 1)

print(l)
