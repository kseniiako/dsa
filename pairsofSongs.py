# Pairs of Songs with Total Duration Divisible by 60 (Leetcode 1010)

# You are given a list of songs where the ith song has a duration of
# time[i] seconds. Return the number of pairs of songs for which their
# total duration in seconds is divisible by 60. Formally, we want the 
# number of indices i, j such that i < j with (time[i] + time[j]) % 60
# == 0.

# This problem is a cookie-cutter representative of
# the "throw in a hashmap" variety. Since the hashmap
# here may contain all numbers in a given constant range,
# it is convenient to use an array for it. This function needs
# constant space (we only need O(60) space to store the aforementioned 
# array-based hashmap, no matter how large the input is) and O(n)
# time (to iterate through every element in the input array).

class Solution:
    def numPairsDivisibleBy60(self, time: List[int]) -> int:
        time_arr = [0]*60
        output = 0
        for x in time:
            if not x % 60:
                output += time_arr[0]
            else:
                output += time_arr[60 - (x%60)]

            time_arr[mod(x, 60)] += 1
     
        return output