class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # freq array: frequency is the key and 

        counts = defaultdict(int)
        for num in nums:
            counts[num] += 1
        freqs = [[] for i in range(len(nums))]
        for num, freq in counts.items():
            freqs[freq - 1].append(num)
        ans = []
        for i in range(len(nums) - 1, -1, -1):
            if len(ans) == k:
                return ans
            if freqs[i]:
                ans.extend(freqs[i])
        return ans
