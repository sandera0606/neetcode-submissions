class Solution:
    def numDecodings(self, s: str) -> int:
        dp = [0] * len(s)

        if s[0] == "0":
            return 0
        dp[0] = 1

        for i in range(1, len(s)):
            # not decodeable 
            # s[i] == "0" and s[i-1] != "1" or "2"
            if s[i] == "0" and (s[i-1] != "1" and s[i-1] != "2"):
                return 0
            
            # decodeable only as a single digit
            # s[i] != "0"
            # int(s[i-1:i+1]) > 26
            elif (s[i] != "0" and int(s[i-1:i+1]) > 26) or s[i-1] == "0":
                dp[i] = dp[i-1]

            # decodeable only as a double digit
            # s[i] == "0" and s[i-1] == "1" or "2" (only need to check that s[i] == "0")
            elif s[i] == "0":
                if i-2>=0:
                    dp[i] = dp[i-2]
                else:
                    dp[i] = 1
            # decodeable as a single digit or a double digit
            # else:
            else:
                if i-2 >= 0:
                    dp[i] = dp[i-2] + dp[i-1]
                else:
                    dp[i] = 1 + dp[i-1]

        return dp[-1]