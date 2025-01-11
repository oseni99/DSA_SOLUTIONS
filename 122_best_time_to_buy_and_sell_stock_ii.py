class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # JUST BEST PRICE TO BUY AND SELL STOCKS I WE PREVIOUSLY DID
        res = 0
        # SUMMING EVERYTHING UPWARDS AND CHECKING BACK
        for r in range(1, len(prices)):
            if prices[r] > prices[r - 1]:
                res += prices[r] - prices[r - 1]
        return res