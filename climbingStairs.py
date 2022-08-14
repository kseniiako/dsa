# Climbing Stairs (LC 70)

# You are climbing a staicase of n steps.
# Each time you can either climb 1 or 2 steps.

# Given step count n, count the number of distinct ways
# that you can climb to the top.

# Inputs are: 1 <= n <= 100

class Solution:
    def climbStairs(self, n):
        # By keeping track of the decision tree representing
        # this problem, one can see that the progression of the
        # count of ways to climb to the top for each output is...
        # the fibonacci sequence!
        
        nMinus2, nMinus1 = 1, 2

        # base cases: we can climb a one-step staircase
        # in one way, a two-step staircase — in two ways.
        if n == 1:
            return nMinus2
        if n == 2:
            return nMinus1
        
        # updating values until nMinus1 holds the output
        # for n steps
        for _ in range(3, n+1):
            nMinus2, nMinus1 = nMinus1, nMinus1 + nMinus2
        
        return nMinus1

        # this solution runs in O(n) time: we perform
        # constant-time assignments/arithmetic operations on the order
        # of n times, where n is the input (length of staircase). 
        # We only allocate extre space for two variables, so 
        # space complexity is O(1)

if __name__ == "__main__":
    my = Solution()

    print(my.climbStairs(1))
    print(my.climbStairs(2))
    print(my.climbStairs(3))
    print(my.climbStairs(45))
    print(my.climbStairs(100))
