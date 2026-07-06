class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        # bottom up dp: cache the result of n previous amounts
        dp = [float("inf")] * (amount+1)
        # base case: it takes zero coins to make zero dollars
        dp[0] = 0
        # iterate through every amount
        for target in range(1, amount+1):
            # iterate through every coin to see if cache applies
            for coin in coins:
                diff = target - coin
                if diff < 0:
                    continue
                dp[target] = min(dp[target], dp[diff] + 1) # recurrence relation
        return dp[amount] if dp[amount] != float("inf") else -1