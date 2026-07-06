class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key = lambda i: i[0])
        res = []
        res.append(intervals[0])
        for interval in intervals[1:]:
            last_end = res[-1][1]
            curr_start = interval[0]
            curr_end = interval[1]
            if curr_start <= last_end:
                res[-1][1] = max(last_end, curr_end)
            else:
                res.append(interval)

        return res