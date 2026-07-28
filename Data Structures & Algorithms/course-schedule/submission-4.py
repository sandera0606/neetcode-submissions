class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        prereq = defaultdict(set)

        for crs, pre in prerequisites:
            prereq[crs].add(pre)
        
        def dfs(visited, crs):
            if crs in visited:
                return False

            visited.add(crs)
            for p in prereq[crs]:
                if not dfs(visited, p):
                    return False
            visited.remove(crs)
            prereq[crs] = set()
            return True

        for course in range(numCourses):
            visited = set()
            if not dfs(visited, course):
                return False

        return True