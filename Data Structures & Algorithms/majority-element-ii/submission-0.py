from collections import Counter

class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        # observations:
        #   maximum number of majority elements is 3
        #   brute force: use one pass counter
        n = len(nums) // 3
        counter = Counter(nums)
        res = []
        for key, value in counter.items():
            if value > n:
                res.append(key)
        return res