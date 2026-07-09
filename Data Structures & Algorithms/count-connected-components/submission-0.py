class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        # 1. start with n components
        # 2. keep track of the nodes within each component
        # 3. when adding an edge, if they are from different components, merge those two components
        # 4. proceed until we are out of edges, then return the # of components.
        
        # each component is a list of nodes
        components = {i: [i] for i in range(n)}

        # map of n : which component it is from
        compMap = {i:i for i in range(n)}

        for one, two in edges:
            if compMap[one] == compMap[two]:
                continue
            # merge the two components
            # 1. get the two components
            first = compMap[one]
            second = compMap[two]

            # 2. merge components 'first' and 'second'
            members = components[second]
            components[first] = components[first] + components[second]
            components.pop(second)

            # 3. update map
            for mem in members:
                compMap[mem] = first



        return len(components)