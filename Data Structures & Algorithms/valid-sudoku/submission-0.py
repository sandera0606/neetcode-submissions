class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # A BUNCH OF SETS!!!!
        #   one for each row
        #   one for each column
        #   one for each 3x3 box
        # O(9 x 9 x 3) -> O(n x n)
        # row sets: stored in list of 9
        # column sets: stored in list of 9
        # 3x3 box sets: stored in 3x3 matrix [0: [0, 1, 2], 1: [0, 1, 2], 2: [0, 1, 2]]

        rowSets = [set() for row in range(9)]
        colSets = [set() for col in range(9)]
        thrSets = [[set() for col in range(3)] for row in range(3)]

        for row in range(9):
            for col in range(9):
                val = board[row][col]
                if(val) == ".":
                    continue # no value here, don't add to any set
                # add to rows set
                if val in rowSets[row]:
                    return False
                else:
                    rowSets[row].add(val)
                # add to column set
                if val in colSets[col]:
                    return False
                else:
                    colSets[col].add(val)
                
                # add to 3x3 set
                rowInd = row // 3
                colInd = col // 3
                if val in thrSets[rowInd][colInd]:
                    return False
                else:
                    thrSets[rowInd][colInd].add(val)

        return True