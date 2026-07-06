class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        # 1 2 3 4, find 3 --> [1,2] since it is one-indexed
        # use O(1) extra space, probably want O(n) time
        l, r = 0, len(numbers) - 1
        while l < r:
            if numbers[l] + numbers[r] > target:
                r -= 1
            elif numbers[l] + numbers[r] < target:
                l += 1
            else:
                return [l+1, r+1]