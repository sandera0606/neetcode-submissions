class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freqs = [[] for i in range(len(nums))]

        counts = defaultdict(int)

        for num in nums:
            counts[num] += 1
        
        for key, value in counts.items():
            freqs[value - 1].append(key)

        ans = []
        cur = len(freqs) - 1
        while len(ans) < k:
            ans.extend(freqs[cur])
            cur -= 1
        return ans