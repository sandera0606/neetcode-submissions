class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        # no cycles and fully connected
        neighbours = {i : set() for i in range(n)}

        for one, two in edges:
            neighbours[one].add(two)
            neighbours[two].add(one)
        
        visited = set()

        def dfs(node, prev):
            if node in visited:
                return False
            visited.add(node)
            for neighbour in neighbours[node]:
                if neighbour == prev:
                    continue
                if not dfs(neighbour, node):
                    return False
            return True
        return dfs(0, -1) and len(visited) == n