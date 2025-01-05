#
# @lc app=leetcode id=704 lang=python
#
# [704] Binary Search
#

# @lc code=start
class Solution(object):
    def search(self, nums, target):
        low = 0
        high = len(nums)-1
        curr = (low+high)//2
        while low<=high:
            if nums[curr] < target:
                low = curr+1
            elif nums[curr] > target:
                high = curr-1
            else:
                return curr 
            curr = (low+high)//2
        
        return -1




        
# @lc code=end

