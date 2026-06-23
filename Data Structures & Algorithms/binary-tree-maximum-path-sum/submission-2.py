# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        maxSum = root.val
        def pathSum(node):
            nonlocal maxSum
            if node is None:
                return 0
            curSum = node.val + max(pathSum(node.left), 0) + max(pathSum(node.right), 0)
            maxSum = max(maxSum, curSum)
            return node.val + max(pathSum(node.left), pathSum(node.right), 0)
        pathSum(root)
        return maxSum