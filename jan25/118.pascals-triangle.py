#
# @lc app=leetcode id=118 lang=python
#
# [118] Pascal's Triangle
#

# @lc code=start
class Solution(object):
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        if numRows == 1:
            return [[1]]
        
        res = [[1]]  # Start with the first row
        
        for _ in range(1, numRows):
            prev_row = res[-1]
            # Compute the next row using sums of adjacent elements in `prev_row`
            new_row = [1] + [prev_row[i] + prev_row[i + 1] for i in range(len(prev_row) - 1)] + [1]
            res.append(new_row)
        
        return res
        
# @lc code=end

