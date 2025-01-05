#
# @lc app=leetcode id=19 lang=python
#
# [19] Remove Nth Node From End of List
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: Optional[ListNode]
        :type n: int
        :rtype: Optional[ListNode]
        """
        # two pointers, linked list
        if head.next == None: # EC: length of LL == 1
            return None
        
        # create length n gap btwn fast & slow

        fast = head
        for i in range(n):
            fast = fast.next
        
        slow = head
        if fast == None: # edge case: length of LL == n
            head = slow.next
            return head
        
        while fast.next != None:
            fast = fast.next
            slow = slow.next
        
        slow.next = slow.next.next # skip

        return head


# @lc code=end

