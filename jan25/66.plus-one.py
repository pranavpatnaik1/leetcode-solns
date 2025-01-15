#
# @lc app=leetcode id=66 lang=python
#
# [66] Plus One
#

# @lc code=start
class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        if digits[-1] == 9:
            i = -1
            while digits[i] == 9 and i*-1 != len(digits):
                i -= 1
            if digits[i] != 9:
                i += 1
            zeros = i * -1
            print(zeros)
            if zeros == len(digits):
                digits = [1] + [0] * zeros
            else:
                digits[i:] = [0] * zeros
                digits[i-1] += 1
        else:
            digits[-1] += 1
            
        return digits
                    
        
# @lc code=end

