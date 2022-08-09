class Solution(object):
    def shuffle(self, nums, n):
        """
        :type nums: List[int]
        :type n: int
        :rtype: List[int]
        """
        a=[]
        i=0
        while i<n:
            a.append(nums[i])
            a.append(nums[n+i])
            i=i+1
        return(a)
    
