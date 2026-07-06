class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        for j in range(len(nums)):
            for offset in range(1, k+1):
                i = j + offset
                if i < len(nums) and nums[i] == nums[j]:
                    return True
        return False
            