# Non-Overlapping Intervals (Leetcode 435)

# Given an array of intervals where intervals[i] = [start_i, end_i],
# return the minimum number of intervals you need to remove to make
# the rest of the intervals non-overlapping.

# Like most intervals problems, this one can be solved with
# a greedy approach. My strategy: first, sort the intervals by start
# time. Then look through the sorted list. Intervals i and i+1 don't
# overlap? Good, add i to the output. Overlap? Add the one that starts
# earlier, and if both start at the same time — the one that ends earlier,
# to the output. Greedily thinking, this will never be a wrong decision.
class Solution:
    def eraseOverlapIntervals(self, intervals):
        sorted_ints = sorted(intervals)
        max_index = len(sorted_ints) - 1
        removals = 0
        if not max_index:
            return removals

        # We know that we must add the first interval in the sorted
        # list following the greedy logic: it starts the earliest.
        previous_added_index = 0
        current_index = 1

        while current_index <= max_index:
            if sorted_ints[previous_added_index][1] <= sorted_ints[current_index][0]:
                previous_added_index, current_index = current_index, current_index + 1
            else:
                removals += 1
                if sorted_ints[previous_added_index][1] > sorted_ints[current_index][1]:
                    previous_added_index = current_index
                current_index += 1

        return removals

if __name__ == "__main__":
    my = Solution()
    print(my.eraseOverlapIntervals([[1,2],[2,3],[3,4],[1,3]]))
    print(my.eraseOverlapIntervals([[1,2],[1,2],[1,2]]))
    print(my.eraseOverlapIntervals([[1,2], [2,3]]))
    print(my.eraseOverlapIntervals([[-52,31],[-73,-26],[82,97],[-65,-11],[-62,-49],
    [95,99],[58,95],[-31,49],[66,98],[-63,2],[30,47],[-40,-26]]))

# Takeaway: it can be very fruitful to first write a function to
# see the output in as much detail as possible (e. g. what the
# output array would look like when all the necessary deletions are 
# performed), and then tweak things so that you get some derivative
# of that output that is requested (i. e. number of deletions). That way,
# it is easier to track what your function is doing.

# Space complexity: O(n) for storing sorted array.
# Time complexity: O(nlogn) for search + O(n) for one pass over
# the array to count deletions. Search dominates -> O(nlogn) is
# the total time complexity.

# Idea (didn't work out for this particular problem, but generally fruitful):
# add sentinel interval(that will 100% not result in a deletion)
# to check last interval comfortably (without going out of bounds).
