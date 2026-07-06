class Solution:
    def maxArea(self, heights: List[int]) -> int:
        # use a sliding window approach
        # always move the smaller height since that one is the limiter
        # we will eventually find the largest possible container of water
        res = 0
        l, r = 0, len(heights)-1
        while l < r:
            water = min(heights[l], heights[r]) * (r-l)
            res = max(res, water)
            if heights[l] > heights[r]:
                r -= 1
            else:
                l += 1
        return res