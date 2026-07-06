import random
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        """
        store the numbers in a set so that we can access them
        find the maximum length of consecutive elements that can be formed
        """
        if not nums:
            return 0
        numSet = set(nums)
        res = 1
        # look for the start of the sequence
        for num in numSet:
            if num-1 not in numSet:
                tmp, cur = num, 1
                while tmp+1 in numSet:
                    cur += 1
                    tmp += 1
                res = max(res, cur)
        return res
