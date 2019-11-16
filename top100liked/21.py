# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        def mtlHelper(n, lst):
            if n:
                lst.append(n.val)
                if n.next:
                    mtlHelper(n.next, lst)
                return lst
            else:
                return []
        
        def clnHelper(lst):
            if lst:
                node = ListNode(lst.pop())
                node.next = clnHelper(lst)
                return node
            else:
                return None
        
        n1 = mtlHelper(l1, [])
        n2 = mtlHelper(l2, [])
        m = sorted(n1 + n2, reverse=True)
        return clnHelper(m)
        