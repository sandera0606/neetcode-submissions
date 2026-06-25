class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        counts = defaultdict(int)
        l = 0
        longest = 0
        mostFreq = 0
        for r in range(len(s)):
                counts[s[r]] += 1
                mostFreq = max(mostFreq, counts[s[r]])
                while r - l + 1 - mostFreq > k:
                        counts[s[l]] -= 1
                        l += 1
                length = r - l + 1
                longest = max(length, longest)
        return longest