class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        count = set()
        longest = 0
        start = 0;
        for i in range(0, len(s)):
            char = s[i]
            if char not in count:
                count.add(char)
            else:
                cur = s[start]
                while(cur != char):
                    count.remove(cur)
                    start += 1
                    cur = s[start]
                start += 1
            longest = max(longest, i - start + 1)
        
        return longest
        

        