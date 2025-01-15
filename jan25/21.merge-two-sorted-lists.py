#
# @lc app=leetcode id=21 lang=python
#
# [21] Merge Two Sorted Lists
#

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution(object):
    def mergeTwoLists(self, list1, list2):
        """
        :type list1: Optional[ListNode]
        :type list2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        skip = ListNode()
        curr = skip
        while list1 and list2:
            if list1.val > list2.val:
                curr.next = list2
                list2 = list2.next
            else:
                curr.next = list1
                list1 = list1.next
            curr = curr.next
        
        curr.next = list1 if list1 else list2
        
        return skip.next




        
# @lc code=end

