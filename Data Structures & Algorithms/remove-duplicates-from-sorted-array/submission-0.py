class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        res = 1
        cur = nums[0]
        i = 1
        while i < len(nums):
            if nums[i] == cur:
                del nums[i]
            else:
                cur = nums[i]
                res += 1
                i += 1
        return res
            
            
                