class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = [set() for i in range(9)]
        cols = [set() for i in range(9)]
        three = [[set() for i in range(3)] for j in range(3)]

        for r in range(9):
            for c in range(9):
                val = board[r][c]
                if val == ".": continue
                if (val in rows[r]) or (val in cols[c]) or (val in three[r//3][c//3]):
                    return False
                rows[r].add(val)
                cols[c].add(val)
                three[r//3][c//3].add(val)

        return True
