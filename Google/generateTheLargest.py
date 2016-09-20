import functools


# compare the pair by xy vs xy
def comparator(x, y):
    if int(str(x) + str(y)) > int(str(y) + str(x)):
        return -1
    else:
        return 1


l = [54, 546, 548, 60]

l.sort(key=functools.cmp_to_key(lambda x, y: comparator(x, y)))
print(l)
