class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        minbuy = prices[0]
        maxsell=-1
        res = 0
        for i in prices:
            if i <=minbuy:
                minbuy = i
                maxsell = -1
            else: 
                if i>maxsell:
                    maxsell=i
            if maxsell!=-1:
                tempres = maxsell - minbuy
                res = max(tempres,res)
        return res
