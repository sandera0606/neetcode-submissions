class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # populate prerequisites list
        prereqs = {i: set() for i in range(numCourses)}

        for crs, pre in prerequisites:
            prereqs[crs].add(pre)
        
        # dfs
        def dfs(visited, cur):
            if not prereqs[cur]:
                return True
            if cur in visited:
                return False
            visited.add(cur)
            for pre in prereqs[cur]:
                if not dfs(visited, pre):
                    return False
            visited.remove(cur)
            prereqs[cur] = [] # no cycles
            return True
        
        for crs in range(numCourses):
            visited = set()
            if not dfs(visited, crs):
                return False
        return True