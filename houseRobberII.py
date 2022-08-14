# House Robber II (Leetcode 213)

# You are a robber who aims to get max profit
# out of robbing the houses on a very creepy street where
# the houses are arranged in a circle. (The first house
# is the neighbor of the last one.) You cannot rob any two
# adjacent houses. The houses are represented as an array
# where each element i is the profit from robbing ith house 
# on the street. Return the max available profit.

# Hint: since house[0] and house[len(arr)-1] are adjacent,
# they can't be robbed together. So the objective is to find
# max profit between robbing house[0] to house[len(arr)-2] or
# house[1] to house[len(arr)-1].

class Solution:
    def robCircle(self, arr):
        # my initial idea was to implement this algorithm
        # via two passes of a classic houseRobber algorithm. 

        def robHelper(arr):
            # for explanations of this algorithm, refer to
            # houseRobber.py
            first, second = 0, 0

            for x in arr:
                first, second = second, max(second, first + x)

            return second
        
        return max(robHelper(arr[:-1]), robHelper(arr[1:]))


if __name__ == "__main__":
    my = Solution()

    print(my.robCircle([1,2,3,1]))
    print(my.robCircle([2,7,9,3,1]))
    #print(my.robCircle([183,219,57,193,94,233,202,154,65,240,97,234,100,249,186,66,90,238,168,128,177,235,50,81,185,165,217,207,88,80,112,78,135,62,228,247,211]))

    print(my.robCircle([2,3,2]))
    print(my.robCircle([1,2,3,1]))
    print(my.robCircle([1,2,3]))



