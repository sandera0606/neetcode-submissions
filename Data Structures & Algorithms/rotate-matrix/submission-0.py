class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        n = len(matrix) - 1
        if n % 2 == 0:
            rMax = n / 2 - 1
        else:
            rMax = n // 2
        
        for r in range(n+1):
            for c in range(r, n-r):
                temp = matrix[c][n-r]
                matrix[c][n-r] = matrix[r][c]
                matrix[r][c] = matrix[n-c][r]
                matrix[n-c][r] = matrix[n-r][n-c]
                matrix[n-r][n-c] = temp 