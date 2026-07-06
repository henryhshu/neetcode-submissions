class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        To do this in O(1) extra space, we need to just keep track of one num while iterating through the nums
        1 2 3 4 5, k = 2 => 4 5 1 2 3
        4 
        """
        # iterate through all the numbers and shift them using copied array (extra mem)
        # use reversal for no extra mem
        n = len(nums)
        k = k % len(nums)

        def reverse(l, r) -> None:
            while l < r:
                nums[l], nums[r] = nums[r], nums[l]
                l += 1
                r -= 1
        
        reverse(0, n-1)
        reverse(0, k-1)
        reverse(k, n-1)


        