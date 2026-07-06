class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        """
        we can choose either to include or not to include the current number in the sequence
        use a hashmap to map prefixsum to count that is incrementally built up
        """
        res = 0
        curSum = 0
        prefixSums = {0:1}
        for n in nums:
            curSum += n
            diff = curSum - k
            res += prefixSums.get(diff, 0)
            prefixSums[curSum] = prefixSums.get(curSum, 0) + 1
        return res
