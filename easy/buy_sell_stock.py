import time

"""You are given an array prices where prices[i] is the price of a given stock on the ith day.

You want to maximize your profit by choosing a single day to buy one stock and choosing a different day in the future to sell that stock.

Return the maximum profit you can achieve from this transaction. If you cannot achieve any profit, return 0.

 

Example 1:

Input: prices = [7,1,5,3,6,4]
Output: 5
Explanation: Buy on day 2 (price = 1) and sell on day 5 (price = 6), profit = 6-1 = 5.
Note that buying on day 2 and selling on day 1 is not allowed because you must buy before you sell.
Example 2:

Input: prices = [7,6,4,3,1]
Output: 0
Explanation: In this case, no transactions are done and the max profit = 0.
 

Constraints:

1 <= prices.length <= 105
0 <= prices[i] <= 104
"""

class soln1:
    def max_profit(self, prices: list[int]) -> int:
        '''runtime error'''
        lptr, rptr = 0, len(prices) - 1
        while prices[lptr] > prices[lptr + 1] and lptr < len(prices)//2:
            lptr += 1
        while prices[rptr] < prices[rptr - 1] and rptr > len(prices)//2:
            rptr -= 1
        print('\n')
        if prices[rptr] - prices[lptr] > 0:
            return prices[rptr] - prices[lptr]
        else:
            return 0       
        
class soln2:
    def max_profit(self, prices: list[int]) -> int:
        '''Runtime: 1595 ms, faster than 47.21% of Python3 online submissions for Best Time to Buy and Sell Stock.
        Memory Usage: 25 MB, less than 85.25% of Python3 online submissions for Best Time to Buy and Sell Stock.
        problem[SOLVED] - when there are local and global minimas e.g - [7,2,6,1,8,1] - it will work'''
        max_price = prices[rptr] - prices[lptr]
        lptr = 0
        for rptr in range(1, len(prices)):
            if prices[lptr] > prices[rptr]:
                lptr = rptr
            max_price = max(max_price, prices[rptr] - prices[lptr])
        return max_price



test = soln2()

start = time.perf_counter()
ans = test.max_profit([7,6,4,3,1])
end = time.perf_counter()
print(ans)
print(f"time = {end - start}") 

start = time.perf_counter()
ans = test.max_profit([7,1,5,3,6,4])
end = time.perf_counter()
print(ans)
print(f"time = {end - start}")            