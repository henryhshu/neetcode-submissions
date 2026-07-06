# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# dfs: "1 2 # # 3 4 # # 5 # #"
# keep track of a variable that tells what position we are at in the encoded string
# O(n) to serialize, and O(n) to deserialize

class Codec:
    
    # Encodes a tree to a single string.
    def serialize(self, root: Optional[TreeNode]) -> str:
        res = ""
        def dfs(root):
            nonlocal res
            if not root:
                res += "#"
                return
            res += str(root.val) + "."
            dfs(root.left)
            dfs(root.right)
            return
        dfs(root)
        return res

        
    # Decodes your encoded data to tree.
    def deserialize(self, data: str) -> Optional[TreeNode]:
        # keep track of where we are at in the decoding string
        print(data)
        i = 0
        def dfs_decode():
            nonlocal i
            if data[i] == "#":
                i += 1
                return None
            num_string = ""
            while data[i] != ".":
                num_string += data[i]
                i += 1
            cur = TreeNode(int(num_string))
            i += 1
            cur.left = dfs_decode()
            cur.right = dfs_decode()

            return cur

        return dfs_decode()