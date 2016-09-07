class Solution(object):

    def isStrobogrammatic(self, num):
        for i in str(num):
            if i in "23457":
                return False
        if str(num)[-1] == "0":
            return False
        rotate = str(num)[::-1]

        array = []

        for i in rotate:
            if i == "6":
                array.append("9")
            elif i == "9":
                array.append("6")
            else:
                array.append(i)

        return str(num) == "".join(array)
