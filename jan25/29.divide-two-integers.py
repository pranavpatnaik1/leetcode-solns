#
# @lc app=leetcode id=29 lang=python
#
# [29] Divide Two Integers
#

# @lc code=start
class Solution(object):
    def divide(self, dividend, divisor):
        """
        :type dividend: int
        :type divisor: int
        :rtype: int
        """
        # handle edge case for zero dividend
        if dividend == 0:
            return 0
        
        # handle sign of the result
        sign = 1 if (dividend < 0) == (divisor < 0) else -1

        # work with absolute values for binary search
        dividend, divisor = abs(dividend), abs(divisor)
        low, high = 0, dividend

        # binary search
        while low <= high:
            mid = low + (high - low) // 2
            if mid * divisor <= dividend:
                low = mid + 1
            else:
                high = mid - 1 

        # clamp to 32-bit range
        result = sign * high
        return max(-2**31, min(result, 2**31 - 1))


# @lc code=end

