# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        cur = 0
        val = -1

        def dfs(node):
            nonlocal cur, val
            if not node:
                return
            dfs(node.left)
            cur += 1
            if cur == k:
                val = node.val
                return 
            dfs(node.right)
        dfs(root)
        return val