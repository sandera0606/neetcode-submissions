class Solution:
    def minWindow(self, s: str, t: str) -> str:
        need = defaultdict(int)

        if len(s) < len(t):
            return ""

        for char in t:
            need[char] += 1
        
        l = 0
        counts = defaultdict(int)
        have = 0
        num = len(need)

        shortest = ""
        shortestLen = len(s) + 1

        for r in range(len(s)):
            counts[s[r]] += 1
            if counts[s[r]] == need[s[r]] and need[s[r]] != 0:
                have += 1

            while l <= r and have >= num:
                # shortest = shortest substring
                if shortestLen > r - l + 1:
                    shortest = s[l:r+1]
                    shortestLen = r - l + 1
                # increment l until we gud
                if counts[s[l]] == need[s[l]]:
                    have -= 1
                counts[s[l]] -= 1
                l += 1
                print(l, r)
                
        return shortest