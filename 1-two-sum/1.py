#Solution Class
class Solution(object):
	def twoSum(self, nums, target):
	    numsDict = {}
	    for index1,value1 in enumerate(nums):
		    numsDict[value1] = index1
	    for index1,value1 in enumerate(nums):
		    if (target - value1 in numsDict and numsDict[target - value1] != index1):
			    return index1,numsDict[target - value1]



#Setup testClass
testClass = Solution()

#Test input
numslist = [3,2,4]
target = 6

#Run
result = testClass.twoSum(numslist,target)

#Print
print (result)