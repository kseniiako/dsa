# Meeting Rooms II (Leetcode 253)

# Given an array of meeting time intervals [start, end],
# return the minimum number of conference rooms required.

import heapq

class Solution:
    def minMeetingRooms(self, intervals):
        # First, we sort the meeting intervals by start time. Then
        # we iterate through the sorted list, and if there is overlap,
        # we allocate an extra room. Now, how to efficiently check for 
        # overlap over multiple rooms?

        # We can make use of a min-heap to store the end times of
        # meetings in various rooms. Every time we want to check
        # if a room is free or not, we should check the topmost
        # element of the min-heap: this room would be free the earliest.
        # If the topmost room is not free at a given time, no room is free,
        # and we should allocate a new room.

        # (Unlike Meeting Rooms I, we do not have to check for overlap
        # using the sorted array in this problem: this would be extraneous
        # since we check for overlap when we compare current item's start 
        # time with the soonest end time in the heap (the topmost element).

        # Remember to update the heap (replace the current lowest end time
        # with the end time of the latest meeting you iterated through in
        # the array) whether or not a new room has to be allocated!

        # helper function to pass to the sorting algorithm as key.
        def helper(x):
            return x[0]

        ints_sorted = sorted(intervals, key = helper)

        room_count = 0
        if not ints_sorted:
            return room_count

        # add room for first meeting
        room_count += 1
        room_heap = [ints_sorted[0][1]]

        # iterate through the rest of the meetings. Each time we either
        # add a new room with a new end time, or replace the current soonest
        # end time with a new end time (i. e. we hold the next meeting in 
        # the room that was available the earliest).
        for i in range(1, len(ints_sorted)):
            if room_heap[0]>ints_sorted[i][0]:
                room_count += 1
                heapq.heappush(room_heap, ints_sorted[i][1])
            else:
                heapq.heapreplace(room_heap, ints_sorted[i][1])

        return room_count


if __name__ == "__main__":
    my = Solution()
    print(my.minMeetingRooms([[0,30],[5,10],[15,20]]))
    print(my.minMeetingRooms([[7,10],[2,4]]))
    print(my.minMeetingRooms([[1,5],[8,9],[8,9]]))