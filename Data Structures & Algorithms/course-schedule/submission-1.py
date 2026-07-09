class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        preMap = {i: [] for i in range(numCourses)}
        # course i has prerequisites in []

        for i, prereq in prerequisites:
            preMap[i].append(prereq)
            # build prerequisites map
        
        # detect cycles
        def dfs(preMap, visited, node):
            if node in visited:
                return False
            if preMap[node] == []:
                return True
            
            visited.add(node)
            for prereq in preMap[node]:
                if not dfs(preMap, visited, prereq):
                    return False
            visited.remove(node)
            preMap[node] = []
            return True
        
        for i in range(numCourses):
            visited = set()
            if not dfs(preMap, visited, i):
                return False
        return True