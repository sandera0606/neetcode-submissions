class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        
        count1, count2 = [0] * 26, [0] * 26

        for i in range(len(s1)):
            count1[ord(s1[i]) - ord('a')] += 1

        l = 0
        len1 = len(s1)

        for r in range(len(s2)):
            count2[ord(s2[r]) - ord('a')] += 1

            if r - l + 1 < len1:
                continue
            
            if count2 == count1:
                return True
                
            count2[ord(s2[l]) - ord('a')] -= 1
            l += 1

        return False