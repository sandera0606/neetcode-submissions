class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        count = 0
        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c] == "1":
                    count += 1
                    self.consumeIsland(grid, r, c)
        return count
    def consumeIsland(self, grid, r, c):
        if r < 0 or r >= len(grid) or c < 0 or c >= len(grid[0]):
            return
        if grid[r][c] == "1":
            grid[r][c] = "0"
        else:
            return
        self.consumeIsland(grid, r-1, c)
        self.consumeIsland(grid, r+1, c)
        self.consumeIsland(grid, r, c+1)
        self.consumeIsland(grid, r, c-1)