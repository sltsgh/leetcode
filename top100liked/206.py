# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        lst = []
        def revHelper(node, lst):
            lst.insert(0, node.val)
            if node.next:
                revHelper(node.next, lst)
                
            return lst
        
        def listHelper(lst):
            new = ListNode(lst[0])
            del lst[0]
            if lst:
                new.next = listHelper(lst)
                
            return new
        
        if head:
            lst = revHelper(head, lst)
            return listHelper(lst)
        else:
            return None
