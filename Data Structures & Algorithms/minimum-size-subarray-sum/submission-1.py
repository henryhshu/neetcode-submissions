class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        l, r = 0, 0
        current_sum = sum(nums)
        if current_sum < target:
            return 0
        current_sum = nums[0]
        window_size = float("inf")
        # loop while not traversed all nums
        while True:
            # increase window until larger than target
            while current_sum < target:
                r += 1
                if r == len(nums):
                    return window_size
                current_sum += nums[r]
            window_size = min(window_size, r-l+1)
            # try shrinking the window
            current_sum -= nums[l]
            l += 1

