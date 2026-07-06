class Solution:
    def foreignDictionary(self, words: List[str]) -> str:
        # using topological sort (post-order dfs)
        # build the adjacency list
        adj = { char: set() for word in words for char in word }

        # iterate through all the pairs in the sorted dictionary
        for i in range(len(words)-1):
            w1, w2 = words[i], words[i+1]

            # check if the sorting is valid
            minLen = min(len(w1), len(w2))
            if len(w1) > len(w2) and w1[:minLen] == w2:
                return ""
            
            # we know sorting is valid, so we add sort to adj list
            for j in range(minLen):
                if w1[j] != w2[j]:
                    adj[w1[j]].add(w2[j])
                    break

        # keep track of whether or not each node is visited and if they are in the current path
        visit = {} # true is in current path, false is visited
        # keep track of the result variable that we will later reverse and join
        res = []
        # create the dfs function
        def dfs(char):
            # base case: if we've already seen this character return whether or not current character is in current path
            if char in visit:
                return visit[char]
            # go through each of it's neighbors and run dfs
            # visit the current node and mark it as in current path
            visit[char] = True
            for neighbor in adj[char]:
                if dfs(neighbor): # if loop detected
                    return True
            # unmark current character in current path
            visit[char] = False
            res.append(char)
            return False
        
        for char in adj:
            if dfs(char):
                return ""
        res.reverse()
        return "".join(res)
        