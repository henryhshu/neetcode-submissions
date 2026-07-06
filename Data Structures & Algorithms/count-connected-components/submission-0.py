class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        # use union find
        # initialize parent list and rank list
        par = [i for i in range(n)]
        rank = [1] * n

        def find(node):
            cur = node
            while cur != par[cur]:
                par[cur] = par[par[cur]] # path halving
                cur = par[cur]
            return cur
            
        def union(n1, n2):
            if n1 == n2:
                return 0
            if rank[n1] > rank[n2]:
                par[n2] = n1
                rank[n1] += 1
            else:
                par[n1] = n2
                rank[n2] += 1
            return 1

        res = n # start with n disconnected components
        for edge in edges:
            # find the parents of both edges
            n1, n2 = find(edge[0]), find(edge[1])
            res -= union(n1, n2) # if merge sucessful, subtract a component
 
        return res
