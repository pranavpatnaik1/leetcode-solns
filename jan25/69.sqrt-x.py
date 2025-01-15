#
# @lc app=leetcode id=69 lang=python
#
# [69] Sqrt(x)
#

# @lc code=start
class Solution(object):
    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        """
        if x < 2:
            return x  #the square root of 0 is 0, and of 1 is 1.
        
        low, high = 0, x // 2
        best = 0
        
        while low <= high:
            mid = (low + high) // 2
            if mid * mid == x:
                return mid  #exact match
            elif mid * mid < x:
                best = mid  #update best and search higher
                low = mid + 1
            else:
                high = mid - 1  #search lower
        
        return best  #return the largest number whose square is <= x
        


        
# @lc code=end

