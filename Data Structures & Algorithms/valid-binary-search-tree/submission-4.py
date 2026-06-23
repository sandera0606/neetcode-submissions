# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        return self.isValidBSTRecurse(root, -1001, 1001)
        
    def isValidBSTRecurse(self, node, min, max):
        if not node:
            return True
        if min < node.val < max:
            return self.isValidBSTRecurse(node.left, min, node.val) and self.isValidBSTRecurse(node.right, node.val, max)
        return False
