# Longest Increasing Subsequence (Leetcode 300)

# Given an integer array nums, return the length
# of the longest strictly increasing subsequence. 

# A subsequence is a sequence that can be derived from an
# array without changing the order of the remaining elements.

# Solutions and explanations double as my notes for this article
# on Leetcode: 
# https://leetcode.com/problems/longest-increasing-subsequence/solution/

class Solution:
    def lengthOfLIS_DP(self, nums):
        # A dynamic programming solution

        # As we go through the input, each decision we make is simple:
        # is it worth to consider this number? If we use a number, it may 
        # contribute towards an increasing subsequence, but it may also
        # eliminate larger elements that came before it.

        # Let's construct an array dp where dp[i] is the length of the
        # longest increasing substring that ends with ith element. (1d state)

        # Recurrence relation: dp[i] = max(dp[j]+1) for all j where 
        # nums[j] < nums[i] and j < i

        # We can initialize every element of dp to 1 since every element
        # on its own is an increasing subsequence.

        dp = [1 for _ in nums]
        for i in range(1, len(nums)):
            for j in range(i):
                if nums[j]<nums[i]:
                    dp[i] = max(dp[i], dp[j]+1)

        return max(dp)

        # Space complexity is O(n) (to hold the dp array).
        # Time complexity is O(n^2) for two nested loops.
        # Loops result in 1 + 2 + 3 + 4 + ... + n = n(n+1)/2
        # operations -> O(n^2) time.

    def lengthOfLIS_ISB(self, nums):
        # An approach in the spirit of intelligent
        # subsequence building.

        # The best way of building a subsequence: for each
        # element num, if num is greater than the largest element in
        # out subsequence, then add it to the subsequence. Otherwise,
        # perform a linear scan through the subsequence starting with
        # the smallest element and replace the first element that is
        # greater than (or, for that matter, equal to) num with num.
        # This potentially makes the max available subsequence longer
        # since it opens the door to elements that are greater than num
        # but less than the element num replaced. 

        # This approach has a surprising nuance: it does not always
        # generate a valid subsequence of the input, but the length
        # of the generated subsequence will always equal the length
        # of the longest increasing subsequence. The length remains
        # correct since the length only changes when a new element
        # is larger than any element in the subsequence. (Then this
        # element is appended instead of replacing another element.)

        subsequence = [nums[0]]

        for i in range(1, len(nums)):
            if nums[i]>subsequence[-1]:
                subsequence.append(nums[i])
            else:
                for j in range(len(subsequence)):
                    if subsequence[j]>=nums[i]:
                        subsequence[j] = nums[i]
                        break

        return(len(subsequence))

        # Space complexity is O(n): we only allocate extra space
        # for the subsequence array, which can be at most n elements
        # long (if the whole sequence monotonically increases). 

        # Time complexity: O(n^2) in the worst case. However, in best
        # and average cases this approach is more efficient than the
        # previous one since we don't have to check n-1 previous values
        # for nth element in array: instead we iterate only until we find
        # the first element in the current subsequence that can be replaced 
        # by the new element (i. e. the first element in the current 
        # subsequence that is equal to or greater than the new element).

    def lengthOfLIS_BinSearch(self, nums):
        # An improvement on the previous approach using binary search.

        # In the prevous approach, when we have an element n that is
        # not greater than all the elements in current subsequence, 
        # we do a linear scan to find the first element in current
        # subsequence that is greater than or equal to n. Since current
        # subsequence is sorted, we can use binary search on it
        # to drastically improve efficiency. 

        subsequence = [nums[0]]

        for i in range(1, len(nums)):

            if nums[i]>subsequence[-1]:
                subsequence.append(nums[i])

            else:
                # perform a binary search on the current
                # subsequence to find the smallest element
                # greater than or equal to current number
            
                left, right = 0, len(subsequence)-1
                result = right

                while left <= right:
                    mid = (left + right) // 2

                    if subsequence[mid] == nums[i]:
                        result = mid
                        break
                        
                    elif subsequence[mid] > nums[i]:
                        result = mid
                        right = mid - 1
                    
                    else:
                        left = mid + 1
                
                subsequence[result] = nums[i]
        
        return(len(subsequence))

        # Space complexity: O(n) for the subsequence array.
        # Time complexity: outer loop runs O(n) times. Within each
        # iteration, a binary search might be performed, which takes
        # O(logn) time. Therefore the total time complexity is O(nlogn),
        # a significant improvement on approach two.

if __name__ == "__main__":
    my = Solution()
    print(my.lengthOfLIS_DP([10,9,2,5,3,7,101,18]))
    print(my.lengthOfLIS_ISB([10,9,2,5,3,7,101,18]))
    print(my.lengthOfLIS_BinSearch([10,9,2,5,3,7,101,18]))


