class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        # brute force is O(n^2) by searching through all the numbers
        # using a set can reduce this to O(n) but also uses O(n) space
        # sum together all the numbers and subtract them
        res = 0
        for i in range(len(nums)+1):
            res += i
        for num in nums:
            res -= num
        return res