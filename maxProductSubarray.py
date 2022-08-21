# Maximum Product Subarray (Leetcode 152)

# Given an interger array nums, find a contiguous non-empty
# subarray within the array that has the largest product, and
# return the product. 

class Solution:
    def maxProduct(self, nums):
        # Cookie-cutter brute-force approach

        max_prod = nums[0]

        # iterate through all numbers in array
        for i in range(len(nums)):
            cur_prod = 1

            # we start the inner loop with i, not i+1,
            # in case i by itself is the biggest substring.
            # An alternative resolution of this edge case would 
            # be initially setting max_prod to max(nums) and
            # cur_prod to current number. Then nested loop could
            # start with i+1. However, we would need + O(n) time to
            # iterate through all the nums and find max. So this
            # implementation is preferred.
            for j in range(i, len(nums)):
                cur_prod *= nums[j]
                max_prod = max(max_prod, cur_prod)
        
        # return maximum product
        return max_prod

        # O(n^2) time complexity for nested loops. O(1) space:
        # the only space allocated is for a constant number of
        # extra variables. 
    
    def maxProdFaster(self, nums):
        # Two things can disrupt our combo chain: zeros 
        # and negative numbers. Zeros reset the combo, you have to
        # start again. Negative numbers can flip the combo chain from
        # largest to smallest number and vice versa. To deal with
        # negative numbers, we have to keep track of both the largest
        # and the smalest product so far.

        cur_min = cur_max = maxProd = nums[0]

        # start iteration with the second element
        # since the first one is the default value of
        # our varuables.
        for x in nums[1:]:
            
            # since we will be changing current value
            # of cur_min and then using it, use a temporary
            # variable
            temp_min = cur_min

            # cur_min is set to min of current number,
            # itself*current number and cur_max*current number
            cur_min = min(x, cur_max*x, cur_min*x)

            # cur_max is set to a max of these three
            cur_max = max(x, temp_min*x, cur_max*x)

            # canonically, output value is updated to hold the max
            # of itself and current max
            maxProd = max(cur_max, maxProd)

        return maxProd

        # O(1) space: space is only allocated for a constant number
        # of extra variables. O(n) time — one pass over the array.

        # Takeaway: think creatively about which intermediate values 
        # you can store in a dynamic programming solution!

    
if __name__ == "__main__":
    my = Solution()
    print(my.maxProduct([2,3,-2,4]))
    print(my.maxProduct([-2,0,-1]))
    print(my.maxProduct([-2]))
    print(my.maxProduct([0, 2]))

    print(my.maxProdFaster([2,3,-2,4]))
    print(my.maxProdFaster([-2,0,-1]))
    print(my.maxProdFaster([-2]))
    print(my.maxProdFaster([0, 2]))
                