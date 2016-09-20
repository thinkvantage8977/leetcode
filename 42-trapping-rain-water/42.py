class Solution(object):

    def trap(self, height):
        if not height:
            return 0
        left = [0] * len(height)
        right = [0] * len(height)

        maxLeft = height[0]

        left[0] = height[0]
        right[-1] = height[-1]

        for i in range(1, len(height)):
            maxLeft = max(maxLeft, height[i - 1])
            left[i] = maxLeft
        maxRight = height[-1]

        for i in range(len(height) - 2, 0, -1):
            maxRight = max(maxRight, height[i + 1])
            right[i] = maxRight

        water = 0

        for i in range(len(height)):
            bar = min(left[i], right[i])
            if height[i] < bar:
                water += bar - height[i]

        return water

testClass = Solution()

print(testClass.trap([0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]))
