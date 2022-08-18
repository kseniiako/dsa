# Longest Consecutive Sequence (Leetcode 128)

# Given an unsorted array of integers nums, return the
# length of the longest consecutive elements sequence. 
# Algorithm must run on O(n) time.

class Solution:
    def longestConsecutive(self, nums):
        # My first idea was to sort the numbers and look
        # through the array. However, a sort would run in O(nlogn)
        # time -> this algorithm is not fast enough for the given
        # problem constraints. However, here is an implementation
        # since it is a viable solution under looser constraints.

        if not nums:
            return 0

        nums_sorted = sorted(nums)

        # Since array is non-empty, for each element
        # in the array the consecutive subarray has at least
        # length 1. max_subarray has length 1 by extension.
        cur_subarray = 1
        max_subarray = 1

        for i in (range(len(nums_sorted)-1)):
            
            # if there is a repeat, ignore the non-last
            # repeating items
            if nums_sorted[i]==nums_sorted[i+1]:
                continue
        
            if nums_sorted[i]+1==nums_sorted[i+1]:
                cur_subarray += 1

            else:
                max_subarray = max(max_subarray, cur_subarray)
                cur_subarray = 1

        return max(max_subarray, cur_subarray)

        # Sort runs in O(nlogn) time (python uses timsort). After 
        # sorting, we have n iterations of the loop, where every
        # iteration runs in constant time. Total time complexity of this
        # algorithm is O(nlogn+n)->O(nlogn)

        # Unless we are allowed to modify the array in place, we need to
        # allocate O(n) extra space for the sorted array. Therefore,
        # the space complexity is O(n).

    def longestConsecutiveFast(self, nums):
        # This approach builds on the intuitive brute force approach
        # (iterating through all possible array element combinations
        # to find consecutive sequences and largest consecutive sequence). 
        # However, as intelligent sequence building goes, it introduces some 
        # improvements. 

        # First, we store numbers in a set instead of an array for O(1) lookups.
        # Second, we only consider beginning sequences with numbers that are not
        # already part of a longer sequence. That is, if for a number n the
        # predecessor n-1 is already present in the array, the sequence [n, (n+1),
        # (n+2)...] is apriori part of a longer sequence. Therefore, we do not
        # consider it.

        # initialize count variables analogously
        # to the first solution

        # initializing max_longest to 0 ensures the
        # algorithm runs correctly on empty array input.
        cur_subarray = 1
        max_subarray = 0

        nums_set = set(nums)

        for num in nums_set:
            if num-1 not in nums_set:
                while num+1 in nums_set:
                    cur_subarray += 1
                    num += 1
                
                max_subarray = max(max_subarray, cur_subarray)
                cur_subarray = 1

        return max_subarray

        # Space complexity: O(n) to create a set.
        # Time complexity: you would think that the two embedded loops
        # in this algorithm (a while inside a for) would amount to O(n^2)
        # time complexity. However, since at the beginning of every
        # iteration of the for loop we check whether the current number
        # could be a beginning of a consecutive subsequence, total number
        # of times the while loop could be run is always within n. Therefore,
        # the total time complexity of this part of the code is O(n+n)->O(n).
        # The rest of the algorithm is constant-time computations. We get O(n)
        # total time complexity.

if __name__ == "__main__":
    my = Solution()
    print(my.longestConsecutive([100,4,200,1,3,2]))
    print(my.longestConsecutive([0,3,7,2,5,8,4,6,0,1]))
    print(my.longestConsecutive([0]))
    print(my.longestConsecutive([]))

    print(my.longestConsecutiveFast([100,4,200,1,3,2]))
    print(my.longestConsecutiveFast([0,3,7,2,5,8,4,6,0,1]))
    print(my.longestConsecutiveFast([0]))
    print(my.longestConsecutiveFast([]))

    # Repeat cases
    print(my.longestConsecutive([1, 0, 1, 2]))
    print(my.longestConsecutiveFast([1, 0, 1, 2]))

# Takeaways/ideas:
# 1) Good idea to check for max between cur_subarray and max_subarray
# at return statement in case there is a chance max_subarray hasn't been
# updated yet (e. g. when the longest consecutive subarray ends at the
# end of the array).
# 2) Lists and sets are different beasts: e. g. when checking for consecutive
# elements in a sorted list, beware of repeated numbers offsetting your calculations.
# Either turn list to set and then to a sorted list to eliminate repeats, or account
# for repeats in your logic. Or, perhaps, stick to working with sets?
# 3) Continue goes to the next loop iteration, break escapes the loop completely.