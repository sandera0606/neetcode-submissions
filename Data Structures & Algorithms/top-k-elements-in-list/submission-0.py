class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        frequency = {}

        for i in range(len(nums)):
            cur = nums[i]
            if cur in frequency:
                frequency[cur] += 1
            else:
                frequency[cur] = 1
        
        sortedFrequency = []

        for key in frequency:
            value = frequency[key]
            i = 0
            while i < len(sortedFrequency):
                compareValue = frequency[sortedFrequency[i]]
                if compareValue > value:
                    sortedFrequency.insert(i, key)
                    break
                i += 1
            
            if i == len(sortedFrequency):
                sortedFrequency.append(key)
        
        return sortedFrequency[len(sortedFrequency) - k:]