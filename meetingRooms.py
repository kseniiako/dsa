# Meeting Rooms (Leetcode 252)

# Given an array of meeting time intervals [start, end],
# determine if a person could attend all meetings.

class Solution:
    def canAttendMeetings(self, intervals):
        # First let's sort all meetings by the
        # beginning time (increasing)
        
        # This is the function that we pass as key
        # to sorting algorithm
        def helper(arr):
            return arr[0]

        # I use sorted instead of sort to avoid modifying
        # the original list
        ints_sorted = sorted(intervals, key = helper)

        # Now that meetings are sorted by start time,
        # check that no two meetings overlap: that is,
        # that every meeting finishes by the time the
        # next one begins.
        for i in range(len(ints_sorted)-1):
            if ints_sorted[i][1] > ints_sorted[i+1][0]:
                return False

        return True

if __name__ == "__main__":
    my = Solution()
    print(my.canAttendMeetings([[0,30],[5,10],[15,20]]))
    print(my.canAttendMeetings([[7,10],[2,4]]))

