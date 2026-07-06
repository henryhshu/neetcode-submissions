class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        l, r = 0, len(nums)-1
        while l <= r:
            m = (l+r) // 2
            # check neighbors
            if m > 0 and nums[m-1] > nums[m]:
                r = m - 1
            elif m < len(nums)-1 and nums[m+1] > nums[m]:
                l = m + 1
            else:
                # solution is found
                return m
