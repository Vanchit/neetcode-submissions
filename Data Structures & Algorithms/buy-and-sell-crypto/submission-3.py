class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        

        #[10,    1,    5,   6    7    1]
         #0      1     2    3    4    5

        left = 0
        right = 1
        maxP = 0

        while right < len(prices):
            if prices[left] < prices[right]:
                profit = prices[right] - prices[left]
                maxP = max(profit, maxP)
                
            else:
                left = right
            right += 1
        return maxP



         