from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # 1. convert string to array - alpha
            # O(n)
        # 2. put (len, (alpha, index)) as KVP in a dictionary dict(int, dict(arr, int))
            # O(m)
        # 3. store in array if alpha in  .. otherwise emplace back [str] and add to dict
        ans = [] # array to store answer
        master = defaultdict(dict) # dict(len, dict(freqs, index))
        index = -1

        for string in strs:
            length = len(string)
            alpha = [0] * 26
            # convert string into array of character frequencies
            for char in string:
                alpha[ord(char) - ord('a')] += 1
            tupled = tuple(alpha)
            if length in master.keys():
                if tupled in master[length].keys():
                    ans[master[length][tupled]].append(string)
                else:
                    ans.append([string])
                    master[length][tupled] = index + 1
                    index += 1
            else:
                ans.append([string])
                master[length][tupled] = index + 1
                index += 1
        
        return ans