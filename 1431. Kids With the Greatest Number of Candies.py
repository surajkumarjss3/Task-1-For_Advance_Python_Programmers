class Solution(object):
    def kidsWithCandies(self, candies, extraCandies):
        """
        :type candies: List[int]
        :type extraCandies: int
        :rtype: List[bool]
        """
        a=[]
        g=max(candies)
        for i in candies:
            sum=i+extraCandies
            if(sum>=g):
                a.append(True)
            else:
                a.append(False)
        return(a)
