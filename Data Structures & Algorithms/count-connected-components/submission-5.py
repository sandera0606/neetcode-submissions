class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        res = n
        components = {x:[x] for x in range(n)}
        componentMap = {x:x for x in range(n)}

        for a, b in edges:
            # alr in same component
            if componentMap[a] == componentMap[b]:
                continue
            # otherwise, adjust data stuff
            res -= 1

            componentA = componentMap[a]
            componentB = componentMap[b]

            move = components.pop(componentB)
            components[componentA] += move
            componentMap[b] = componentA
            for node in move:
                componentMap[node] = componentA

        return res