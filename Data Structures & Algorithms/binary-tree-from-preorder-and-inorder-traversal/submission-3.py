# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        # base case 
        if not preorder or not inorder:
            return None
        
        root = TreeNode(preorder[0])
        split = 0
        while inorder[split] != preorder[0]:
            split += 1
        root.left = self.buildTree(preorder[1:1+split], inorder[0:split])
        root.right = self.buildTree(preorder[1+split:], inorder[split + 1:])
        return root