class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        if m > n:
            temp = n
            n = m
            m = temp
        bot = math.factorial(m-1)
        top = 1
        for i in range(n, m+n-1):
            top *= i

        return (int)(top / bot)