class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        # input is list of numbers, the output is the length of the longest increasing subseq
        # use DFS with caching
        # work backwards with O(n^2) dynamic programming solution
        dp = [1] * len(nums)
        for i in range(len(nums)-1, -1, -1):
            for j in range(i+1, len(nums)):
                if nums[i] < nums[j]:
                    dp[i] = max(dp[i], dp[j] + 1)
        return max(dp)

