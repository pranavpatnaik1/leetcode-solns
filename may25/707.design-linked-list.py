#
# @lc app=leetcode id=707 lang=python
#
# [707] Design Linked List
#

# @lc code=start
class ListNode:
    def __init__(self, val):
        self.val = val
        self.next = None

class MyLinkedList(object):
    def __init__(self):
        self.head = ListNode(0)
        self.size = 0

        
    def get(self, index):
        """
        :type index: int
        :rtype: int
        """
        if index >= self.size:
            return -1
        
        curr = self.head.next
        for _ in range(index):
            curr = curr.next
        
        return curr.val

    def addAtHead(self, val):
        """
        :type val: int
        :rtype: None
        """
        newNode = ListNode(val)
        newNode.next = self.head.next
        self.head.next = newNode
        self.size += 1


        
    def addAtTail(self, val):
        """
        :type val: int
        :rtype: None
        """
        curr = self.head

        while curr.next:
            curr = curr.next
        
        curr.next = ListNode(val)

        self.size += 1

    def addAtIndex(self, index, val):
        """
        :type index: int
        :type val: int
        :rtype: None
        """
        if index > self.size:
            return
        
        prev = self.head
        for _ in range(index):
            prev = prev.next

        newNode = ListNode(val)
        newNode.next = prev.next
        prev.next = newNode
        self.size += 1
                
        

    def deleteAtIndex(self, index):
        """
        :type index: int
        :rtype: None
        """
        if index >= self.size:
            return

        prev = self.head
        for _ in range(index):
            prev = prev.next
        prev.next = prev.next.next
        self.size -= 1

        


        


# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)
# @lc code=end

