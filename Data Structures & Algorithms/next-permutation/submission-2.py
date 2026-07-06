class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        if the array is fully descending, then we just return the reversed array
        find the point where the number is lower
        """
        breakpoint = -1
        for i in range(len(nums)-2, -1, -1):
            if nums[i+1] > nums[i]:
                breakpoint = i
                break

        # take care of edge case
        if breakpoint == -1:
            nums.reverse()
            return

        # replace the character and flip subarray
        for i in range(len(nums)-1, -1, -1):
            if nums[i] > nums[breakpoint]:
                nums[breakpoint], nums[i] = nums[i], nums[breakpoint]
                break
        nums[breakpoint+1:] = reversed(nums[breakpoint+1:])
        

        