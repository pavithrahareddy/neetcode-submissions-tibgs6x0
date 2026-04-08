class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        i,j,res = 0,1,0
        while i<=len(prices)-2 and j<=len(prices)-1:
            if prices[i]<=prices[j]:
                res = max(res,prices[j]-prices[i])
                j = j+1
            else:
                i = j
                j = j+1
        return res



        
        