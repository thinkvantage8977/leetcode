import random
class Solution(object):

    def __init__(self, nums):
        self.nums=nums
        

    def pick(self, target):
        cnt = 0
        res= 0
        for i in range(len(self.nums)):
            if self.nums[i] ==target:
                if random.randint(0,cnt)==0:
                    res = i
                cnt+=1
        return res
