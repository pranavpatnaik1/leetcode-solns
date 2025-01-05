#
# @lc app=leetcode id=27 lang=python
#
# [27] Remove Element
#

# @lc code=start
class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        w_index = 0

        for i in range(len(nums)):
            if nums[i] != val:
                nums[w_index] = nums[i]
                w_index += 1
        
        return w_index
        
# @lc code=end

