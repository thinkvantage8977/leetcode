def insertMtoN(m, n, i, j):
    return (((n >> (j + 1)) << (j - i + 1)) | m) << i


print(bin(insertMtoN(0b10011, 0b10000000000, 2, 6)))
