class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # adjacency list graph, build the graph then try to find a cycle
        preMap = {i:[] for i in range(numCourses)}
        for pre in prerequisites:
            preMap[pre[0]].append(pre[1])
        visited = set()
        def dfs(cur):
            if cur in visited:
                return False
            if preMap[cur] == []:
                return True
            visited.add(cur)
            for i in preMap[cur]:
                if not dfs(i):
                    return False
            visited.remove(cur)
            preMap[cur] = []
            return True

        for course in range(numCourses):
            if not dfs(course):
                return False
        return True
