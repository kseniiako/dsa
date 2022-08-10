# Leetcode 33
# There is an integer array nums sorted in ascending order
# (all values are distinct). Prior to being passed to this 
# function, the array is possibly rotated. Given the array
# after the possible rotation and an integer target, return
# index of target if it is in array, or -1 if it is not.

# Write an algorithm with O(log n) time complexity.

class Solution:
    def search(self, arr, target):
        # first solution: two passes of binary search
        
        # step 1: use binary search to locate the smallest
        # element in the array.
        # the smallest element is the place of the wraparound. 
        # condition: iff arr[n] > arr[n+1], arr[n+1] is the
        # smallest element in the array. 
        # we choose the number n to be the middle of the current array.
        # if for a number n we check for the condition above, and it is not 
        # satisfied, we next choose the correct half of the array to look for the
        # smallest element. That is, if arr[start] < arr[n], wraparound
        # happens after element n -> we need to search second half of array, indices
        # after n. If arr[start] > arr[n], wraparound happens in the first half of the array,
        # at an index before n or n.
        # We repeat this search recursively, each time halving the search space.

        # handle trivial case: empty array
        if len(arr) == 0:
            return -1

        start, finish = 0, (len(arr)-1)

        # handle trivial case: 1 element in array
        if start == finish:
            if arr[0] == target:
                return 0
            else:
                return -1

        smallest_index = -1 # -1 is dummy value for non-found smalles_index.

        while (start<finish) and (smallest_index == -1):
            mid = (start + finish) // 2
            if arr[mid] > arr[mid+1]:
                smallest_index = mid+1
            elif arr[start] >= arr[mid]:
                finish = mid
            elif arr[start] < arr[mid]:
                start = mid+1
        
        if start == finish:
            # this case means array has no wrap around!
            smallest_index = 0

        print("Smallest index: "+str(smallest_index))
        
        # reset start, finish for second run of binary search.
        start, finish = 0, (len(arr)-1)

        # choose the half of the array to look for the target in 
        # (we skip this step search the whole array if no wrap around)
        if start != smallest_index:
            if target >= arr[start]:
                finish = smallest_index - 1
            else:
                start = smallest_index

        while start <= finish:
            mid = (start + finish) // 2
            if arr[mid] == target:
                return mid
            if arr[mid] < target:
                start = mid+1
            else:
                finish = mid-1
        
        return -1

        # Two consecutive binary sorts, each takes O(log n) time ->
        # this solution runs in O(log n) time.

        # Only a constant number of extra variable used -> space
        # complexity is O(1). 

    def searchOnePass(self, arr, target):
        # challenge: try to rewrite this algorithm so that
        # it only performs binary search once.

        # Heuristic: run binary search, finding a midpoint in every
        # iteration of the search loop. If arr[mid] == target, return mid.
        # If not, there are two cases.
        # Case 1: arr[mid] < arr[start], wraparound happens between start
        # and mid. In the next interation we search the left part 
        # of the list if target > arr[mid] or target < arr[start]. 
        # Otherherwise (if arr[start] > target > arr[mid]), we search
        # the right part.
        # Case 2: arr[mid] > arr[start], wraparound happens between mid and end.
        # In the next iteration we search the left part of the list if
        # arr[start] < target < arr[mid]. Otherwise (if target < arr[start] or
        # target > arr[mid]), we search the right part.

        start, finish = 0, (len(arr) - 1)
        while start <= finish:
            mid = (start + finish) // 2
            if arr[mid] == target:
                return mid
            if arr[mid] < arr[start]:
                if arr[start] > target and arr[mid] < target:
                    start = mid + 1
                else:
                    finish = mid - 1
            else:
                if arr[start] <= target and arr[mid] > target:
                    finish = mid - 1
                else:
                    start = mid + 1

        return -1

        # Binary search runs in O(log n) time ->
        # this algorithm has time complexity O(log n)

        # Space complexity is O(1) since we only create a constant
        # number of new variables.


# Tests!
if __name__ == "__main__":
    arr1 = [4,5,6,7,0,1,2]
    arr2 = [1]
    arr3 = [1, 3]
    my = Solution()
    print(my.search(arr1, 0))
    print(my.search(arr1, 7))
    print(my.search(arr1, 1))
    print(my.search(arr1, 2))
    print(my.search(arr2, 0))

    print(my.search(arr3, 0))
    print(my.search(arr3, 1))
    print(my.search(arr3, 3))

    print(my.searchOnePass(arr1, 0))
    print(my.searchOnePass(arr1, 7))
    print(my.searchOnePass(arr1, 1))
    print(my.searchOnePass(arr1, 2))
    print(my.searchOnePass(arr2, 0))

    print(my.searchOnePass(arr3, 0))
    print(my.searchOnePass(arr3, 1))
    print(my.searchOnePass(arr3, 3))

                    
                    
            



