# Two sum II: input array is sorted. 

# Given a 1-indexed array of integers numbers that is
# already sorted in a non-decreasing order, find two
# numbers such that they add up to a specific target number. 
# Let these two numbers be numbers[ind1] and numbers[ind2] where
# 1 <= ind1 < ind2 <= len(numbers)

# Return [ind1+1, ind2+1]

class Solution:
    def twoSum(self, arr, target):
        dct = {}
        for x in range(len(arr)):
            if arr[x] in dct:
                return [dct[arr[x]]+ 1, x+1]
            else:
                dct[target - arr[x]] = x
        return [-1, -1]
    
    def twoSumII(self, arr, target):
        # the previous solution uses the classic two sum
        # approach. However, it does not take advantage
        # of the fact that array is sorted!

        # We can use two pointers to come up with a O(n)
        # time, O(1) space solution (better than the previous
        # one, which is O(n) time, O(n) space).

        start = 0
        end = len(arr) - 1

        while start < end:
            cur =  arr[start] + arr[end] 
            if cur == target:
                return [start + 1, end + 1]
            if cur < target:
                start += 1
            else:
                end -= 1
        
        return [-1, -1]


my = Solution()
print(my.twoSum([2, 7, 11, 15], 9))
print(my.twoSum([2, 3, 4], 6))
print(my.twoSum([-1, 0], -1))

print(my.twoSumII([2, 7, 11, 15], 9))
print(my.twoSumII([2, 3, 4], 6))
print(my.twoSumII([-1, 0], -1))

# Takeaway: wow! What a clever solution!


