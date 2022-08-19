# K Closest Points to Origin (Leetcode 973)

# Given an array of points on a 2D plane [x, y], return
# k closest points to the origin [0, 0].

import heapq
import math

class Solution:
    # Both of these solutions use heap-based priority queues. 

    def kClosest(self, points, k):
        # Naive idea: create an n-heap to store
        # distances to origins and corresponding points.
        # The distances should be the heap keys.
        # Then pop k smallest elements from heap
        # and return corresponding points.

        lst_distances = []

        # Create a list to store (distance, point) tuples.
        # Note that by default, if we pass tuples to heapq methods,
        # they interpret tuples as (key, value) pairs, and the 
        # created heap(s) function as priority queues. (Only if 
        # two keys are the same, values are compared.)
        for i in range(len(points)):
            dst = math.sqrt((points[i][0]**2)+(points[i][1]**2))
            lst_distances.append((dst, points[i]))

        # sort the list to get a min-heap
        heapq.heapify(lst_distances)

        output = []

        # pop n elements out of min-heap
        # and store corresponding points in output array
        for i in range(k):
            output.append(heapq.heappop(lst_distances)[1])
            
        return output

        # O(n) space to store lst_distances.
        # O(n) time to find distance from every point to origin.
        # O(n) time to run heapify (bottom-up heap construction).
        # O(klogn) to get k smallest elements from n-sized heap.

        # Total time complexity: O(2n + klogn)-> O(n+klogn).

    def kClosestFast(self, points, k):
        # Rule of thumb: if we only need k smallest
        # elements from a min-heap, we never need to store
        # more than k elements in a heap. This change
        # drastically improves the time and space complexity
        # of the algorithm (compared to naive approach).

        lst_distances = []

        for i in range(len(points)):

            distance = math.sqrt((points[i][0]**2)+(points[i][1]**2))

            # Our objective is to find and store n smallest values in a
            # stream of values. heapq module provides a minheap and a 
            # function heappushpop to push a new value onto the heap 
            # and pop out smallest value out of the heap. But we don't want
            # to push smallest values out of the heap: we want to keep k
            # smallest values and push out larger ones. With these "inputs",
            # it makes sense to invert the distance values (keys in the heap)
            # so that our heap effectively functions as a max-heap.

            # if heap has not reached its max size yet, push
            # current element (distance should be inverted)
            if i < k:
                heapq.heappush(lst_distances, (-distance, points[i]))

            # if heap has reached its max size, push the new value
            # onto it and pop the largest value out (smallest -distance)
            else:
                heapq.heappushpop(lst_distances, (-distance, points[i]))
        
        # return points corresponding to each element in the heap
        return [elem[1] for elem in lst_distances]

        # O(nlogk) time to repeatedly add elements to the heap.
        # O(n) to iterate through final list and extract points. 
        # Total time complexity is O(n+nlogk), which can be an
        # asymptotic improvement over the previous algorithm 
        # depending on values n and k.

        # O(k) extra space for k-size heap.
    
    def kClosest3(self, points, k):
        # Same logic as in the previous solution, however,
        # we store the n-k largest-distance elements in the stream
        # on a (n-k) sized heap (instead of storing k smallest-distance
        # elements on a k-sized heap). This way, we avoid the need to
        # invert the sign on distance to transform min-heap into max-heap
        # (min-heap is just what is needed for this approach). Moreover,
        # we can immediately append points with smallest values to output 
        # as we pop them out and avoid he extra O(n) time overhead of 
        # constructing the output array.

        lst_distances = []
        largest_count = len(points)-k

        output = []

        for i in range(len(points)):

            distance = math.sqrt((points[i][0]**2)+(points[i][1]**2))

            if i < largest_count:
                heapq.heappush(lst_distances, (distance, points[i]))

            else:
                output.append(heapq.heappushpop(lst_distances, (distance, points[i]))[1])

        return output

        # O(nlog(n-k)) to repeatedly push or push-pop n items
        # onto/from a (n-k)-sized heap. Since output array
        # is constructed while we are pushing-popping items (out
        # of popped items), there is no extra time needed for that.
        # Total time complexity is O(nlog(n-k)). + We gain some constant 
        # speed-up in comparison to solution 2 since we don't have to 
        # invert every distance value.

        # Space complexity is O(n-k) to store the heap.


if __name__ == "__main__":
    my = Solution()

    print(my.kClosest([[1,3],[-2,2]], 1))
    print(my.kClosest([[3,3],[5,-1],[-2,4]], 2))

    print(my.kClosestFast([[1,3],[-2,2]], 1))
    print(my.kClosestFast([[3,3],[5,-1],[-2,4]], 2))

    print(my.kClosest3([[1,3],[-2,2]], 1))
    print(my.kClosest3([[3,3],[5,-1],[-2,4]], 2))