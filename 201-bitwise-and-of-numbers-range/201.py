#我们只要写代码找到左边公共的部分即可，我们可以从建立一个32位都是1的mask，
#然后每次向左移一位，比较m和n是否相同，不同再继续左移一位，直至相同，然后把m和mask相与就是最终结果
class Solution(object):

    def rangeBitwiseAnd(self, m, n):
        shitfCounter = 0

        while m != n:
            m >>= 1
            n >>= 1
            shitfCounter += 1
        return m << shitfCounter

