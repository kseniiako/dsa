# A solution of K Closest Points to Origin (Leetcode 973)
# that uses divide and conquer and quickselect to achieve
# O(n) average time complexity. 

# From the article on Leetcode:

# Say we choose some random element x = A[i] and split the array
# into two buckets. One bucket is for all the elements less that x,
# another one is for all the elements greater than or equal to x.
# This is known as quickselecting by pivot x. 

# The idea is that if we quickselect by some pivot, on
# average in linear time we'll reduce the problem to
# a problem of half the size. 

# Let's define a helper function quickSelect(i, j, K) that partially 
# sorts the subarray do that the smallest K elements of this subarray
# occur in the first K positions. 

# First, we quickselect by a random pivot element from the subarray.
# To do this in place, we have two pointers i and j and move these
# pointers to elements that are in the wrong bucked — and then swap
# elements.

# After that, we have two buckets [oi, i] and [i+1, oj], where (oi, oj)
# are the original (i, j) values when calling quickSelect(i, j, K). Say
# the first bucket has 10 items and the second one has 15 items. If we were
# trying to partially sort say K = 5 items, then we only need to partially
# sort the first bucket: quickSelect(oi, i, 5). Otherwise, if we were trying
# to partially sort say K = 17 items, then the first 10 items are already
# partially sorted, and we only need to partially sort the next 7 items:
# quickSelect(i+1, oj, 7).

import random

class Solution:
    def kClosest(self, points, k):
        # we don't need to spend time finding the square root
        # to compute the distance: if all distances are given
        # squared, the relationship between them would still
        # be the same.
        distance = lambda i: points[i][0]**2 + points[i][1]**2

        def quickSelect(i, j, k):
            # partially sort A[i:j+1] so that the first K elements
            # are the K smallest. 

            # edge case: invalid subarray
            if i >= j: return

            # Find random element — a pivot. Put it at ith index. 
            p = random.randint(i, j)
            points[p], points[i] = points[i], points[p]

            # call helper function
            mid = partitionHelper(i, j)

            # define next steps depending on where K lands as a result
            # of running partitionHelper

            if k < mid - i + 1:
                quickSelect(i, mid - 1, k)
            elif k > mid - i + 1:
                quickSelect(mid + 1, j, k - (mid - i + 1))

        def partitionHelper(i, j):
            # Partition by pivot A[i] (remember that we saved pivot as i),
            # return an index mid such that A[i] <= A[mid] <= A[j] for i<mid<j.
            
            # save original i
            oi = i  
            pivot = distance(i)
            i += 1

            while True:
                while i < j and distance(i) < pivot:
                    i += 1
                while i <= j and distance(j) >= pivot:
                    j -= 1
                if i >= j:
                    break
                points[i], points[j] = points[j], points[i]

            points[oi], points[j] = points[j], points[oi]
            return j

        quickSelect(0, len(points)-1, k)
        return points[:k]

        # Space complexity is O(1) since everything is done in place. 
        # Time complexity is O(n) in average case and O(n^2) in the worst
        # case (repeated unfortunate choice of pivot at the very beginning
        # or end of the array).

if __name__ == "__main__":
    my = Solution()
    print(my.kClosest([[1,3],[-2,2]], 1))
    print(my.kClosest([[3,3],[5,-1],[-2,4]], 2))
