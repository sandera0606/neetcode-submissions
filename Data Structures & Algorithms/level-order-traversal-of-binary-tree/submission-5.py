# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        q = collections.deque()
        q.append(root)
        ans = []
        while q:
            layerLen = len(q)
            layer = []
            for _ in range(layerLen):
                node = q.popleft()
                if not node:
                    continue
                layer.append(node.val)
                q.append(node.left)
                q.append(node.right)
            if layer:
                ans.append(layer)
        return ans
            