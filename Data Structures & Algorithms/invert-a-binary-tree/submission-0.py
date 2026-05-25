# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        return self.invertTreeRecurs(root)
    
    def invertTreeRecurs(self, node):
        if node:
            temp = node.left
            node.left = self.invertTreeRecurs(node.right)
            node.right = self.invertTreeRecurs(temp)
        else:
            return None
        
        return node