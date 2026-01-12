#The trick : track the minimum price and the maximum possible profit
#Keep track of the buy price --> keep comparing the current price with prvious buy price and track of the minimum price while iterating through the list
#However, if the current price is greater than the previous buy price
#now check if you sell it now would you get a better profit than the previous one
#   Keep track of the maximum profit


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        cp=prices[0]
        profit=0

        for i in range(1, len(prices)):
            if prices[i]<cp: cp=prices[i]
            else: profit= max(profit, prices[i]-cp)

        return profit