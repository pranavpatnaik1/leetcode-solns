#
# @lc app=leetcode id=35 lang=python
#
# [35] Search Insert Position
#

# @lc code=start
class Solution(object):
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        i = 0
        while i < len(nums):
            if nums[i] >= target:
                nums.insert(i, target)
                break 
            i += 1
        if target not in nums:
            nums.insert(-1, target)
            nums[-1], nums[-2] = nums[-2], nums[-1]
        
        print(nums)
        return nums.index(target)
        
# @lc code=end

