# Merge Intervals (Leetcode 56)

# Given an array of intervals where intervals[i] -
# [start, end], merge all overlapping intervals,
# and return an array of non-overlapping intervals
# that cover all the intervals in the input.

class Solution:
    def merge(self, ints):
        # Naive and very slow approach (O(n^2) runtime).
        ints_sorted = sorted(ints)
        output = []

        i = 0

        while i < len(ints_sorted):
            offset = 1
            for j in range(i+1, len(ints_sorted)):
                if ints_sorted[j][0]<=ints_sorted[i][1]:
                    ints_sorted[i][1] = max(ints_sorted[i][1],
                    ints_sorted[j][1])
                    offset += 1
            output.append(ints_sorted[i])
            i += offset

        return output

        # Space complexity is O(n) to hold the reversed array 
        # (since we're not sorting in place).

        # O(nlogn) time complexity to sort the input array.
        # O(n^2) time complexity to look through the whole array
        # using two nested loops.
        # Total time complexity is O(n^2+nlogn) = O(n^2).

    def mergeFast(self, ints):
        # This is an attempt at a faster solution. The previous
        # solution goes into an O(n^2) nested loop. However,
        # since intervals are already sorted by start time at the
        # first step of our algorithm, once we hit the first 
        # non-overlapping interval I, we should stop looking
        # for overlaps with any previous intervals (there is nothing
        # to be found) and proceed to look for overlaps with I in the
        # [index(I)+1:] slice of the array. That way, we can reduce 
        # time complexity from O(n^2) to O(n) for the loop.


        if not ints:
            return []
        # sort array by start time (default sorting option,
        # so we need not provide a key function)
        ints_sorted = sorted(ints)

        # initialize output to first element
        output = [ints_sorted[0]]
        
        # now iterate through the whole array
        for i in range(len(ints_sorted)):
            # perform merging
            if output[-1][1] >= ints_sorted[i][0]:
                output[-1][1] = max(output[-1][1], ints_sorted[i][1])
            
            # or append a non-overlapping element to output array
            else:
                output.append(ints_sorted[i])
        
        return output
        
        # Time complexity O(nlogn) for sorting, O(n) for the loop
        # (iterating through the array and merging). Total time
        # complexity is O(nlogn) (dominated by sorting).

        # Space complexity is O(n) to store sorted array.

    def mergeImproved(self, ints):
        # Small tweaks to first (naive) algorithm to make the nested
        # loop run in linear time and thus improve efficiency.
        ints_sorted = sorted(ints)
        output = []

        i = 0

        while i < len(ints_sorted):
            offset = 1
            for j in range(i+1, len(ints_sorted)):
                if ints_sorted[j][0]<=ints_sorted[i][1]:
                    ints_sorted[i][1] = max(ints_sorted[i][1],
                    ints_sorted[j][1])
                    offset += 1
                # escape loop if we've gone through all possible
                # overlaps
                else:
                    break

            # append merged interval
            output.append(ints_sorted[i])

            i += offset

        return output

        # O(nlogn) for sorting + O(n) for loop -> O(nlogn) time compexity.
        # O(n) space complexity to store sorted array.


if __name__ == "__main__":
    my = Solution()
    print(my.merge([[1,3],[2,6],[8,10],[15,18]]))
    print(my.merge([[1,4],[4,5]]))
    print(my.merge([]))

    print(my.mergeFast([[1,3],[2,6],[8,10],[15,18]]))
    print(my.mergeFast([[1,4],[4,5]]))
    print(my.mergeFast([]))

    print(my.mergeImproved([[1,3],[2,6],[8,10],[15,18]]))
    print(my.mergeImproved([[1,4],[4,5]]))
    print(my.mergeImproved([]))