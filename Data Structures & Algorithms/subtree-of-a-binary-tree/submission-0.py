# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        # as soon as we find a subtree thats true we can return true
        # explore through the left and right side until we find subroot
        # bfs to explore all the nodes then dfs to match subtrees
        def subtreeMatch(r, sub):
            if not r and not sub:
                return True
            if not r or not sub or r.val != sub.val:
                return False
            return subtreeMatch(r.left, sub.left) and subtreeMatch(r.right, sub.right)

        q = deque()
        q.append(root)
        while q:
            for _ in range(len(q)):
                cur = q.popleft()
                if subtreeMatch(cur, subRoot):
                    return True
                if cur:
                    q.append(cur.left)
                    q.append(cur.right)
        return False