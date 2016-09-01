class Solution(object):

    def maximumGap(self, nums):
        if len(nums) < 2:
            return 0
        maxValue = -float("inf")
        minValue = float("inf")
        for i in nums:
            maxValue = max(maxValue, i)
            minValue = min(minValue, i)

        BucketSize = (maxValue - minValue) // len(nums) + 1
        BucketCount = (maxValue - minValue) // BucketSize + 1

        # print("max = {}, min = {}, size = {}".format(
        #     maxValue, minValue, BucketSize))

        Buckets = []
        for i in range(BucketCount):
            Buckets.append([float("inf"), -float("inf")])

        for i in nums:
            location = (i - minValue) // BucketSize
            # print("location = {} , i ={}".format(location, i))
            # print(Buckets)
            Buckets[location][0] = min(Buckets[location][0], i)
            Buckets[location][1] = max(Buckets[location][1], i)

        ans = 0
        prv = Buckets[0]
        print(Buckets)
        for i in range(1, len(Buckets)):
            if Buckets[i][0] == float("inf") or Buckets[i][1] == -float("inf"):
                continue
            # print(i)
            ans = max(ans,  Buckets[i][0] - prv[1])
            prv = Buckets[i]

        return ans


testClass = Solution()

l = [1, 10000000]


print(testClass.maximumGap(l))
