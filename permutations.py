# Permutations (Leetcode 46)

# Given an array nums of distinct integers, return
# all possible permutations. You can return the answer
# in any order.
import copy

class Solution:
    def permute(self, nums):
        # Trying to make it work with a set
        # (for easy pops/delections)
        output = []
        nums_set = set(nums)

        def backtrack(nums_set, cur):
            if not nums_set:
                output.append(cur)
                return
            for each in nums_set:
                nums_set1 = copy.deepcopy(nums_set)
                nums_set1.remove(each)
                cur.append(each)
                backtrack(nums_set1, list(cur))

                cur.pop()

        backtrack(nums_set, [])
        return output

    def permute1(self, nums):
        res = []

        if len(nums) == 1:
            return [list(nums)] # creating a deep copy of the list

        for i in range(len(nums)):
            num = nums.pop(0)
            perms = self.permute(nums)

            for perm in perms:
                perm.append(num)

            res.extend(perms)
            nums.append(num)
        return res

if __name__ == "__main__":
    my = Solution()
    print(my.permute([1, 2, 3]))
    print(my.permute1([1, 2, 3]))
