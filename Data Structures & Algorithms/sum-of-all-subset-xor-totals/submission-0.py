class Solution:
    def subsetXORSum(self, nums: List[int]) -> int:
        # need to find every subset of nums
        # we can keep track of an xor along the way
        xors = [] # list of xors for every subset
        # find every subset using dfs backtracking, choose either include or not include
        def dfs(i, prev):
            # base case
            if i == len(nums):
                return
            curr = prev ^ nums[i]
            dfs(i+1, prev) # skip current element
            dfs(i+1, curr) # include current element
            xors.append(curr)
        
        dfs(0, 0)
        # return sum of xors
        return sum(xors)