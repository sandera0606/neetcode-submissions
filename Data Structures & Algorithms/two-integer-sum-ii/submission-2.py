class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        l = 0
        r = len(numbers) - 1
        while True:
            desired = target - numbers[l]
            if numbers[r] == desired:
                return [l + 1, r + 1]
            elif numbers[r] > desired:
                r -= 1
            else:
                l += 1