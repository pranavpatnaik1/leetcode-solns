#
# @lc app=leetcode id=83 lang=python
#
# [83] Remove Duplicates from Sorted List
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def deleteDuplicates(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        if not head:
            return None

        curr = head
        prev = head
        while curr.next:
            if curr.val < curr.next.val:
                curr, prev = curr.next, prev.next
            else:
                dupValue = prev.val
                while prev.next and prev.next.val == dupValue:
                    prev = prev.next
                curr.next = prev.next
                
                    
        
        return head


    
        
# @lc code=end

