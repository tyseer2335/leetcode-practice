class Solution:
    def maxProfit(self, prices: List[int]) -> int: 
############################################################################################################################## 
# Brute Force Solution O(n^2)
############################################################################################################################## 

        # max_profit = 0   
        # for B in range(len(prices)):
        #     for S in range(B+1, len(prices)): 
        #         max_profit = max(max_profit, prices[S] - prices[B]) 
        # return max_profit 

############################################################################################################################## 
# 2 Pointer Solution 
############################################################################################################################## 

        # Result 0 by default
        res = 0

        # Our left and right pointers 
        l = 0 
        r = 1 

        # Loop through prices
        while r < len(prices):  

            # If we make no profit
            if prices[l] >= prices[r]:  
                # Update left pointer plus 1, and right to the next of left 
                # Since we made no money we can increment left to find a better starting point
                l += 1  
                r = l + 1 

            # We made some money
            else: 
                profit = prices[r] - prices[l] # Compute profit
                res = max(profit, res) # Update result if its max profit
                r += 1 # Increment r to see if we can make more by selling the next day

        return res

############################################################################################################################## 
# Min So Far Solution 
##############################################################################################################################        # We can keep track of a min so far varable as we iterate through the array 
    # If we encounter a better min so far we know that we cant make profit so we update minSoFar 
    # If we can make profit we update maxProfitSoFar 

        # Variables needed
        # maxProfit = 0 
        # minSoFar = prices[0]

        # # Loop through all prices starting at index 1
        # for i in range(1, len(prices)):  
        #     # If we cant make profit
        #     if prices[i] <= minSoFar: 
        #         minSoFar = prices[i] 
        #     else:  
        #         # If we can make profit see if its max
        #         profit = prices[i] - minSoFar 
        #         maxProfit = max(maxProfit, profit) 

        # return maxProfit 

    # Time 7:07 
    # Time Copmplexity: O(n) 
    # Space Complexity: O(1)
            
    # For an good explination watch https://www.youtube.com/watch?v=kJZrMGpyWpk&ab_channel=GregHogg

