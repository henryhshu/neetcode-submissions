class MedianFinder:

    # use both a maxheap and a minheap to get the largest and the smallest
    # to get the median in O(1) time
    # if one heap is bigger, pull from that heap
    # maintain all values in the minheap is larger than that in the maxheap
    # multiply by -1 to build maxheap
    # get the first element of the list in order to find the max or min of the heap

    def __init__(self):
        self.small, self.large = [], []

    def addNum(self, num: int) -> None:
        heapq.heappush(self.small, -1 * num)

        # check if heaps are consistent
        if (self.small and self.large and self.small[0]*-1 > self.large[0]):
            value = -1*heapq.heappop(self.small)
            heapq.heappush(self.large, value)
        # check if heaps are balanced
        if len(self.small) > len(self.large)+1:
            value = -1*heapq.heappop(self.small)
            heapq.heappush(self.large, value)
        if len(self.large)> len(self.small)+1:
            value = heapq.heappop(self.large)
            heapq.heappush(self.small, -1*value)

    def findMedian(self) -> float:
        if len(self.small) > len(self.large):
            return -1*self.small[0]
        if len(self.large) > len(self.small):
            return self.large[0]
        return (self.large[0] + -1*self.small[0]) / 2
        