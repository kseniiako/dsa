# Remove Duplicates From Sorted Array (Leetcode 26)

# Given an integer array sorted in non-decrasing order, remove the duplicates
# in-place such that each unique element appears only once. The relative order
# of the elements should be kept the same.

# You must place the result in the first part of the
# array. What is in the rest of the array, doesn't matter,
# but the array length must be preserved (length of updated array must 
# be the same as input array length).

# Example: you are passed an n-long array with k distinct elements.
# You must update the array to be an n-long array where the first k elements are 
# the distinct k elements, and the remaining n - k elements can be anything.

# DO NOT RETURN ARRAY. Return k after placing the final result in the first k slots
# of nums. Id est, return length of array if it contained only unique elements.

# You must solve this using O(1) extra memory.

# Strategy: we can use a two-pointers approach to solve this. Clarification:
# strictly speaking, by "two pointers" I mean two variables holding indices of the array.

# The first element is apriori in the right place. Create variables for a fast and a slow pointer.
# The first duplicate can occur at index 1 -> set both pointers to be equal to this index. 
# We should also initialize a value prev (stands for previous) to be the first (0-indexed) element 
# in the array. Now, until the fast pointer reaches the end of the array, proceed:
# The fast pointer is incremented by 1 in every iteration. The value at this pointer
# (i. e. at the index designated by this variable's value) is checked against the value of
# prev. If it is not the same, we've reached a new unique number! We set the element at the
# index designated by the "slow pointer" variable to be this new element. We increment
# the slow pointer by 1: this is the place in which we'll put the next unique variable we
# encounter. The prev variable is updated.

# Once the fast pointer is out of bounds, the slow pointer will be the index right before which
# the relevant output ends. So the length of the distinct-numbers array is equal to slow pointer.

class Solution:
    def removeDuplicates(self, nums):
        next_val_index = i = 1
        prev = nums[0]
        max_len = len(nums)
        while i < max_len:
            if nums[i] != prev:
                prev = nums[i]
                nums[next_val_index] = nums[i]
                next_val_index += 1

            i += 1
        
        print(nums)
        return next_val_index

        # Time complexity: two passes of the array: O(2n) -> O(n).
        # Space complexity: we only assign constant-space variables. O(1).

    # Smart idea (from Leetcode): we can do without prev variable whatsoever!
    # Note that the slow pointer points to previous value (before it is updated). 
    # Just tweak the rules for updating the slow pointer, and voila! We need even less space :)

    def removeDuplicates2(self, arr):
        fast = slow = 0
        max_len = len(arr)
        while fast < max_len:
            if arr[fast] != arr[slow]:
                slow += 1
                arr[slow] = arr[fast]
            fast += 1

        print(arr)
        return slow + 1

        # Unfortunately, with Leetcode testing, this version seems to run slower.
        # I suppose this is so because of the added cost of calculating value at index slow
        # each time we compare it to fast. Would be interesting to compare the speeds of the two
        # functions and see the difference on my machine!

if __name__ == "__main__":
    my = Solution()
    print(my.removeDuplicates([1,1,2]))
    print(my.removeDuplicates([0,0,1,1,1,2,2,3,3,4]))

    print(my.removeDuplicates2([1,1,2]))
    print(my.removeDuplicates2([0,0,1,1,1,2,2,3,3,4]))