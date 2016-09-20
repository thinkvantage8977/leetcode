def encode(s):
    if not s:
        return s

    res = []
    current = s[0]
    counter = 0

    s = s + "@"
    for c in s:
        if c == current:
            counter += 1

        else:
            res.append(str(counter))
            res.append("x")
            res.append(current)

            current = c
            counter = 1

    return "".join(res)


def decode(s):

    res = []

    counter = ""

    i = 0
    while i < len(s):
        if s[i] in ["1", "2", "3", "4", "5", "6", "7", "8", "9"]:
            counter += s[i]
            i += 1
            continue
        elif s[i] != "x":
            return ""
        i += 1
        target = s[i]
        res.append(target * int(counter))
        i += 1
        counter = ""

    return "".join(res)

print(encode("aaaabbcceerqdqcadiadj"))
print(decode("4xa2xb2xc2xe1xr1xq1xd1xq1xc1xa1xd1xi1xa1xd1xj"))
