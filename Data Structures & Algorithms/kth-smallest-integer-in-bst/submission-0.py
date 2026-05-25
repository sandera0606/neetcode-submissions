# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        myArr = []
        self.makeArray(myArr, root)
        return myArr[k - 1]
    def makeArray(self, arr, root):
        if not root:
            return
        else:
            self.makeArray(arr, root.left)
            arr.append(root.val)
            self.makeArray(arr, root.right)
        