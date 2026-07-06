class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        # majority counting algorithm
        # optimized O(1) space and O(n) time
        curMaj = nums[0]
        curCount = 1
        # iterate over every element
        for i in range(len(nums)):
            if nums[i] != curMaj:
                curCount -= 1
                if curCount < 0:
                    curMaj = nums[i]
                    curCount = 1
            else:
                curCount += 1
        return curMaj