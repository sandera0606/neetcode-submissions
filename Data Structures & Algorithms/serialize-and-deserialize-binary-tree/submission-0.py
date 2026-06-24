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
        s = ""

        while q:
            layer = len(q)
            for _ in range(layer):
                node = q.popleft()
                if node:
                    s += str(node.val) + "."
                    q.append(node.left)
                    q.append(node.right)
                else:
                    s += "N."
        return s
        
    # Decodes your encoded data to tree.
    def deserialize(self, data: str) -> Optional[TreeNode]:
        data = collections.deque(data.split("."))
        if not data:
            return None

        q = collections.deque()
        root = self.getTreeNode(data.popleft())
        if not root: 
            return
        q.append(root)
        
        while q:
            node = q.popleft()
            left = self.getTreeNode(data.popleft())
            right = self.getTreeNode(data.popleft())
            node.left = left
            node.right = right
            if left:
                q.append(left)
            if right:
                q.append(right)
        return root


    def getTreeNode(self, val):
        if val == "N":
            return None
        else:
            return TreeNode(int(val)) 
            
            