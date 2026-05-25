class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        matching = 0
        count1 = [0] * 26
        count2 = [0] * 26

        length = len(s1)

        if length > len(s2): return False

        for i in range(0, length):
            count1[ord(s1[i]) - ord('a')] += 1
            count2[ord(s2[i]) - ord('a')] += 1
        
        for i in range(0, 26):
            if(count1[i] == count2[i]): matching += 1
        
        l = 0
        for r in range(length, len(s2)):
            if matching == 26: return True
            newLetter = ord(s2[r]) - ord('a')
            count2[newLetter] += 1
            
            if count2[newLetter] == count1[newLetter]:
                matching += 1
            elif count1[newLetter] + 1 == count2[newLetter]:
                matching -= 1

            oldLetter = ord(s2[l]) - ord('a')
            count2[oldLetter] -= 1
            if count2[oldLetter] == count1[oldLetter]:
                matching += 1
            elif count1[oldLetter] - 1 == count2[oldLetter]:
                matching -= 1
            l += 1
            
        return matching == 26