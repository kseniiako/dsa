# Jump Game! (LC 55)

# You are given an integer array nums. You are initially
# positioned at the first index of the array, and each
# element in the array represents your maximum jump length at that
# position. 

# Return true if you can reach the last index, and false otherwise.

# Length of input array is between 1 and 10**4
class Solution:
    def canJump(self, arr):
        # Using a greedy approach
        destination = len(arr)-1

        # starting with the destination itself (to
        # account for single-element arrays), iterate backwards
        # over the array.
        for x in range(len(arr)-1, -1, -1):
            # we will shift the goalpost of destination
            # to ith node if we know for sure that we can reach
            # the destination if starting from ith node.

            if x+arr[x] >= destination:
                destination = x

        # If destination has shifted to 0, this means we can traverse
        # the whole array by jumping. Return True. Otherwise, return false.
        return destination == 0

if __name__ == "__main__":
    my = Solution()

    print(my.canJump([2,3,1,1,4]))
    print(my.canJump([5,0,0,0,0,0,0,0,0]))
    print(my.canJump([3,2,1,0,4]))