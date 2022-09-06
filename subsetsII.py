# Subsets II (Leetcode 90)

# Given an integer aray nums that may contain duplicates, return
# all possible subsets (the power set).

# Note: do not return equal subsets (repeats)!

class Solution:
    def subsetsWithDup(self, nums):
        # Sort input array
        nums.sort()
        output = []
        
        # Backtrack function (to be called recursively)
        def backtrack(i, cur):
            # If we've reached the target, return
            if i == len(nums):
                output.append(list(cur))
                return

            # Count occurrences of the current value in the array.
            k = 1
            while i+k in range(len(nums)) and \
            nums[i] == nums[i+k]:
                k+= 1
            # Call backtrack on the first value unequal to the
            # current one (skip all the repeats)
            backtrack(i+k, cur)

            num = nums[i]

            # Now try appending all possible numbers of occurrences
            # of current value to the current subset. E. g. if we've determined
            # there are 3 4s, we try adding one four, two fours, and three fours.
            # Call backtrack on each of these options, where index passed to backtrack
            # function indicates the first value non-equal to the current one 
            # (skip the repeats).
            for x in range(k):
                cur.append(num)
                backtrack(i+k, cur)
            
            # Now pop all the added repeated values from the current subset.
            for x in range(k):
                cur.pop()

            # Time complexity: O(2^n) subsets will be generated. Generating each subset
            # requires O(n) calls to backtrack, and additional time on the order of O(n)
            # per call due to all the iterations over the list (to check for repeats and
            # handle them properly). Creating a deep copy of each subset is also O(n) time. 
            # Result: O((n^2+n)*2^n) -> O(n^2*2^n) total time complexity.
            # Space complexity: O(n) to keep current subset (variable cur) and
            # O(n) for recursive depth. Total: O(n).

        backtrack(0, [])
        return output

    # There are some other awesome solutions to this problem, including bit masking!
    # For now, here is an approach that mimics the second solution (the one from Neetcode)
    # of Combination Sum 2 that I have in this repository. That is, create just one "branch"
    # for adding the duplicate numbers to the subset (going through all the possible numbers
    # of occurrences of the repeat element: not more, not less) instead of having multiple 
    # redundant branches grow there.
    def subsetsWithDup2(self, nums):

        nums.sort()
        output = []
        # Potentially smart design choice: do not pass current subset/combination
        # to the nested function backtrack! It will be available to backtrack simply
        # by virtue of being in the scope of its parent function.
        cur = []

        def backtrack(i):
            if i >= len(nums):
                output.append(list(cur))
                return
            
            cur.append(nums[i])
            backtrack(i+1)
            cur.pop()
            
            occurrences = 1
            step = 1
            while i + step < len(nums) and nums[i] == nums[i+step]:
                step += 1
            backtrack(i+step)

        backtrack(0)
        return output

        # Time complexity: O(2^n) possible subsets generated. Generating a subset requires
        # O(n) calls to backtrack + we need O(n) time to make a deep copy of each ready subset.
        # Total time complexity is O((2n)*2^n) -> O(n*2^n).
        # Space complexity: O(n) for function call stack + O(n) to keep current subset ->
        # total space complexity is O(n).

if __name__ == '__main__':
    my = Solution()
    print(my.subsetsWithDup([1, 2, 3]))
    print(my.subsetsWithDup([1,2,2]))
    print(my.subsetsWithDup([0]))
    print(my.subsetsWithDup([5,5,5,5,5]))        

    print(my.subsetsWithDup2([1, 2, 3]))
    print(my.subsetsWithDup2([1,2,2]))
    print(my.subsetsWithDup2([0]))
    print(my.subsetsWithDup2([5,5,5,5,5]))        
    
            