class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # check if there is a loop in the course using a visit set
        # but not one that we have already completed, so need separate currently_visited
        # we create a graph of courses that we must take in a particular order

        # construct adj list and visit set
        adj = {i:[] for i in range(numCourses)}
        for course, pre in prerequisites:
            adj[course].append(pre)

        # implment dfs function
        visiting = set()
        def dfs(course):
            # base cases
            if course in visiting:
                return False # loop encountered
            if adj[course] == []:
                return True # can complete course

            visiting.add(course)
            for i in adj[course]:
                if not dfs(i):
                    return False
            visiting.remove(course)
            # clear prereqs
            adj[course] = []
            return True
        
        # iterate through all the courses and do dfs
        for i in range(numCourses):
            if not dfs(i):
                return False
        return True
            

