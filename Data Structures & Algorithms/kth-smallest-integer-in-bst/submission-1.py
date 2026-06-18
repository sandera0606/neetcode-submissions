# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        cnt = 0
        cur = None

        def traverse(node):
            nonlocal cnt, cur
            if not node:
                return
            traverse(node.left)
            cnt += 1
            if cnt == k:
                cur = node
                return
            traverse(node.right)
        
        traverse(root)
        return cur.val