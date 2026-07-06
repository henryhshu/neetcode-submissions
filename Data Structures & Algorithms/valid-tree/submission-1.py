class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        # edge cases
        # O(n) time and O(n) space
        if n == 0:
            return True

        adj = {i:[] for i in range(n)}
        if not n:
            return True
        for e in edges:
            adj[e[0]].append(e[1])
            adj[e[1]].append(e[0])
        
        visit = set()
        def dfs(node, parent):
            if node in visit:
                return False
            visit.add(node)
            for i in adj[node]:
                if i == parent:
                    continue
                if not dfs(i, node):
                    return False
            return True
            
        if not dfs(0, -1):
            return False

        return n == len(visit)