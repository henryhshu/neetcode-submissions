"""
# Definition for a QuadTree node.
class Node:
    def __init__(self, val, isLeaf, topLeft, topRight, bottomLeft, bottomRight):
        self.val = val
        self.isLeaf = isLeaf
        self.topLeft = topLeft
        self.topRight = topRight
        self.bottomLeft = bottomLeft
        self.bottomRight = bottomRight
"""

class Solution:
    def construct(self, grid: List[List[int]]) -> 'Node':
        # use a recursive solution to build the quad tree
        # base case is size of one square
        root = Node()
        if len(grid) == 1:
            root.isLeaf = True
            root.val = bool(grid[0][0])
            return root
            
        # divide the tree into four parts and run construct on each
        sideLen = len(grid)
        mid = sideLen // 2
        topLeft = self.construct([row[:mid] for row in grid[:mid]])
        topRight = self.construct([row[mid:] for row in grid[:mid]])
        bottomLeft = self.construct([row[:mid] for row in grid[mid:]])
        bottomRight = self.construct([row[mid:] for row in grid[mid:]])

        # consider case where all the quad nodes are the same
        # if same, set current node to leaf node
        if (topLeft.isLeaf and topRight.isLeaf and bottomLeft.isLeaf and bottomRight.isLeaf and
            topLeft.val == topRight.val == bottomLeft.val == bottomRight.val
            ):
            root.isLeaf = True
            root.val = topLeft.val
        else:
            # set the quadrant children to each quad node
            root.topLeft = topLeft
            root.topRight = topRight
            root.bottomLeft = bottomLeft
            root.bottomRight = bottomRight
            root.isLeaf = False

        # return the root node
        return root

        