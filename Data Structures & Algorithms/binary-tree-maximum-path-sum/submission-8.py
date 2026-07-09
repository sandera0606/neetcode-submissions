# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        maxPathSum = -1001
        def pathSum(node):
            nonlocal maxPathSum
            if not node:
                return 0
            leftSum = max(0, pathSum(node.left))
            rightSum = max(0, pathSum(node.right))

            maxPathSum = max(maxPathSum, leftSum + rightSum + node.val)
            return node.val + max(leftSum, rightSum)
        pathSum(root)
        return maxPathSum