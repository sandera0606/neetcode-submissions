class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        # no cycles and connected
        adj = defaultdict(set)
        for a, b in edges:
            adj[a].add(b)
            adj[b].add(a)

        explored = 0
        
        def dfs(path, prev, n):
            if n in path:
                return False
            nonlocal explored
            explored += 1

            path.add(n)

            for neigh in adj[n]:
                if neigh == prev:
                    continue
                if not dfs(path, n, neigh):
                    return False
            path.remove(n)
            return True

        path = set()
        return dfs(path, -1, 0) and explored == n