def quickSort(nums, start, end):
    if start >= end:
        return
    pivot = nums[start]
    i, j = start + 1, end
    while (i <= j):
        if nums[i] > pivot:
            nums[i], nums[j] = nums[j], nums[i]
            j -= 1
        else:
            i += 1
    nums[start], nums[j] = nums[j], nums[start]

    quickSort(nums, start, j - 1)
    quickSort(nums, j + 1, end)


l = [2, 32, 34, 3, 1, 2, 3, 87, 1, 23, 23, 1, 23]

quickSort(l, 0, len(l) - 1)

print(l)
