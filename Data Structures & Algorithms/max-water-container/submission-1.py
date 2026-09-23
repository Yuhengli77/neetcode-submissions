class Solution:
    def maxArea(self, heights: List[int]) -> int:

        ans = 0
        n = len(heights)
        l = 0
        r = n - 1

        while l < r:
            amount = min(heights[l], heights[r]) * (r - l)
            if amount > ans:
                ans = amount

            if heights[l] < heights[r]:
                l += 1
            else:
                r -= 1

        return ans



