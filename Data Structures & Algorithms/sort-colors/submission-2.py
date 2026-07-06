class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        we only have 3 colors: red white and blue
        """
        l, r = 0, len(nums)-1
        i = 0
        while i <= r:
            if nums[i] == 2:
                nums[r], nums[i] = 2, nums[r]
                r -= 1
            elif nums[i] == 0:
                nums[l], nums[i] = 0, nums[l]
                l += 1
                i += 1
            else:
                i += 1