# Best time to buy and sell stock! 
# The notoriouis LC 121! 

# You are given an array prices where prices[i] is the price of
# a given stock on the ith day. You want to maximize your profit by 
# choosing a single day to buy one stock and a different day in
# the future to sell that stock. 

# Return the maximum profit you can achieve from this transaction. 

# Some notes:
# a) price cannot be lower than 0
# b) we need to pick basically the smallest and the
# largest number in the array: with the constraint
# that the largest number must be located after the smallest number. 

from math import inf

class Solution():
    def Kadane(self, arr):
        # I'm brushing up on dynamic programming concepts.
        # This is Kadane's algorithm to find max value subarray
        # within an array.
        current_sub = max_sub = arr[0]

        for x in arr[1:]:
            current_sub += x
            if current_sub < 0:
                current_sub = x
            max_sub = max(max_sub, current_sub)
        
        return max_sub
    
    def Kadane_elegant(self, arr):
        # A more elegant formulation of the same solution
        # as seen on Leetcode. 

        current_sub = max_sub = arr[0]

        for x in arr[1:]:
            current_sub = max(current_sub + x, x)
            max_sub = max(max_sub, current_sub)

        return max_sub

    def bruteForce(self, prices):
        # Now on to the max profit algorithm itself!
        # First let's try the brute force solution as 
        # described on Leetcode. 
        max_profit = 0
        for i in range(len(prices)):
            for j in range(i + 1, len(prices)):
                profit = prices[j] - prices[i]
                if profit > max_profit:
                    max_profit = profit
        return max_profit

    def onePass(self, prices):
        # a one-pass solution (as recommended by Leetcode)

        max_profit = 0

        smallest = inf
        for x in prices:
            if x < smallest:
                smallest = x
            
            else:
                if (x - smallest) > max_profit:
                    max_profit = x - smallest
        
        return max_profit

        # yoo I feel so happy having coded this up!


my = Solution()
print(my.Kadane([-2,1,-3,4,-1,2,1,-5,4]))
print(my.Kadane([1]))
print(my.Kadane([5, 4, -1, 7, 8]))

print(my.Kadane_elegant([-2,1,-3,4,-1,2,1,-5,4]))
print(my.Kadane_elegant([1]))
print(my.Kadane_elegant([5, 4, -1, 7, 8]))

prices1 = [7,1,5,3,6,4]
prices2 = [7,6,4,3,1]

print(my.bruteForce(prices1))
print(my.onePass(prices1))

print(my.bruteForce(prices2))
print(my.onePass(prices2))

# 


