class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        self.grid = grid
        count = 0
        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if self.grid[r][c] =="1":
                    count += 1
                    self.dfs(r, c)
        return count

    def dfs(self, r, c):
        if r < 0 or r >= len(self.grid) or c < 0 or c >= len(self.grid[0]):
            return
        if self.grid[r][c] != "1":
            return
        self.grid[r][c] = "0"
        self.dfs(r-1, c)
        self.dfs(r+1, c)
        self.dfs(r, c-1)
        self.dfs(r, c+1)