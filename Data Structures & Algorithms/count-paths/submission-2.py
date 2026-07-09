class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        if m > n:
            temp = n
            n = m
            m = temp

        res = 1

        for i in range(m, m+n-1):
            res *= i

        for i in range(1, n):
            res //= i
        
        return int(res)