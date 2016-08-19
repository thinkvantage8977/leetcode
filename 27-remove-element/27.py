class Solution(object):
    def removeElement(self, nums, val):
        newi = 0
        for i in range(0,len(nums)):
        	if nums[i]!=val:
        		nums[newi]=nums[i]
        		newi+=1

        return newi



testClass= Solution()

nums = [3,2,2,3]



print(testClass.removeElement(nums,3))

print(nums)
        