class Solution(object):
    def runningSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        Sum=0
        a=[]
        for i in range(len(nums)):
            Sum=Sum+nums[i]
            a.append(Sum)
        return(a)  
