class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        """
        initialize pointers at the start of both of the strings
        use a recursive dfs to find all the branching conditions when we hit a *
        then finally optimize the brute force by using a top down memo
        we just try to find one branching condition that is true
        """
        # store every time we have seen (i, j)
        cache = {}

        # write the dfs function
        def dfs(i, j):
            # check base case that both i and j are out of bounds return true
            if i >= len(s) and j >= len(p):
                return True
            # if only j is out of bounds, then return false
            if j >= len(p):
                return False
            
            # check if the current index matches
            match = i < len(s) and (s[i] == p[j] or p[j] == ".")
            # check branching conditions when encountering *
            if j < (len(p) - 1) and p[j+1] == "*":
                # branch either dont match (skip *) or match (keep *)
                cache[(i,j)] = dfs(i, j+2) or (match and dfs(i+1, j))
                return cache[(i,j)]
            # check if curr indices are matching
            if match:
                cache[(i,j)] = dfs(i+1, j+1)
                return cache[(i,j)]
            # nothing we tried matches, these indices are bad
            cache[(i,j)] = False
            return False
        return dfs(0,0)

        
        
