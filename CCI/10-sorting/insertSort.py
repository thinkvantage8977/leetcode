def insertSort(l):
    if len(l) <= 1:
        return

    for i in range(1, len(l)):
        current = l[i]

        j = i - 1

        while j >= 0 and l[j] > current:
            l[j + 1] = l[j]
            j -= 1
        l[j + 1] = current


l = [2, 3, 4, 12, 2, 3, 4, 1, 21, 22, 3, 212, 1, 21, 233]

insertSort(l)
print(l)
