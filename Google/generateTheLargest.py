def comparator(x, y):
    if int(str(x) + str(y)) > int(str(y) + str(x)):
        return 1
    else:
        return -1


l = [54, 546, 548, 60]

l.sort(comparator)

print(l)
