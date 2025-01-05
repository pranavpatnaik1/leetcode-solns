#
# @lc app=leetcode id=707 lang=python
#
# [707] Design Linked List
#

# @lc code=start
class MyLinkedList(object):

    def __init__(self):
        self.head = 0
        self.next = None

    def get(self, index):
        """
        :type index: int
        :rtype: int
        """
        curr = self.head
        for _ in range(index):
            curr = curr.next
        return curr     
        

    def addAtHead(self, val):
        """
        :type val: int
        :rtype: None
        """
        

    def addAtTail(self, val):
        """
        :type val: int
        :rtype: None
        """
        

    def addAtIndex(self, index, val):
        """
        :type index: int
        :type val: int
        :rtype: None
        """
        

    def deleteAtIndex(self, index):
        """
        :type index: int
        :rtype: None
        """
        


# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)
# @lc code=end

