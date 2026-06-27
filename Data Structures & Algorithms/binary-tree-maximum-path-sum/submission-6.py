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
            left = pathSum(node.left)
            right = pathSum(node.right)
            maxSum = max(maxSum, val + max(0, left) + max(0, right))
            return val + max(left, right, 0)
        
        pathSum(root)
        return maxSum