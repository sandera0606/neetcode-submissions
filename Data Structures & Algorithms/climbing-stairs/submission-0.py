class Solution:
    def climbStairs(self, n: int) -> int:
        checked = {}

        def climbStairsRecurs(count):
            if count in checked:
                return checked[count]
            elif count >= n:
                return count == n
            else:
                checked[count] = climbStairsRecurs(count + 1) + climbStairsRecurs(count + 2)
                return checked[count]

        return climbStairsRecurs(0)