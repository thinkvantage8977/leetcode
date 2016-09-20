class Codec:

    def encode(self, strs):
        sb = []
        for s in strs:
            sb.append(str(len(s)))
            sb.append("#")
            sb.append(s)
        return "".join(sb)

    def decode(self, s):
        res = []

        while s:
            tag = s.index("#")
            length = int(s[:tag])
            res.append(s[tag + 1:1 + tag + length])
            s = s[1 + tag + length:]

        return res


# Your Codec object will be instantiated and called as such:
codec = Codec()
print(codec.decode(codec.encode(["123", "234", "456", "789"])))
