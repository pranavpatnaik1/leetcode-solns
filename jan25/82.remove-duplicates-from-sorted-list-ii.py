#
# @lc app=leetcode id=82 lang=python
#
# [82] Remove Duplicates from Sorted List II
#

# @lc code=start
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution(object):
    def deleteDuplicates(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        # dummy node 
        dummy = ListNode(-1)
        dummy.next = head
        prev = dummy  
        curr = head   

        while curr:
            # if the current node is the start of a duplicate sequence
            if curr.next and curr.val == curr.next.val:
                # skip all nodes with the same value
                dupValue = curr.val
                while curr and curr.val == dupValue:
                    curr = curr.next
                # connect prev.next to the node after the duplicate block
                prev.next = curr
            else:
                # no duplicate, so move prev forward
                prev = curr
                curr = curr.next

        return dummy.next

        




# @lc code=end

