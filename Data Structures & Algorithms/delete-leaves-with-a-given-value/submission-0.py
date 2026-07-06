# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def removeLeafNodes(self, root: Optional[TreeNode], target: int) -> Optional[TreeNode]:
        # binary tree so must traverse to leaf nodes, use post-order traversal
        # recursive solution is much simpler
        if not root:
            return None
        # recursively run check leaf node
        root.left = self.removeLeafNodes(root.left, target)
        root.right = self.removeLeafNodes(root.right, target)
        # check if current node is leaf node in an in-order manner
        if root.val == target and not root.left and not root.right:
            return None # effectively deleting the node
        return root