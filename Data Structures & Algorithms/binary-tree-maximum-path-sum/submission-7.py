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
            if not node:
                return 0
            val = node.val
            left = max(0, pathSum(node.left))
            right = max(0, pathSum(node.right))
            maxSum = max(maxSum, val + left + right)
            return val + max(left, right)
        
        pathSum(root)
        return maxSum