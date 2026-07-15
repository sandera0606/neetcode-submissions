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

        def cloneRecurse(node):
            cloned = Node(node.val)
            clones[node] = cloned
            if node.neighbors:
                clonedNeighbours = []
                cloned.neighbors = clonedNeighbours
                for neighbour in node.neighbors:
                    if neighbour in clones:
                        clonedNeighbours.append(clones[neighbour])
                    else:
                        clonedNeighbours.append(cloneRecurse(neighbour))
            return cloned
        return None if not node else cloneRecurse(node)