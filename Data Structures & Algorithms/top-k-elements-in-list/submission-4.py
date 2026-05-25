class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # array of length n - space bounded above by O(n)
            # index = frequency
            # value = number
        # dict (num, freq) - space bounded above by O(n)
        # 3 passes: 
        #   1. put things into dict O(n)
        #   2. put things from dict into array O(n)
        #   3. read k frequent from array O(n)

        freqArray = [[] for i in range(len(nums))]
        freqDict = defaultdict(int)

        # 1. make frequency dictionary
        for num in nums:
            freqDict[num] += 1

        # 2. put things from freqDict into freqArray
        #   ans guaranteed to be unique so we don't care about overwriting
        for key, value in freqDict.items():
            freqArray[value - 1].append(key)

        ans = []
        numRead = 0
        # 3. read k frequent from array
        for i in range(len(nums) - 1, -1, -1):
            if freqArray[i] != []:
                ans.extend(freqArray[i])
                numRead += len(freqArray[i])
            if numRead == k:
                return ans
        return ans

