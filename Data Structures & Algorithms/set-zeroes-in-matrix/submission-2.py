class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        topRow = 1
        for r in range(len(matrix)):
            for c in range(len(matrix[0])):
                if matrix[r][c] == 0:
                    matrix[0][c] = 0
                    if r == 0:
                        topRow = 0
                    else:
                        matrix[r][0] = 0
        
        def setRowZeros(r):
            for c in range(len(matrix[0])):
                matrix[r][c] = 0

        def setColZeros(c):
            for r in range(len(matrix)):
                matrix[r][c] = 0
        
        # 0 rows
        for r in range(1, len(matrix)):
            if matrix[r][0] == 0:
                setRowZeros(r)

        # 0 cols
        for c in range(0, len(matrix[0])):
            if matrix[0][c] == 0:
                setColZeros(c)

        if topRow == 0:
            setRowZeros(0)
        