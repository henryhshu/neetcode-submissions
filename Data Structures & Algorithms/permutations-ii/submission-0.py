class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        # searching for permutations, not subsets
        # order matters, each perm must contain every element
        # use visited set to avoid duplicate counting
        # recursive backtracking to solve subproblems
        # mark elements as used by replacing them with a sentinel value
        visited = set()

        def dfs(cur):
            # base case: if length is same as nums add to set
            if len(cur) == len(nums):
                visited.add(tuple(cur))
                return
            # recurse deeper for every unseen number
            for i in range(len(nums)):
                if nums[i] != "x":
                    cur.append(nums[i])
                    temp = nums[i]
                    nums[i] = "x"
                    dfs(cur)
                    nums[i] = temp # restore the original value
                    cur.pop() # remove the added element from the current perm

        dfs([])
        return list(visited)