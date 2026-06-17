class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = [set() for i in range(9)]
        cols = [set() for i in range(9)]
        three = [[set() for i in range(3)] for j in range(3)]

        for row in range(9):
            for col in range(9):
                item = board[row][col]
                if item == ".": continue
                if item in rows[row] or item in cols[col] or item in three[row//3][col//3]:
                    return False
                rows[row].add(item)
                cols[col].add(item)
                three[row//3][col//3].add(item)
        return True