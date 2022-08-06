import math

class Solution:
    def generateAllSubarr(self, arr, length):
        # given an array, generate (brute-force — how else, I ask!)
        # all possible subarrays to print them

        # pick start point
        for i in range(0, length):

            # pick end point
            for j in range(i, length):

                # print subarray between current starting
                # and ending points
                for k in range(i, j+1):
                    print (arr[k], end=" ")

                print ("\n", end = "")
            
    def maxSubArray0(self, nums: list[int]) -> int:
        # this is a slightly optimized brute force
        # solution. 
        # we need to caclulate the sum of all subarrays
        # and keep the best one. We can change the time complexity
        # from O(n^3) to O(n^2) by recognizing that
        # all subarrays starting at particular value
        # share a prefix.
        max_subarray = -math.inf

        # from each starting pt create a variable current_subarray = 0
        # then, loop thru the array from the starting index, adding each element
        # to current_subarray. every time we add an element, it represents
        # a possible subarray! so continuously update max_subarray
        # to contain the maximum of current_subarray and itself. 
        for i in range(len(nums)):
            current_subarray = 0
            for j in range(i, len(nums)):
                current_subarray += nums[j]
                max_subarray = max(max_subarray, current_subarray)

        return max_subarray

    def Kadanes(self, nums: list[int]) -> int:
        # dynamic programming algorithm to help us figure out
        # which negative numbers are "worth" keeping in the subarray. 
        # (all positive numbers are obvi worth it). very greedy 
        # intuition behind this algorithm. 

        # Initialize max and current variables to the first element
        current_subarray = max_subarray = nums[0]

        # start sith the 2nd element since we already used
        # the first one. 

        for num in nums[1:]:

            # if current subarray is negative, throw it away!
            # otherwise, keep adding to it. 
            current_subarray = max(num, current_subarray + num)
            max_subarray = max(max_subarray, current_subarray)

        return max_subarray

        # here time complexity is O(n), and space complexity is
        # O(1) (we're only using two variables current and max)
    
    def DivandConq(self, nums: list[int]) -> int:
        # slower than Kadanes and uses more space: but still
        # a fun way to think about this problem differently. 

        # basically, our answer is the largest of:
        # 1) max subarray contained on the left side
        # 2) max subarray contained on the right side
        # 3) max subarray thar uses both sides' elements
        def findBestSubarray(nums, left, right):
            # Base case — empty array
            if left > right:
                return - math.inf
            
            mid = (left + right) // 2
            curr = best_left_sum = best_right_sum = 0

            # Iterate over the left side
            for i in range(mid - 1, left - 1, -1):
                curr += nums[i]
                best_left_sum = max(best_left_sum, curr)

            # Reset curr and iterate over the right side
            curr = 0
            for i in range(mid+1, right+1):
                curr += nums[i]
                best_right_sum = max(best_right_sum, curr)

            # The best combined sum uses the middle element and
            # the best possible sum from each half. 
            best_combined_sum = nums[mid] + best_left_sum + best_right_sum

            # Find the best subarray possible from both halves
            left_half = findBestSubarray(nums, left, mid-1)
            right_half = findBestSubarray(nums, mid+1, right)

            return max(best_combined_sum, left_half, right_half)

        # Now calling this helper funcion on our entire input!
        return findBestSubarray(nums, 0, len(nums) - 1)

        # Time complexity here is O(nlogn), where n is length
        # of nums. We handle n elements over log n cycles
        # (an array can be recursively split in half -> half of half etc
        # logn times)

        # Space complexity: O(log n).
        # The extra space we use relative to input size is solely
        #occupied by the recursion stack. Each time the
        # array gets split in half, another call
        # of findBestSubarray will be added to the recursion stack
        # until calls start to get resolved by the base case
        # (base case happens at empty arrays, after log n calls)



        


my = Solution()
print(my.maxSubArray0(nums = [-2,1,-3,4,-1,2,1,-5,4]))
print(my.Kadanes(nums = [-2,1,-3,4,-1,2,1,-5,4]))
print(my.DivandConq(nums = [-2,1,-3,4,-1,2,1,-5,4]))
my.generateAllSubarr([0, 1, 2, 3, 4, 5], 6)