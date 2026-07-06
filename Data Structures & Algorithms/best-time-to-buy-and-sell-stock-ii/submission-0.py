class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # iterate through the array
        # only count positive diffs
        last_price = prices[0]
        res = 0
        for price in prices[1:]:
            if price > last_price:
                res += price - last_price
            last_price = price
        return res
            