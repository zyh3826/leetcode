class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        import sys
        minPrice = sys.maxsize
        maxPrice = 0
        for i in range(len(prices)):
            if prices[i] < minPrice:
                minPrice = prices[i]
            elif prices[i] - minPrice > maxPrice:
                maxPrice = prices[i] - minPrice
        return maxPrice
