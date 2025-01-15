#
# @lc app=leetcode id=86 lang=python
#
# [86] Partition List
#

# @lc code=start
# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution(object):
    def partition(self, head, x):
        """
        :type head: Optional[ListNode]
        :type x: int
        :rtype: Optional[ListNode]
        """
        if not head:
            return None
        
        less_head = ListNode(0)
        more_head = ListNode(0)
        
        less = less_head
        more = more_head
        curr = head
        
        # partition
        while curr:
            if curr.val < x:
                less.next = curr
                less = less.next
            else:
                more.next = curr
                more = more.next
            curr = curr.next
        
        # terminate partition
        more.next = None
        
        # connect partitions
        less.next = more_head.next
        
        return less_head.next
