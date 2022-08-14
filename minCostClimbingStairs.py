# Min Cost Climbing Stairs (Leetcode 746)

# You are given an integer array cost, where cost[i]
# is the cost of ith step on a staircase. Once you pay the
# cost, you can either climb one or two steps.

# You can either start with index 0, or index 1. 

# Return the minimum cost to reach the top floor.

# Length of input array is in the range 2 <= len(cost) <= 1000

class Solution:
    def minCostClimbingStairs(self, cost):
        # This is a dynamic programming solution that uses two variables
        # to hold cumulative min-cost values for the positions one step away and
        # two steps away (i. e. for positions i+1 and i+2: the two next-step 
        # destinations from position i). We iterate backwards over the array
        # to calculate cumulative min cost.

        first, second = cost[-2], cost[-1]

        for i in range((len(cost)-3), -1, -1):
            second, first = first, cost[i]+min(first, second)

        # Since we know we can start from step 0 or 1 in the array 
        # (that is, from base position we can make a two-step move 
        # or one-step move, just as later on the staircase), we need
        # to return the minimum between min-cost values for starting
        # from each of these positons.
        return min(first, second)

        # O(n) time complexity (the number of iterations of constant-time
        # operations is on the order of n, or input length)
        # O(1) space complexity: we allocate constant extra space for two
        # variables

if __name__ == "__main__":
    my = Solution()

    print(my.minCostClimbingStairs([1, 2]))
    print(my.minCostClimbingStairs([1, 2, 3]))
    print(my.minCostClimbingStairs([10,15,20]))
    print(my.minCostClimbingStairs([1,100,1,1,1,100,1,1,100,1]))


