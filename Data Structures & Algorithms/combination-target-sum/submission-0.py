class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        # same as the change question
        combos = [[] for _ in range(target + 1)]
        combos[0] = [[]]

        for num in nums:
            for i in range(num, target + 1):
                old = combos[i-num]
                for lst in old:
                    newLst = lst.copy() + [num]
                    combos[i].append(newLst)

        return combos[-1]