# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def invertTree(self, root: TreeNode) -> TreeNode:
        def invertHelper(n):
            new = TreeNode(n.val)
            if n.left:
                new.right = invertHelper(n.left)
                
            if n.right:
                new.left = invertHelper(n.right)
                
            return new
        
        if root:
            return invertHelper(root)
        else:
            return None
