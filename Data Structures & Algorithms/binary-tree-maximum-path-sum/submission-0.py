# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        # splitting at a node means you cant access the parents
        # brute force will be to try every single node as the topmost then find max left and right
        # keep track to prevent repeated work
        # solve subproblem with dfs to get linear time solution
        # compute two values at every node: split or no split

        res = root.val # 2

        def dfs(root):
            # base case is if the root is None
            if not root:
                return 0
            
            # find the left max and right max to find the greatest value with split
            left_max = max(0, dfs(root.left)) # 2
            right_max = max(0, dfs(root.right)) # 3
            
            # update the res
            nonlocal res
            res = max(res, root.val + left_max + right_max)
            
            # return the value with no split
            return max(root.val + left_max, root.val + right_max)
        
        dfs(root)
        return res


