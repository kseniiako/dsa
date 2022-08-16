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
    
    def findMin2(self, arr):

        # very clever solution that avoids out-of-bounds errors
        # when start == finish and speeds up checking values 
        # by storing intermediate values in a variable result

        # check for empty array
        if not arr:
            return -1

        # by default, e g if array is one element long,
        # result is at index 0
        start, finish, result = 0, (len(arr) - 1), arr[0]

        while start <= finish:
            if arr[start] < arr[finish]:
                # if at any time the array is monotonously
                # increasing, our result is the min between 
                # pre-saved result and beginning of current 
                # segment of array
                result = min(result, arr[start])
                return result
            
            mid = (start + finish) // 2

            # instead of comparing arr[mid] with the number after it,
            # save value of arr[mid] in result in case it is the target
            # (smallest value)
            result = min(result, arr[mid])

            if arr[mid] >= arr[start]:
                start = mid + 1

            else:
                # we need not worry about missing the target if it is
                # at index mid: any small enough arr[mid] value is 
                # already saved in result, and we don't need 
                # to consider mid in the next iteration
                finish = mid - 1

        return result



if __name__ == "__main__":
    my = Solution()
    print(my.findMin([3,4,5,1,2]))
    print(my.findMin([4,5,6,7,0,1,2]))
    print(my.findMin([11, 13, 15, 17]))

    print(my.findMin2([3,4,5,1,2]))
    print(my.findMin2([4,5,6,7,0,1,2]))
    print(my.findMin2([11, 13, 15, 17]))
    print(my.findMin2([]))
    print(my.findMin2([1]))