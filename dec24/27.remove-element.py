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
        i = 0
        while i < len(nums):  # Use a while loop for manual index control
            if nums[i] == val:
                nums.pop(i)  # Remove the element
            else:
                i += 1  # Only increment if no removal
        return len(nums)
        
# @lc code=end

