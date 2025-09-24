class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        
        if not prices or len(prices)<2:
            return 0
        
        n = len(prices)
        k= 2 # two transactions

        #buy-sell table
        dp = [[0]*n for _ in range(k+1)]
            
        
        #update
        for i in range(1,k+1):
            max_diff = -prices[0]
            for j in range(1,n):
                dp[i][j] = max(dp[i][j-1], prices[j]+ max_diff)
                max_diff = max(max_diff, dp[i-1][j]-prices[j])
        
        return dp[k][n-1]



