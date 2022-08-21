# Coin Change (Leetcode 322)

# You are given an integer array representing different
# coin denominations and an integer representing a
# total amount of money.

# Return the fewest number of coins that you need to make up
# that amount. The only denominations avalialble to you are
# in the array. You can use as many coins of each denomination
# as you'd like.

# If the target amount of money cannot be made up by any
# combination of coins of given denominations, return -1.

class Solution:
    def coinChange(self, coins, amount):
        # Dynamic programming solution!

        # Amount + 1 is more than the max possible coin count:
        # use it as default value. We initialize an array to hold
        # all possible amounts within given amount (inclusive of
        # the given amount itself). This array will hold minimum
        # coin counts for each target amount.
        dp = [amount+1] * (amount + 1)

        # Base case: we need 0 coins to get amount 0.
        dp[0] = 0

        # For each target value from one to amount, check 
        # coin count for adding each possible coin denomination
        # (such that coin denomination is not bigger than target
        # amount) and save the minimum coin count. 
        # In every comparison, coin count is 1 (for the
        # one coin added) + value in the array at the index
        # [current position - added coin denomination]. 
        # Thus we try all coin values for all amounts and
        # go through the decision tree in an optimized way!
        for i in range(1, amount+1):
            for c in coins:
                if i - c >= 0:
                    dp[i] = min(dp[i], 1 + dp[i-c])
        
        # Return coin count at index [amount]. 
        # If coin count is unset (still the default one), this 
        # means no coin denominations fit, and it is impossible 
        # to get this amount with given denominations. Return -1.
        return dp[-1] if dp[-1] < (amount + 1) else -1

        # Time complexity O(amount*(no of coins)) for the nested loops.
        # Space complexity O(amount) to keep the dp array.

if __name__ == "__main__":
    my = Solution()

    print(my.coinChange([1,2,5], 11))
    print(my.coinChange([2], 3))
    print(my.coinChange([1], 0))