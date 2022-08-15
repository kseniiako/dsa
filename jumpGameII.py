# Jump Game II (Leetcode 45)

# Given an array of non-negative integers nums, you are
# initially positioned at the first index of the array. 
# Each element in the array represents your maximum jump at
# that position. Your goal is to reach the last index in
# the minimum number of jumps.

# You can assume that you can always reach the last index.

class Solution:
    def jump(self, arr):
        # While this problem could be solved with dynamic programming
        # in O(2**n) time, it can also be solved in O(n) with a greedy
        # approach. This greedy algorithm uses a form of breadth-first
        # search on a one-dimensional array where each "level" of the array
        # are the destinations that are avaiable to us after the same
        # number of jumps: i. e. after one jump, after two jumps, etc.

        # Note that this solution benefits from the assumption that we can
        # always reach the last index. If this function is run on an input
        # that makes you stuck on a 0 position (e. g. [1,0,1]), it will
        # loop indefinitely since max_destination stays the same in
        # consecutive loop iterations (and max_destination is assigned to 
        # right in the end of each iteration).
        
        output = 0
        left = right = 0

        # Once right reaches last index, this means that we can
        # reach end last index on current level -> we've already
        # made the minimum necessary number of jumps to traverse
        # the array.
        while right < len(arr) - 1:

            max_destination = 0

            # Find the max breadth/furthest boundary of the
            # next level by updating max_destination to be
            # the max of max_destinations for jumps from every
            # position in the current level's range.
            for j in range(left, right+1):
                max_destination = max(max_destination, j+arr[j])

            # Now set the boundaries for next level. Right is 
            # max_destination, whereas left is current right boundary + 1.
            # Notice how these assignments depend on our assumption that
            # progress through the array is possible on each level (i. e. it
            # is not erroneous to update next level's left to be bigger than current
            # level's right each time).
            left = right+1
            right = max_destination

            output += 1
        
        return output

            

if __name__ == "__main__":

    my = Solution()
    print(my.jump([2,3,1,1,4]))
    print(my.jump([2,3,0,1,4]))
    print(my.jump([1]))
    print(my.jump([1,2,3]))
    print(my.jump([1,2,1,1,1]))
    print(my.jump([2,3,1]))

    # Warning: running self.jump with the following input
    # causes the program to loop indefinitely.
    #print(my.jump([1,0,1,0]))



            