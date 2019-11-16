# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def mergeTrees(self, t1: TreeNode, t2: TreeNode) -> TreeNode:
        def mergeHelper(n1, n2):
            if not n1:
                return n2
            if not n2:
                return n1
                
            new = TreeNode(n1.val + n2.val)
            new.left = mergeHelper(n1.left, n2.left)
            new.right = mergeHelper(n1.right, n2.right)
            return new
        
        return mergeHelper(t1, t2)
        