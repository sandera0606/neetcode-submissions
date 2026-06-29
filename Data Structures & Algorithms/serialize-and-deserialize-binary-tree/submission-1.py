# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Codec:
    
    # Encodes a tree to a single string.
    def serialize(self, root: Optional[TreeNode]) -> str:
        q = collections.deque()
        q.append(root)
        res = ""

        while q:
            node = q.popleft()
            if not node:
                res += "N,"
                continue
            res += str(node.val) + ","
            q.append(node.left)
            q.append(node.right)
        return res
        
    # Decodes your encoded data to tree.
    def deserialize(self, data: str) -> Optional[TreeNode]:
        parsed = data.split(',')
        root = self.toNode(parsed[0])
        if not root:
            return root
        q = collections.deque()
        q.append(root)
        i = 1
        while q:
            cur = q.popleft()
            cur.left = self.toNode(parsed[i])
            cur.right = self.toNode(parsed[i+1])
            if cur.left:
                q.append(cur.left)
            if cur.right:
                q.append(cur.right)
            i += 2
        return root
    
    def toNode(self, data):
        if data == 'N':
            return None
        return TreeNode(int(data))