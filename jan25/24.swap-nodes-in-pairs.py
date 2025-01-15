#
# @lc app=leetcode id=24 lang=python
#
# [24] Swap Nodes in Pairs
#

# @lc code=start
# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution(object):
    def swapPairs(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        # dummy node, simplify edge cases
        dummy = ListNode()
        dummy.next = head
        prev = dummy

        while prev.next and prev.next.next:
            # identify nodes to swap
            first = prev.next
            second = first.next

            # perform swap
            prev.next = second
            first.next = second.next
            second.next = first

            # move prev forward
            prev = first

        return dummy.next

# @lc code=end

