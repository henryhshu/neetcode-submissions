class Solution:
    def numSquares(self, n: int) -> int:
        # greedy doesn't work, needs to find the minimal result
        # almost same problem as coin change
        # brute force approach is decision tree, but we can optimize using caching
        # store solutions to subproblems in dp array
        dp = [n] * (n+1) # store 0 to n inclsive
        dp[0] = 0

        # iterate through every number
        for target in range(1, n+1):
            # iterate through every square that fits
            for s in range(1, target + 1):
                square = s * s
                if square > target:
                    break # went over
                dp[target] = min(dp[target], dp[target - square] + 1)
        
        return dp[n]



