class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        longestUnique = 0
        seen = {}
        curStreak = 0
        startPoint = 0

        for i, char in enumerate(s):
            if char not in seen or seen[char] < startPoint:
                curStreak += 1
            else:
                startPoint = seen[char] + 1
                curStreak = i + 1 - startPoint
            seen[char] = i
            if curStreak > longestUnique:
                longestUnique = curStreak

        return longestUnique