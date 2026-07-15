class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        count = 0
        def conquer(r, c):
            if r < 0 or r >= len(grid) or c < 0 or c >= len(grid[0]):
                return
            
            if grid[r][c] == '1':
                grid[r][c] = '0'
            else:
                return
            
            conquer(r+1, c)
            conquer(r-1, c)
            conquer(r, c+1)
            conquer(r, c-1)
        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c] == '1':
                    count += 1
                    conquer(r, c)
        return count