#
# @lc app=leetcode id=70 lang=python
#
# [70] Climbing Stairs
#

# @lc code=start
class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        memo = {}

        def helper(distance):
            if distance == 0:  
                return 1
            if distance < 0:  
                return 0
            if distance in memo:  # check if the result is already computed.
                return memo[distance]

            memo[distance] = helper(distance - 1) + helper(distance - 2)
            return memo[distance]

        return helper(n)


# @lc code=end

