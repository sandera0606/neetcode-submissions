# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        ans = []
        self.levelOrderRecurse(root, 0, ans)
        return ans

    def levelOrderRecurse(self, node, level, levels):
        if not node:
            return
        if len(levels) <= level:
            levels.append([node.val])
        else:
            levels[level].append(node.val)
        self.levelOrderRecurse(node.left, level + 1, levels)
        self.levelOrderRecurse(node.right, level + 1, levels)