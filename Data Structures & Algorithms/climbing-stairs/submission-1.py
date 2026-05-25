class Solution:
    def climbStairs(self, n: int) -> int:
        # [1, 1, 2, 3, ]
        # nth fibonacci
        one = 1
        two = 1

        for i in range(1, n):
            temp = two
            two = one + two
            one = temp
        
        return two