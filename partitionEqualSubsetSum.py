# Partition Equal Subset Sum (Leetcode 416)

# Given a non-empty array nums containing only positive integers,
# find if the array can be partitioned into two subsets such that
# the sum of elements in both subsets is equal.

class Solution:
    def canPartition(self, nums):
        # Brute-force solution

        half_size, mod = divmod(sum(nums), 2)
        if mod:
            return False

        def doTheySum(nums, target):
            for i in range(len(nums)):
                if nums[i] == target:
                    return True
                if nums[i] > target:
                    return False
                else:
                    new_lst = [nums[j] for j in range(len(nums)) if j != i]
                    if doTheySum(new_lst, target - nums[i]): return True

            return False
        
        return doTheySum(nums, half_size)

        # This brute-force solution runs in exponential (2^n) time. It also
        # needs O(n(n-1)/2) -> O(n^2) space to hold the recursion calls and 
        # new_lst versions for each one of them.

        # Cache dimensions: O(n*sum(nums)) -> time and memory complexity
        # of a naive solution with cache.
        # We can improve on this using dynamic programming!

    def canPartition1(self, nums):
        
        half_size, mod = divmod(sum(nums), 2)
        if mod:
            return False

        cache = set()
        
        for x in nums:
            if x == half_size:
                return True
            if x > half_size:
                return False

            new_cache = set()
            new_cache.add(x)

            for y in cache:
                new_cache.add(y)
                if x + y == half_size:
                    return True
                if x + y < half_size:
                    new_cache.add(x+y)
            
            cache = new_cache

        return False

    # O(n*sum(nums)) time complexity (for the nested loop).
    # O(sum(nums)) complexity to store the cache. (Notice that
    # no values greater than or equal to sum(nums)/2 (half_sum)
    # get stored in the cache set, and no duplicates are possible 
    # in a set.)

    # I like solution, it is great that it short-circuits a lot 
    # to save us time and space.

    # Difference: in the first solution we were looking at one target
    # at a time, going down branches of the decision tree, whereas in 
    # the second solution, we are caching multiple possible targets
    # to speed up search!

            

            
    

                

     
if __name__ == "__main__":
    my = Solution()
    print(my.canPartition([1,5,11,5]))
    print(my.canPartition([1,2,3,5]))
    print(my.canPartition([3,3,3,4,5]))

    print(my.canPartition1([1,5,11,5]))
    print(my.canPartition1([1,2,3,5]))
    print(my.canPartition1([3,3,3,4,5]))
    print(my.canPartition1([1,2,5]))