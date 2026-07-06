# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        res = 0
        def dfs(node, curr):
            nonlocal res
            if not node:
                return
            tmp = curr
            if node.val >= curr:
                res += 1
                curr = node.val
            dfs(node.left, curr)
            dfs(node.right, curr)
            curr = tmp
        dfs(root, root.val)
        return res