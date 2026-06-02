class Solution:
    def climbStairs(self, n: int) -> int:
        if n <= 2:
            return n
        one, two = 1, 1
        while n > 0:
            n -= 1
            temp = one
            one = one + two
            two = temp
        return two