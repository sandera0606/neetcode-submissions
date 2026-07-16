class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        def reachable(mySet, prevHeight, r, c):
            if (r, c) in mySet or r < 0 or r >= len(heights) or c < 0 or c >= len(heights[0]):
                return
            if heights[r][c] < prevHeight:
                return
            mySet.add((r, c))
            reachable(mySet, heights[r][c], r+1, c)
            reachable(mySet, heights[r][c], r-1, c)
            reachable(mySet, heights[r][c], r, c+1)
            reachable(mySet, heights[r][c], r, c-1)
        
        # pacific ocean
        pacific = set()
        for r in range(len(heights)):
            reachable(pacific, -1, r, 0)
        for c in range(len(heights[0])):
            reachable(pacific, -1, 0, c)

        # atlantic ocean
        atlantic = set()
        for r in range(len(heights)):
            reachable(atlantic, -1, r, len(heights[0]) -1)
        for c in range(len(heights[0])):
            reachable(atlantic, -1, len(heights) -1, c)


        return list(pacific & atlantic)
