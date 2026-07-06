class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        # basic binary search
        l,r = 0, len(nums)-1
        while l<r:
            m = (l+r)//2
            if nums[m] > target:
                r = m-1
            elif nums[m] < target:
                l = m+1
            else:
                return m
        # 1 3 5 6
        # l m   r
        return l+1 if target > nums[l] else l