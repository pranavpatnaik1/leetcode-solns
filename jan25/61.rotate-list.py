#
# @lc app=leetcode id=61 lang=python
#
# [61] Rotate List
#

# @lc code=start
# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution(object):
    def rotateRight(self, head, k):
        """
        :type head: Optional[ListNode]
        :type k: int
        :rtype: Optional[ListNode]
        """
        curr = head
        if curr == None:
            return head
        length = 1
        while curr.next:
            curr = curr.next
            length += 1
        tail = curr

        k %= length
        if k == 0:
            return head

        # traverse again
        curr = head
        for _ in range(length - k - 1):
            curr = curr.next
        
        new_tail = curr
        tail.next = head
        head = new_tail.next
        new_tail.next = None

        return head




# @lc code=end

