# Insert Interval (Leetcode 57)

# You are given an array of non-overlapping intervals
# where intervals[i] = [start, end]. You are also given an
# new interval. Insert new interval into intervals such that
# intervals is still sorted in ascending order, and there are
# no overlapping intervals (merge overlapping intervals if
# necessary). Return array after insertion.

class Solution:
    def insert(self, intervals, new):
        
        # edge case: input array is empty
        if not intervals:
            return [new]

        output = []
        # iterate over the list of intervals
        for i in range(len(intervals)):

            # if current element comes strictly before
            # the new one, append it to output
            if intervals[i][1] < new[0]:
                output.append(intervals[i])
            
            # else if current element comes strictly after
            # the new one, add the new element and all remaining
            # elements to output and return
            elif intervals[i][0] > new[1]:
                output.append(new)
                return output + intervals[i:]

            # if current element is overlapping with the new one,
            # update new to hold the merged interval
            else:
                new = [min(intervals[i][0], new[0]), \
                max(intervals[i][1], new[1])]

        # if we have not returned from within the loop, this 
        # means new needs to be appended to the output (i. e. 
        # there was only one element in input array and new 
        # overlapped with it).
        output.append(new)
        return output

        # O(n) time (one pass over the array). O(1) space (we only
        # update the variable that holds new interval, no variables
        # are created except the array necessary to hold output).

if __name__ == "__main__":
    my = Solution()
    print(my.insert([[1,3], [6,9]], [2,5]))
    print(my.insert([[1,2],[3,5],[6,7],[8,10],[12,16]], [4,8]))
    print(my.insert([[1,5]], [2,3]))





        
            
