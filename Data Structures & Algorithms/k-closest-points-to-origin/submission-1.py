import math
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        heap = []
        for p in points:
            heap.append((p[0]**2 + p[1]**2, p[0], p[1]))
        heapq.heapify(heap)
        res = []
        for i in range(k):
            dist, x, y = heapq.heappop(heap)
            res.append([x, y])

        return res
