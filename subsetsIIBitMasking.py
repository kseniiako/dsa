# There is no code in this file! It is just a textual
# explanation of a solution to Subsets II (Leetcode 90)
# based on bit masking. This is heavily based on the Leetcode
# article for this problem.

# Intuition:

# There are a total of 2^n distinct subsets for an array of
# length n with no duplicates. According to explicit problem
# constraints, the max possible value of n is 10. Thus, no more
# than 2^10 = 1024 subsets will be generated. Since this number
# is small, we can represet all the possible subsets using bit masking.

# Idea: map each subset to a bitmask of length n, where 1 in
# the ith position of the bitmask implies nums[i] is in the subset,
# and 0 implies nums[i] is not in the subset. 

# However, in this approach, if there are duplicates in the input array,
# then some of the generated subsets will be duplicates, too. We need to use
# an additional set, seen, to detect duplicate subsets. In order to make use of
# seen, we must first sort the given array. Otherwise, seen won't be able to distinguish
# between duplicate subsets (if the order in which the subset elements are arranged is 
# different for each of the duplicates).

# Algorithm

# 1. Sort nums array.
# 2. Initialize maxNumberOfSubsets to the max number of subsets that
# can be generated, i. e. 2^n.
# 3. Initialize a set, seen, to store the generated subsets. Adding all
# sorted subsets to the set gives us the opportunity to catch any duplicate
# subsets.
# 4. Iterate from 0 to maxNumberOfSubsets - 1. The set bits in the binary
# representation of the subsetIndex indicate the position of the elements in the
# nums array that are present in the current subset.
# 5. Initialize a string hashcode which will store a comma-separated list of
# numbers in the currentSubset as a string. Hashcode is necessary to uniquely
# identify each subset via the use of a set.
# 6. We run an inner for loop from j = 0 to n - 1 to check the position of set bits
# in subsetIndex. If at the jth position bit is set, add nums[j] to the current subset
# via the use of a set.
# 7. Add the current subset currentSubset to seen and to the subsets list if
# the generated hashcode is not in seen.
# 8. Return subsets.

# Note that in python you can deal with transferring subsets from string to list type
# and from a set to a list (of subsets) very quickly and easily using a comprehension.

# Note: there is something called StringBuilder in Java which requires O(n) time to
# be converted to a string.

# Time complexity: O(n*2^n).
# Sorting the array -> O(nlogn). Outer for loop runs 2^n times. Inner loop
# runs n times. We know that average case time complexity for set operations
# is O(1). To generate a hash value for each subset, O(n) time is required,
# and we generate the hashcode in parallel/element by element as we are running
# the inner for loop. So the overall time complexity is O(nlogn + (2^n) * n (n is for inner
# loop)) = O(n*2^n).

# Space complexity: O(n*2^n). (O(n) for python!)
# We need to store at most 2^n number of subsets in the set seen (again,
# might not be an issue in python — depending on your perspective). Max
# length of any subset is n.
# Space complexity of the sorting algorithm depends on the implementation.
# By default, in python — timsort — O(n). Java uses a variant of
# quicksort that needs O(log n) memory. In C++, STL sort() function is a hybrid of
# quicksort, heapsort, and insertion sort, and memory use is also O(logn).
