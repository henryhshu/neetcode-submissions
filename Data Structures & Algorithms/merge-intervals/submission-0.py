class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        # sort the intervals
        # keep track of a start and an end
        # what are the cases that we want to merge the intervals?
        # merge when the start of the next interval is before the end of the previous interval
        # take the end of the longer interval
        # keep track of a result array to append merged intervals to
        # [1,3] [1,5]
        intervals.sort()
        res = []
        start = intervals[0][0]
        prevEnd = intervals[0][1]
        for i in intervals[1:]:
            if i[0] <= prevEnd:
                prevEnd = max(i[1], prevEnd)
            else:
                res.append([start, prevEnd])
                start = i[0]
                prevEnd = i[1]
        res.append([start, prevEnd])

        return res