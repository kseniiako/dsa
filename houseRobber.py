# House Robber (Leetcode 198)

# You are a robber looking to get the max amount of money
# from robbing a street of houses (represented as an array where
# the value of each element is the profit of robbing a particular 
# house). Constraint: you cannot rob any two adjacent houses (it
# would alert the police). Return the maximum profit you can obtain
# from robbery without alerting the police.

# Length of street can be between 1 and 100 houses (inclusive).

class Solution:
    def robBruteForce(self, arr):
        # Recursive brute-force solution. Beware: 2^n time!
        
        # base cases
        if len(arr) == 1:
            return arr[0]
        if len(arr) == 2:
            return max(arr[0], arr[1])
            
        # return max between robbing the closest house + any of 
        # the houses two positions removed and robbing any of the
        # houses one posiiton removed
        return max((arr[-1]+self.robBruteForce(arr[:-2])), 
        self.robBruteForce(arr[:-1]))

    def robRecurse(self, arr):
        # This is a recursive solution that optimizes the
        # brute force approach to achieve O(n) asymptotic time. 
        # It utilizes memoization.

        cache = {}

        def robHelper(i, arr):
            # helper function takes array and current position in
            # array.

            # edge case: end of array reached, nothing left to examine.
            if i >= len(arr):
                return 0

            # check if the max profit from robbing all positions up to 
            # and including i is already cached. If so, we're in luck!
            # Return the cached value
            nonlocal cache
            if i in cache:
                return cache[i]

            # if max profit for i is not already cached, recurse
            # to compute it.
            result_i = max(robHelper(i+1, arr), 
            robHelper(i+2, arr) + arr[i])

            # now we cache the result we got for future use
            cache[i] = result_i

            return result_i
        
        # initialize cache and call helper function on the
        # beginning of the array.
        cache = {}
        return robHelper(0, arr)

        # O(n) time — optimized because all recursive calls
        # now take O(1) time each thanks to caching. O(n) space —
        # we need to hold the O(n) cache and the O(n) recursion stack 
        # in memory.

    def robIter(self, arr):
        # Iterative approach: this version runs in 
        # O(n) time and utilizes O(1) space (just two
        # extra variables initialized)

        # Let first and second be the houses two and one
        # positions to the left, respectively, from the house
        # we are currently considering.
        first, second = 0, 0

        # For every element in array, update second to include the
        # biggest total profit between robbing the houses two 
        # positions away + house at current position and robbing
        # houses one position away.
        # This way, we don't bother robbing houses one position away
        # (more restrictions for us) unless it's more profitable than
        # robbing two positions away.
        for i in arr:
            first, second = second, max(i + first, second)
        
        return second

    

if __name__ == "__main__":
    my = Solution()

    print(my.robBruteForce([1,2,3,1]))
    print(my.robBruteForce([2,7,9,3,1]))

    #Careful: takes pretty long to run!
    #print(my.robBruteForce([183,219,57,193,94,233,202,154,65,240,97,234,100,249,186,66,90,238,168,128,177,235,50,81,185,165,217,207,88,80,112,78,135,62,228,247,211]))


    print(my.robIter([1,2,3,1]))
    print(my.robIter([2,7,9,3,1]))
    print(my.robIter([183,219,57,193,94,233,202,154,65,240,97,234,100,249,186,66,90,238,168,128,177,235,50,81,185,165,217,207,88,80,112,78,135,62,228,247,211]))

    print(my.robRecurse([1,2,3,1]))
    print(my.robRecurse([2,7,9,3,1]))
    print(my.robIter([183,219,57,193,94,233,202,154,65,240,97,234,100,249,186,66,90,238,168,128,177,235,50,81,185,165,217,207,88,80,112,78,135,62,228,247,211]))

