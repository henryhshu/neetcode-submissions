class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # use sliding window approach
        # start from the ends and move the one that moves inside
        # track the lowest to the left of each point and the highest to the right of each point
        # 7 1 1 1 1 1
        # 7 6  6  6 6 6  6 4
        low = [0] * len(prices)
        high = [0] * len(prices)
        low[0], high[-1] = prices[0], prices[len(prices)-1]
        for i in range(1, len(prices)):
            low[i] = min(low[i-1], prices[i])
        for i in range(len(prices)-2, -1, -1):
            high[i] = max(high[i+1], prices[i])
        res = 0
        # print(low, high)
        for i in range(len(prices)):
            res = max(high[i] - low[i], res)
        return res
