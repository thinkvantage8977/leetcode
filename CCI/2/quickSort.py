def quickSort(l, start, end):
    print(l)
    if start >= end:
        return

    pivot = l[start]
    left, right= start + 1,end

    while left <= right:
        if l[left] > pivot:
            l[left], l[right] = l[right], l[left]
            right -= 1
        else:
            left += 1

    l[start], l[right] = l[right], l[start]

    quickSort(l, start, right - 1)
    quickSort(l, right + 1, end)


l = [1, 2, 3, 4]


quickSort(l, 0, len(l) - 1)
print(l)
