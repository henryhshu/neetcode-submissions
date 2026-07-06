class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        # binary search on the weight of the ship
        # need to find out whether the packages can be shipped within n days
        # upper bound is just the sum of the weights
        def feasible(cap):
            counter = 0 # count number of days
            i = 0
            while i < len(weights):
                curr = 0
                while i < len(weights):
                    curr += weights[i]
                    if curr > cap:
                        break
                    else:
                        i += 1 # add the weight
                counter += 1
            return counter <= days

        l, r = max(weights), sum(weights)
        res = r
        while l <= r:
            m = (l + r) // 2
            if feasible(m):
                r = m-1
                res = min(res, m)
            else:
                l = m+1
        return res