#
# @lc app=leetcode id=26 lang=python
#
# [26] Remove Duplicates from Sorted Array
#

# @lc code=start
class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        w_index = 1

        for i in range(1, len(nums)):
            if nums[i] > nums[i-1]: # if there exists an increase
                nums[w_index] = nums[i]
                w_index += 1
        
        return w_index



# @lc code=end

