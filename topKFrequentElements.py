# Leetcode 347

# Given an integer array nums and an integer k, return
# the k most frequent elements. You may return the answer
# in any order.

import heapq

class Solution:
    def topKFrequent(self, nums, k):
        # a simple solution that uses the built-in
        # heapq module. I manually construct
        # a dictionary to hold the element frequencies,
        # but alternatively this could be done in one line 
        # using the built-in dictionary subclass Counter.

        # trivial case: k=n, all elements in array are unique
        if len(nums) == k:
            return nums
        
        # build a dictionary where keys are unique elements
        # and corresponding values are their frequencies.
        dct = {}
        for x in nums:
            if x not in dct:
                dct[x] = 1
            else:
                dct[x] += 1
        
        # now we pass our dictionary to heapq.nlargest, using
        # values in the dictionary for comparison but returning
        # keys!
        return heapq.nlargest(k, dct.keys(), key = dct.get)

        # Dictionary construction is O(n) time. heapq.nlargest 
        # adds k elements to a heap and then pushes and pops
        # extra elements (N-k) times so that only
        # the k most frequent elements remain in the heap.
        # It can be implemented in O(nlogk) time. (Or we could
        # build up an n-sized heap and pop k largest elements
        # in O(n+klogn) time.) Then we return the heap 
        # (remember that heaps are stored as arrays in heapq).

        # Total time complexity is O(n + nlogk) -> O(nlogk). If
        # n=k, we run an edge case and time complexity is
        # O(1) (just returning input array). Therefore, time
        # complexity is always better than O(nlogn).

        # O(n) extra space for dictionary, O(k) extra space
        # for k-sized heap (O(n) if we took the n-size heap approach).
        # Total space complexity of this algorithm is O(n+k).
    
    def topKFrequentBucketSort(self, nums, k):
        # This is an alternative approach. It uses bucket sort
        # heuristic: that is, it utilizes the idea that in an 
        # array of length n, no unique element can have frequency
        # larger than n.

        # Build a dictionary/counter to store frequency values.
        dct = {}

        # Build a 2D array to store all possible frequency counts.
        # All elements with frequency i will be stored in the (sub)array
        # at index i in the 2D array frequencies.
        frequencies = [[] for _ in range(len(nums)+1)]

        # Populate the dictionary.
        for x in nums:
            dct[x] = 1 + dct.get(x, 0)

        # Populate the frequencies array.
        for x in dct:
            frequencies[dct[x]].append(x)

        # Going from the back of frequencies array (largest
        # frequencies), create a k-sized output.
        output = []
        for i in range(len(frequencies)-1, -1, -1):
            for j in frequencies[i]:
                if len(output) < k:
                    output.append(j)
                else:
                    return output
            
        return output

        # This algorithm runs in O(n) time. O(n) time to create
        # a dictionary + O(n) time to topulate array + O(k) time
        # to extract k elements from array -> total time complexity
        # is O(n).
        
        # It takes up O(n) extra space: O(n) for dictionary and O(n)
        # for array.


if __name__ == "__main__":
    my = Solution()
    print(my.topKFrequent([1,1,1,2,2,3], 2))
    print(my.topKFrequent([1], 1))

    print(my.topKFrequentBucketSort([1,1,1,2,2,3], 2))
    print(my.topKFrequentBucketSort([1], 1))
        


        
