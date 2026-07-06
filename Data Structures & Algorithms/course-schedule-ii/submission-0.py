class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        # create adj list and toposort list
        toposort = []
        visited = set()
        adj = {i:[] for i in range(numCourses)}
        for course, pre in prerequisites:
            adj[course].append(pre)

        # create dfs function and visiting set
        visiting = set()
        def dfs(course):
            # base cases
            if course in visiting:
                return False
            if course in visited:
                return True
            
            visiting.add(course)
            for i in adj[course]:
                if not dfs(i):
                    return False # cycle detected
            # cleared to put course in toposort
            visiting.remove(course)
            visited.add(course)
            toposort.append(course)
            return True

        # run dfs for every course
        for i in range(numCourses):
            if not dfs(i):
                return []
        return toposort