class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        price = 0
        maximum = 0
        l = 0
        r = 1
        n = len(prices)
        while r<n:
            if prices[l]<prices[r]:
                price = prices[r]-prices[l]
                maximum = max(maximum,price)
            else:
                l=r
            r+=1
        return maximum

        
        
        