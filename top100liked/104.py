# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        def helper(t, n):
            if t.left:
                nl = n + helper(t.left, n)
            else:
                nl = n
            
            if t.right:
                nr = n + helper(t.right, n)
            else:
                nr = n
            return max(nl, nr)
            
        if root:
            return helper(root, 1)
        else:
            return 0
            