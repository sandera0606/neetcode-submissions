"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    visited = {}

    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node:
            return node
        
        if not node.neighbors:
            return Node(node.val)
        
        if node in self.visited:
            return self.visited[node]
        
        start = Node(node.val)
        self.visited[node] = start
        neighbors = []

        for neighbour in node.neighbors:
            neighbors.append(self.cloneGraph(neighbour))

        start.neighbors = neighbors
        return start