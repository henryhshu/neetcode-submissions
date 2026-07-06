class Solution:
    def trap(self, height: List[int]) -> int:
        # we can use linear time solution and no extra space
        # at every point keep track of the maximum to the left and right
        # if we just keep track of one left and one right, we shift the one that is smaller to guarantee that we can store water
        l, r = 0, len(height)-1
        if not height: return 0
        maxR, maxL = 0, 0
        res = 0
        while l < r:
            res += max(0, maxL - height[l])
            res += max(0, maxR - height[r])
            maxL = max(maxL, height[l])
            maxR = max(maxR, height[r])
            if height[l] <= height[r]:
                l += 1
            else:
                r -= 1
        return res