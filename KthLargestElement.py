# Kth Largest Element in a Stream (Leetcode 703)

# Design a class to find the kth largest element in
# a stream.

import heapq

class KthLargest:
    # I am using the heap data structure (provided in 
    # the module heapq) and the method heapq.nlargest
    # in order to retrieve the n largest elements from 
    # the heap.

    # Trick: a stream is a particular beast. As we are 
    # repeatedly looking for a kth largest number in a stream,
    # and as no numbers ever get removed from the stream, it is
    # enough to only store k largest elements that have been added
    # to the stream so far. It is not necessary to store the (k+1)th
    # etc elements -> they will never be the largest. Storing
    # (and sorting through) all the elements we've encountered
    # so far is a waste of time and space!

    def __init__(self, k, nums):
        # initializes the object with integer k
        # and stream nums

        # note that the heapify method creates a min heap
        # in place.
        heapq.heapify(nums)
        self.heap = nums
        self.k = k
        self.minimize()

    def minimize(self):
        # Helper function:
        # We need a k-sized heap -> pop out all the extra 
        # values so that only k largest values remain
        while len(self.heap) > self.k:
            heapq.heappop(self.heap)
    
    def add(self, val):
        # appends the integer val to the stream and
        # returns the kth largest element in the stream

        # we push the new value onto the stream and bring
        # the stream back to k elements.
        heapq.heappush(self.heap, val)
        self.minimize()

        # return the smallest element on the heap.
        # Our minheap is stored in memory as a list, so we
        # can just retrieve the first element in the list.
        return self.heap[0]

    # O(k) space complexity: we hold a k-sized heap in memory.

    # Time complexity of __init__: O(nlogn)
    # O(n) time complexity for heap creation (heapify). O(logn)
    # for each of (n-k) calls to minimize. Total time complexity of
    # __init__ is therefore O(n+((n-k)logn)) = O((n-k)logn) = O(nlogn)

    # Time complexity of add: O(log k)
    # O(logk) time complexity for pushing an element onto a k-sized heap + 
    # O(logk) time complexity for the subsequent call to minimize
    # (one pop from a k-sized heap). O(1) time complexity for retrieving
    # 0th index of an array. Total time complexity: O(log k)

    # Note: we can't use heappushpop in add implementation since
    # it is possible that current heap has fewer than k elements
    # and we shouldn't delete anything.

if __name__ == "__main__":

    my = KthLargest(3, [4,5,8,2])
    print(my.add(3))
    print(my.add(5))
    print(my.add(10))
    print(my.add(9))
    print(my.add(4))
