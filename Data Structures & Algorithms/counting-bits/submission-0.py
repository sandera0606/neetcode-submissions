class Solution:
    def countBits(self, n: int) -> List[int]:
        res = [0] * (n+1)
        if n == 0:
            return res

        res[1] = 1

        cur = 1

        for i in range(2, n+1):
            if i == (cur << 1):
                res[i] = 1
                cur = cur << 1
                continue
            res[i] = res[cur] + res[i-cur]
        return res
            