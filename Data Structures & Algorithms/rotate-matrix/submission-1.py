class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        dim = len(matrix)
        n = dim // 2
        m = n if dim % 2 == 0 else n + 1
        dim -= 1

        for r in range(m):
            for c in range(n):
                # tl = matrix[r][c]
                # tr = matrix[c][dim-r]
                # br = matrix[dim-r][dim-c]
                # bl = matrix[dim-c][r]
                temp = matrix[r][c]
                matrix[r][c] = matrix[dim-c][r]
                matrix[dim-c][r] = matrix[dim-r][dim-c]
                matrix[dim-r][dim-c] = matrix[c][dim-r]
                matrix[c][dim-r] = temp
        
