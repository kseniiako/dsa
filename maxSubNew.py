import math

class Solution:
    def maxSubArray(self, nums):
        # optimized brute force approach: runs in O(n^2)
        max_subarray = -math.inf
        for i in range(len(nums)):
            # for each new starting point, you start from scratch
            cur_subarray = 0
            for j in range(i, len(nums)):
                # add new consequtive number to current subarray
                cur_subarray += nums[j]
                # and update max_subarray to max of itself and current
                max_subarray = max(cur_subarray, max_subarray)
        return max_subarray

    def Kadanes(self, nums):
        # Kadanes algorithm: based on the idea that no 
        # subarray that, when its sum is added to the current number,
        # brings down the value of a current number is worth keeping.
        # So no subarray with negative value is worth keeping. What this means
        # is that if there are some positive numbers in the array,
        # then the output will be a positive subarray (of length
        # 1 or more), and if all numbers in the array are negative,
        # then the output will be one number: the closest to 0 (the lesser evil)
        # in the array.
        # Remark: if all are positive, we'll just return the whole array.
        if len(nums) > 0:
            max_subarray = cur_subarray = nums[0]
        else:
            print("""Please input a non-empty list: empty output is not allowed for this problem""")
            return []

        for num in nums[1:]:
            # cur_subarray is evaluated to the the max of current number 
            # or current subarray + current number
            cur_subarray = max(num, cur_subarray + num)
            # max_subarray keeps the largest of all past current subarrays
            max_subarray = max(max_subarray, cur_subarray)

        return max_subarray

    def KadanesWNuns(self, nums):
        # this is a classical implementation which allows to
        # have an empty array be the result
        max_subarray = cur_subarray = 0
        for num in nums:
            cur_subarray = max(num, cur_subarray+num)
            max_subarray = max(max_subarray, cur_subarray)
            
        return max_subarray
    
    def DivandConq(self, nums):
        #divide and conquer approach!
        def bestMidSum(nums, left, right):
            if left > right:
                return -math.inf
            
            if left == right:
                return nums[left]

            mid = (right + left) //2

            cur_right = max_right = 0
            for num in nums[mid+1:right+1]:
                cur_right += num
                max_right = max(cur_right, max_right)
            
            cur_left = max_left = 0
            for num in range(mid-1, left-1, -1):
                cur_left += nums[num]
                max_left = max(cur_left, max_left)

            best_mid = max_left + max_right + nums[mid]

            best_left = bestMidSum(nums, left, mid-1)
            best_right = bestMidSum(nums, mid+1, right)

            best_overall = max(best_mid, best_left, best_right)
            return best_overall

        return bestMidSum(nums, 0, len(nums)-1)
        # Time complexity: O(n log n) -> iterate through all n
        # elements in a list when looking for best subarray spanning
        # the middle. Plus we have log n calls to do this because
        # we recursively perform the helper function on each half of the
        # array. 

    def printAllSubarrays(self, nums):
        # this is a brute-force O(n^3) function that finds all
        # subarrays
        if len(nums) == 0:
            print("Empty input array: no subarrays!")

        for i in range(len(nums)):
            for j in range(i+1, len(nums)+1):
                for k in nums[i : j]:
                    print(k, end = " ")
                print("")
                    

            



    


my = Solution()
#import pdb; pdb.set_trace()
print(my.maxSubArray([-2,1,-3,4,-1,2,1,-5,4]))
print(my.Kadanes([-2,-1,-3,-4,-1,-2,-1,-5,-4]))
print(my.KadanesWNuns([-2,1,-3,4,-1,2,1,-5,4]))
# The way python's lists work allows me to safely use nums[1:] (even if
# index 1 does not exist, given a list of just one element). However,
# while KadanesWNuns does not demand nums[0] in the beginning and runs
# smoothly with empty input (later avoiding entering the loop "for num
# in nums", because there is nothing in nums), Kadanes starts from nums[0]
# and so we need to catch the error that happens on empty input.
print(my.Kadanes([]))

#import pdb; pdb.set_trace()
print(my.DivandConq([0, 1, 2, 3, 4, 5]))
print(my.DivandConq([-2,1,-3,4,-1,2,1,-5,4]))
print(my.DivandConq([-2,-1,-3,-4,-1,-2,-1,-5,-4]))
print(my.DivandConq([1]))

print("Find all subarrays")
my.printAllSubarrays([1, 2, 3, 4, 5])
my.printAllSubarrays([-15])
my.printAllSubarrays([-15, 3])
my.printAllSubarrays([])
my.printAllSubarrays([17, 3, 29, 100])