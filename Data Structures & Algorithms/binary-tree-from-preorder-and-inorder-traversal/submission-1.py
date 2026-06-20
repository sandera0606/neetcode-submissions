# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        return self.buildTreeRecurse(preorder, inorder, 0, len(preorder) - 1, 0, len(preorder) - 1)
        
    def buildTreeRecurse(self, preorder, inorder, prel, prer, l, r):
        if prer < prel or r < l:
            return None
        val = preorder[prel]
        node = TreeNode(val)

        m = l
        while(m < r and inorder[m] != val):
            m += 1
        left_size = m - l

        node.left = self.buildTreeRecurse(preorder, inorder, prel + 1, prel + left_size + 1, l, m - 1)
        node.right = self.buildTreeRecurse(preorder, inorder, prel + left_size + 1, prer, m + 1, r)

        return node