# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if self.areEquivalentTrees(root, subRoot):
            return True
        elif not root:
            return False
        else:
            left = self.isSubtree(root.left, subRoot)
            right = self.isSubtree(root.right, subRoot)
            if left:
                return left
            return right
    
    def areEquivalentTrees(self, p, q):
        if not p and not q:
            return True
        elif p and q and p.val == q.val:
            return self.areEquivalentTrees(p.left, q.left) and self.areEquivalentTrees(p.right, q.right)
        else:
            return False