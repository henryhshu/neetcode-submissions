class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        numsHash = {}
        for i in range(len(nums)):
            numsHash[nums[i]] = i
        for i in range(len(nums)):
            diff = target - nums[i]
            if diff in numsHash and numsHash[diff] != i:
                return [i, numsHash[diff]]