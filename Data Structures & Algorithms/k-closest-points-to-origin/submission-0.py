import math
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        dists = []
        for i in range(len(points)):
            x = points[i][0]
            y = points[i][1]
            dists.append((math.sqrt(x**2 + y**2), i))

        res = [points[dist[1]] for dist in sorted(dists)[:k]]
        return res