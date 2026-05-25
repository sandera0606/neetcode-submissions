class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counts = {}
        for num in nums:
            if num not in counts:
                counts[num] = 1
            else:
                counts[num] += 1

        sortedCounts = [[] for _ in range(len(nums))]

        for num, count in counts.items():
            sortedCounts[count - 1].append(num)
        
        result = []

        i = len(nums) - 1

        while k > 0:
            result.extend(sortedCounts[i])
            k -= len(sortedCounts[i])
            i -= 1

        return result