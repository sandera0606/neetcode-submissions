# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Codec:
    
    # Encodes a tree to a single string.
    def serialize(self, root: Optional[TreeNode]) -> str:
        ans = ""
        q = collections.deque()
        q.append(root)

        while q:
            node = q.popleft()
            if not node:
                ans += "N,"
            else:
                ans += str(node.val) + ","
                q.append(node.left)
                q.append(node.right)

        return ans
        
    # Decodes your encoded data to tree.
    def deserialize(self, data: str) -> Optional[TreeNode]:
        q = collections.deque()
        nodes = collections.deque(data.split(',')) # array of values

        root = self.getNode(nodes.popleft())

        q.append(root)

        while q:
            cur = q.popleft()
            if not cur:
                continue
            left = self.getNode(nodes.popleft())
            right = self.getNode(nodes.popleft())
            cur.left = left
            cur.right = right
            q.append(left)
            q.append(right)
        
        return root

    def getNode(self, val):
        if val == 'N':
            return None
        else:
            return TreeNode(int(val))
