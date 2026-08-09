class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        d=0
        sum=prices[0]
        for i in range(len(prices)):
            sum=min(sum,prices[i])
            d=max(d,prices[i]-sum)
        return d