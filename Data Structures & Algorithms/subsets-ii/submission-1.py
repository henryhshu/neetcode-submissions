class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        # backtracking algorithm
        # decision binary tree traversal in 2^n
        # either include or don't include
        nums.sort()
        res = set()
        def dfs(i, curr):
            if i >= len(nums):
                res.add(tuple(curr))
                return
            
            curr.append(nums[i])
            dfs(i+1, curr.copy())
            curr.pop()
            dfs(i+1, curr.copy())
        
        dfs(0, [])
        return list(res)