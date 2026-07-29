class Solution:
    def getSum(self, a: int, b: int) -> int:
        carry = 0
        res = 0

        for position in range(32):
            # get rightmost bit
            right_a = a % 2
            right_b = b % 2

            cur = right_a ^ right_b ^ carry
            cur = cur << position
            res = res | cur

            carry = (right_a & right_b) or (right_a & carry) or (right_b & carry)
            a = a >> 1
            b = b >> 1


        if res & (1 << 31):
            return ~(res ^ 0xFFFFFFFF)
        return res