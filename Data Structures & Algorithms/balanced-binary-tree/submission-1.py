# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True
        
        b = True
        # find max depth
        def dfs(curr, depth):
            nonlocal b
            if not curr:
                return depth
            left_depth = dfs(curr.left, depth+1)
            right_depth = dfs(curr.right, depth+1)
            # print(left_depth, right_depth)
            if abs(left_depth - right_depth) > 1:
                b = False
            # print(b)
            return max(left_depth, right_depth)

        height = dfs(root, 0)
        return b