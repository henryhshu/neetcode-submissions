# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        # simple bfs
        if not root:
            return []
        res = []
        q = deque([root])
        while q:
            curList = []
            for _ in range(len(q)):
                cur = q.popleft()
                curList.append(cur.val)
                if cur.left: q.append(cur.left)
                if cur.right: q.append(cur.right)
            res.append(curList)
        return res