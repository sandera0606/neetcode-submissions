class Solution:
    def reverseBits(self, n: int) -> int:
        res = 0

        for i in range(32):
            bit = n%2
            res *= 2
            if bit == 1:
                res += 1
            n //= 2
        
        return res