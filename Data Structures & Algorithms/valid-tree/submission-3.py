class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        # connected and no cycles
        adj = defaultdict(set)

        for a, b in edges:
            adj[a].add(b)
            adj[b].add(a)
        
        visited = set()
        
        def dfs(path, prev, node):
            if node in path:
                return False
            visited.add(node)
            path.add(node)
            for n in adj[node]:
                if n == prev:
                    continue
                if not dfs(path, node, n):
                    return False
            return True
        
        return dfs(set(), -1, 0) and len(visited) == n