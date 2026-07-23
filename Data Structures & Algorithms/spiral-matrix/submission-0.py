class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        cur = [0, 0]
        c = [-1, len(matrix[0]) - 1]
        r = [0, len(matrix) - 1]

        dir = 0
        res = []
        # 0 right, 1 down, 2 left, 3 up
        while True:
            res.append(matrix[cur[0]][cur[1]])
            if dir == 0:
                if cur[1] == c[1]:
                    dir = 1
                    cur[0] += 1
                    c[0] += 1
                    if not(r[0] <= cur[0] <= r[1]):
                        return res
                else:
                    cur[1] += 1
                    
            elif dir == 1:
                if cur[0] == r[1]:
                    dir = 2
                    cur[1] -= 1
                    r[0] += 1
                    if not(c[0] <= cur[1] <= c[1]):
                        return res
                else:
                    cur[0] += 1

            elif dir == 2:
                if cur[1] == c[0]:
                    dir = 3
                    cur[0] -= 1
                    r[1] -= 1
                    if not(r[0] <= cur[0] <= r[1]):
                        return res
                else:
                    cur[1] -= 1 # left

            elif dir == 3:
                if cur[0] == r[0]:
                    dir = 0
                    cur[1] += 1
                    c[1] -= 1
                    if not(c[0] <= cur[1] <= c[1]):
                        return res
                else:
                    cur[0] -= 1 # up
    

            