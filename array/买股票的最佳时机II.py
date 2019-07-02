class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        return sum(y - x for x, y in zip(prices[:-1], prices[1:]) if y > x)
        
#solution: https://leetcode-cn.com/problems/best-time-to-buy-and-sell-stock-ii/solution/mai-mai-gu-piao-de-zui-jia-shi-ji-ii-by-leetcode/
