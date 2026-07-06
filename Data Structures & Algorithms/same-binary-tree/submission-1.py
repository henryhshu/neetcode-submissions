# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        plist = []
        qlist = []
        queue = deque()
        
        # populate plist
        if p:
            queue.append(p)
            plist.append(p.val)
        else:
            plist.append(None)
        while queue:
            for _ in range(len(queue)):
                cur = queue.popleft()
                if cur.left:
                    queue.append(cur.left)
                    plist.append(cur.left.val)
                else:
                    plist.append(None)
                if cur.right:
                    queue.append(cur.right)
                    plist.append(cur.right.val)
                else:
                    plist.append(None)
        
        # populate qlist
        if q:
            queue.append(q)
            qlist.append(q.val)
        else:
            qlist.append(None)
        while queue:
            for _ in range(len(queue)):
                cur = queue.popleft()
                if cur.left:
                    queue.append(cur.left)
                    qlist.append(cur.left.val)
                else:
                    qlist.append(None)
                if cur.right:
                    queue.append(cur.right)
                    qlist.append(cur.right.val)
                else:
                    qlist.append(None)
        
        return qlist == plist