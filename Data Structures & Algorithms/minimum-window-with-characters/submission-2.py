class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(s) < len(t):
            return ""

        tCounts = defaultdict(int)
        for char in t:
            tCounts[char] += 1
        
        has = 0
        need = len(tCounts.keys())

        sCounts = defaultdict(int)
        shortest = ""
        shortestLen = len(s) + 1
        l, r = 0, 0

        while r < len(t) - 1:
            sCounts[s[r]] += 1
            if sCounts[s[r]] == tCounts[s[r]]:
                has += 1
            r += 1

        while r < len(s):
            sCounts[s[r]] += 1
            
            if sCounts[s[r]] == tCounts[s[r]]:
                has += 1
                while has == need:
                    if shortestLen > r - l + 1:
                        shortest = s[l:r+1]
                        shortestLen = r - l + 1
                    sCounts[s[l]] -= 1
                    if sCounts[s[l]] < tCounts[s[l]]:
                        has -= 1
                    l += 1
                    
            r += 1
        
        return shortest