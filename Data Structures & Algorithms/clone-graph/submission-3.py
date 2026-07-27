"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        clones = {}

        def cloneGraphRecurse(node):
            if node in clones:
                return clones[node]
            copy = Node(node.val)
            clones[node] = copy
            for n in node.neighbors:
                copy.neighbors.append(cloneGraphRecurse(n))
            
            return copy
            

        return None if node is None else cloneGraphRecurse(node)