class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # 3 5 6 0 1 2
        # m r      r
        # m must either be before or after the pivot
        # if r > m and target < r and target > m then look in other half
        l, r = 0, len(nums)-1

        while l <= r:
            m = (l+r) // 2
            if nums[m] == target:
                return m
            # if right part is sorted
            if nums[r] >= nums[m]:
                if target > nums[r] or target < nums[m]:
                    r = m - 1
                else:
                    l = m + 1
            else:
                if target < nums[l] or target > nums[m]:
                    l = m + 1
                else:
                    r = m - 1
                    
            
        return -1
