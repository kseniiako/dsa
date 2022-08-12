# Find minimum in rotated sorted array. (LC 153)
# This algorithm uses binary search

# Note: all elements in this array are unique!

class Solution:
    def findMin(self, arr):
        left = 0
        right = len(arr) - 1

        while left < right:

            mid = (left + right) // 2
            
            if arr[mid] > arr[mid+1]:
                return arr[mid+1]
            
            # technically we don't need to check for
            # equality, as all elements of array are
            # supposed to be unique. However, this is a
            # guard against bad input.

            if arr[mid] >= arr[left]:
                left = mid + 1
            
            elif arr[mid] < arr[left]:
                right = mid

        # output not found! This means that array is
        # not rotated (or rotated n times where n is its length,
        # coming full circle)
        return arr[0]

if __name__ == "__main__":
    my = Solution()
    print(my.findMin([3,4,5,1,2]))
    print(my.findMin([4,5,6,7,0,1,2]))
    print(my.findMin([11, 13, 15, 17]))