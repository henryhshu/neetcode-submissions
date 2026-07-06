# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        # use recursion to find the node to delete, always simplifying down
        # base case
        if not root:
            return None
        # traverse the tree to find the key node
        if root.val > key:
            root.left = self.deleteNode(root.left, key)
        elif root.val < key:
            root.right = self.deleteNode(root.right, key)
        else:
            # key has been found
            # if there are no children
            if not root.right and not root.left:
                return None
            # if there is one child
            if not root.right and root.left:
                return root.left
            if not root.left and root.right:
                return root.right
            # if there are two children
            # find the smallest in the right subtree
            curr = root.right
            while curr.left:
                curr = curr.left
            # set deleted node's value to curr's
            root.val = curr.val
            # delete the curr value
            root.right = self.deleteNode(root.right, curr.val)
        return root
            