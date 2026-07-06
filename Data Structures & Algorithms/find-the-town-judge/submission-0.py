class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        # the town judge has n-1 incoming connections
        # the town judge has no outgoing connections
        # the town judge can be found using a single dfs starting from an arbitrary person
        # construct an ajacency list first
        # what if there are loops? can just delete the person after visting
        # when can the judge not be identified? when there is a loop
        # simply count number of incoming and number of outgoing edges and check their values
        incoming = defaultdict(int)
        outgoing = defaultdict(int)
        for s, d in trust:
            incoming[d] += 1
            outgoing[s] += 1
        for key, val in incoming.items():
            if val == n-1 and outgoing[key] == 0:
                return key
        return -1 

