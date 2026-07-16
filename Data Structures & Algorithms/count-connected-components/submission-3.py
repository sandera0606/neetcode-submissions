class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        adj = defaultdict(set)

        components = {i:set([i]) for i in range(n)}
        compMap = {i:i for i in range(n)}
        count = len(components)
        for a, b in edges:
            if compMap[a] == compMap[b]:
                continue
            # else, merge the two components
            first = compMap[a]
            second = compMap[b]
            members = components[second]
            components[first] |= components[second]
            components.pop(second)

            for mem in members:
                compMap[mem] = first
            
        return len(components)