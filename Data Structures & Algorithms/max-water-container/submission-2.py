class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l, r = 0, len(heights) - 1
        maxWater = 0

        while l < r:
            if heights[l] < heights[r]:
                maxWater = max(maxWater, heights[l] * (r - l))
                l += 1
            else:
                maxWater = max(maxWater, heights[r] * (r - l))
                r -= 1

        return maxWater