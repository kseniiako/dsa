# solution to find duplicate (LC 287) using
# bitwise operations

class Solution:
    def Bitwise(self, arr):
       bin_length = len(bin(len(arr)-1)[2:])

        # default invalid output (0 is never in range and so
        # is never in the input array)
       output = 0
       
       for offset in range(bin_length):

           mask = 1 << offset

           count_range = count_actual = 0
           
           # update count for the range
           for x in range(1, len(arr)):
               if x & mask:
                   count_range += 1

           # update count for the actual array
           for x in arr:
               if x & mask:
                   count_actual += 1
                   
           if count_actual > count_range:
                output |= mask

       return output
           
           


arr = [1, 8, 2, 3, 4, 5, 6, 7, 8]
my = Solution()
print(my.Bitwise(arr))

# Very fun and elegant algorithm! But how long does it take to run?
# Well, outer loop runs in bin length m, and two inner loops run in
# O(n+1). We also know that m is (log n) + 1. So we get an algorithm that
# runs in O(n log n) time — linearithmic time complexity. 
# Constant space — only constant number of extra variables.

