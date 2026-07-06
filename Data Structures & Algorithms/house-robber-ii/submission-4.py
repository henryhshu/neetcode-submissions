class Solution:
    def rob(self, nums: List[int]) -> int:
        def helper(n):
            rob1, rob2 = n[0], max(n[0], n[1])
            for i in range(2,len(n)):
                temp = rob1 + n[i]
                rob1 = rob2
                rob2 = max(temp, rob2)
            return rob2
        if len(nums) < 3:
            return max(nums)
        return max(helper(nums[1:]), helper(nums[:-1]))