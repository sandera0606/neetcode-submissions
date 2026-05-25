class Solution:
    def climbStairs(self, n: int) -> int:
        if n == 1:
            return 1
        if n == 2:
            return 2
        numWays = [0] * (n)
        numWays[0] = 1
        numWays[1] = 2
        start = 0

        for i in range(2, n):
            numWays[i] = numWays[i-1] + numWays[i-2]
        
        print(numWays)
        
        return numWays[n-1]