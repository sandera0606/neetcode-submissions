class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        pre = defaultdict(set)

        for a, b in prerequisites:
            pre[a].add(b)

        def dfs(path, course):
            if course in path:
                return False
            path.add(course)
            for p in pre[course]:
                if not dfs(path, p):
                    return False
            path.remove(course)
            pre[course] = set()
            return True
        
        for course in range(numCourses):
            path = set()
            if not dfs(path, course):
                return False
        return True