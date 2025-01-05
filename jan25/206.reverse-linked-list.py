#
# @lc app=leetcode id=206 lang=python
#
# [206] Reverse Linked List
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def reverseList(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        curr = head
        store = []
        while curr != None:
            store.append(curr.val)
            curr = curr.next
            
        curr = head
        
        i = 0
        while curr != None:
            curr.val = store[i]
            curr = curr.next
            i += 1
        
        return head
        
# @lc code=end

