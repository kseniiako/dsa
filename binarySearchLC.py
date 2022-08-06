# Binary search binary search binary search!
# (LC 704)

# Given an array of integers nums which is sorted in ascending order
# (all the integers in the array are unique), and an integer target,
# write a function to search target in nums. If target exists, return 
# its index. Otherwise, return -1. 

# Write an algorithm with O(lon n) time complexity. 

class Solution():
    def search(self, nums, target):
        def searchHelper(arr, target, start, finish):

            mid = (start + finish) // 2
            
            if start <= finish:
                
                if arr[mid] == target:
                    return mid
                elif arr[mid] > target:
                    return searchHelper(arr, target, start, mid-1)
                elif arr[mid] < target:
                    return searchHelper(arr, target, mid + 1, finish)
                
            return -1
        
        return searchHelper(nums, target, 0, (len(nums) - 1))

    def searchIterative(self, nums, target):

        start = 0
        finish = len(nums) - 1

        while start <= finish:

            mid = (start + finish) // 2

            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                start = mid + 1
            elif nums[mid] > target:
                finish = mid - 1

        return -1 

        
        
my = Solution()
#import pdb; pdb.set_trace()
print(my.search([-1,0,3,5,9,12], 2))
print(my.searchIterative([-1,0,3,5,9,12], 2))
print(my.searchIterative([-1,0,3,5,9,12], 9))

# Takeaway: distinguish between for an while loops! If you have
# recurion, you likely don't need that while, you need a simple
# if test condition. The multiple execution of a loop would be accomplished
# anyways via recursion.

# O(log n) time complexity for sorted list (O(n) otherwise —
# if we were just looking for a number in an unsorted list.
# O(1) space complexity for iterative solution.
# For recursive solution, O(log n) space complexity due to stack use. 

