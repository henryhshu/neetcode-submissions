class Solution:
    def trap(self, height: List[int]) -> int:
        # we can use linear time solution and no extra space
        # at every point keep track of the maximum to the left and right
        # if we just keep track of one left and one right, we shift the one that is smaller to guarantee that we can store water
        l, r = 0, len(height)-1
        if not height: return 0
        maxL, maxR = height[l], height[r]
        res = 0
        while l < r-1:
            if maxL < maxR:
                l += 1
                maxL = max(maxL, height[l])
                res += maxL - height[l]
            else:
                r -= 1
                maxR = max(maxR, height[r])
                res += maxR - height[r]
        return res