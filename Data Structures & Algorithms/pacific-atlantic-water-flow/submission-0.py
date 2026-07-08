class Solution:

    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        pacific = set()
        atlantic = set()
        self.heights = heights
        self.setPacific(pacific)
        self.setAtlantic(atlantic)
        return list(pacific & atlantic)
    
    def setPacific(self, pacific):
        for c in range(len(self.heights[0])):   # top row
            self.dfs(pacific, -1, 0, c)
        for r in range(len(self.heights)):      # left col
            self.dfs(pacific, -1, r, 0)

    def setAtlantic(self, atlantic):
        r = len(self.heights) - 1
        for c in range(len(self.heights[0])):   # bottom row
            self.dfs(atlantic, -1, r, c)
        c = len(self.heights[0]) - 1
        for r in range(len(self.heights)):      # right col
            self.dfs(atlantic, -1, r, c)
    
    def dfs(self, hashset, prev, r, c):
        if r < 0 or r >= len(self.heights) or c < 0 or c >= len(self.heights[0]):
            return
        if self.heights[r][c] < prev:
            return
        if (r, c) in hashset:
            return
        hashset.add(tuple([r, c]))
        self.dfs(hashset, self.heights[r][c], r + 1, c)
        self.dfs(hashset, self.heights[r][c], r - 1, c)
        self.dfs(hashset, self.heights[r][c], r, c + 1)
        self.dfs(hashset, self.heights[r][c], r, c - 1)
