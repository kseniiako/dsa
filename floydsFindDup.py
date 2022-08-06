# solving find duplicate using Floyd's cycle-finding algorithm!
# say we have a pointer traveling thru the array arr, where at each step
# the pointer at value x goes to arr[x]. If we had no repeating numbers in
# the array, we would have one number whose value is out of bounds for
# the array (since array indexing starts with zero, and array numbers
# start with one). However, if there is a repeated number, we would run into
# a loop with that number. Then we use Floyd's algorithm to find the beginning
# of the cycle in order to find the necessary number.

class Solution:
    def floydsFindDup(self, arr):
        if len(arr) < 1:
            # Invalid input
            return -1

        slow = arr[0]
        fast = arr[arr[0]]

        while slow != fast:
            
            slow = arr[slow]
            fast = arr[arr[fast]]

        slow = 0

        while slow != fast:

            slow = arr[slow]
            fast = arr[fast]

        return slow

arr = [4,3,1,4,2]
my = Solution()
print(my.floydsFindDup(arr))
