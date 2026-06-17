# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        maxVal = 1001
        minVal = -1001
        return self.isValidBSTRecurse(root, maxVal, minVal)

    def isValidBSTRecurse(self, node, max = None, min = None):
        if node is None:
            return True
        if node.val >= max or node.val <= min:
            return False
        return self.isValidBSTRecurse(node.left, node.val, min) and self.isValidBSTRecurse(node.right, max, node.val)