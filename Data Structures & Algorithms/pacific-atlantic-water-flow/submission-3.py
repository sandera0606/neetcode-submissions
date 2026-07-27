class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        pacific = set()
        atlantic = set()


        def findReachable(mySet, prev, r, c):
            if (r, c) in mySet or r < 0 or c < 0 or r >= len(heights) or c >= len(heights[0]):
                return
            
            if prev > heights[r][c]:
                return
            mySet.add((r, c))
            findReachable(mySet, heights[r][c], r+1, c)
            findReachable(mySet, heights[r][c], r-1, c)
            findReachable(mySet, heights[r][c], r, c+1)
            findReachable(mySet, heights[r][c], r, c-1)

        # check reachable from pacific
        for c in range(len(heights[0])):
            findReachable(pacific, -1, 0, c)
        for r in range(len(heights)):
            findReachable(pacific, -1, r, 0)


        # check reachable from atlantic
        for c in range(len(heights[0])):
            findReachable(atlantic, -1, len(heights)-1, c)
        for r in range(len(heights)):
            findReachable(atlantic, -1, r, len(heights[0])-1)

        return list(pacific & atlantic)