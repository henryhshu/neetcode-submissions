# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        # find the two nodes
        # can just compare value since all node values are unique
        # record the matching path between the two nodes until they dont match
        p_path = [root]
        q_path = [root]
        cur = root
        while cur.val != p.val:
            if p.val > cur.val:
                cur = cur.right
            else:
                cur = cur.left
            p_path.append(cur)

        cur = root
        while cur.val != q.val:
            if q.val > cur.val:
                cur = cur.right
            else:
                cur = cur.left
            q_path.append(cur)

        shorter = min(len(p_path), len(q_path))
        for i in range(shorter):
            if i == shorter - 1 and p_path[i].val == q_path[i].val:
                return p_path[i]
            if p_path[i].val != q_path[i].val:
                return p_path[i-1]