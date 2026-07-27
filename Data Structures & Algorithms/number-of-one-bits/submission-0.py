class Solution:
    def hammingWeight(self, n: int) -> int:
        # 32 bit
        count = 0
        cur = 1

        for i in range(0, 32):
            count += 1 if cur & n == cur else 0
            cur *= 2
        
        return count