# Subsets (Leetcode 78)

# Given an integer array nums of unique elements, return
# all possible subsets (the power set).

# The solution set must not contain duplicate subsets. Return
# the solution in any order.

class Solution:
    def subsets(self, nums):
        output = []
        def backtrack(i, cur):
            if i == len(nums):
                output.append(list(cur))
                return
            backtrack(i+1, cur)
            cur.append(nums[i])
            backtrack(i+1, cur)
            cur.pop()
        
        if nums:
            backtrack(0, [])
        return output

if __name__ == "__main__":
    my = Solution()
    print(my.subsets([1,2,3]))
    print(my.subsets([0]))

            