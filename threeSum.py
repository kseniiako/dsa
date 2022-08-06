# ThreeSum! (Leetcode 15)

# Given an integer array nums, return all the triplets [nums[i]],
# nums[j], nums[k] such that i != j, j != k, i != k, and nums[i] +
# nums[j] + nums[k] == 0.

# The brute force solution (three loops) would run in O(n^3) time.

class Solution():
    def threeSum(self, arr):
        looking_for_two = set()
        looking_for_one = {}

        output = []
        # My initial idea: solution with two dictionaries.
        for x in range(len(arr)):

            cur = arr[x]

            if cur in looking_for_one:
                looking_for_one[cur].append[cur]
                if looking_for_one[cur] not in output:
                    output.append(looking_for_one[cur])
            
            for x in looking_for_two:
                
            

nums1 = [-1,0,1,2,-1,-4]
nums2 = [0,1,1]
nums3 = [0, 0, 0]
my = Solution()
print(my.threeSum(nums1))



