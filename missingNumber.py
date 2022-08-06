class Solution:
    def missingNumber(self, nums: list[int]) -> int:
        # bit manipulation solution (not my own,
        # given by leetcode).
        n = len(nums)
        for ind, val in enumerate(nums):
            n ^= ind ^ val
        return n

    def missingNumberGauss(self, nums: list[int]) -> int:
        # this is another solutuion I read
        # about leetcode. It is pretty intuitive:
        # uses Gaussian formula. 
        # We quickly find sum of first n naturals 
        # (0 excluded) using gauss's formula:
        # it's n*(n+1)/2. The array we're given is a 
        # valid sum of these integers where one of them
        # is replaced by 0. So we calculate sum of our array
        # and substract it from expected result (by Gauss's formula).
        # We can increment/decrement some numbers to account
        # for a 0 in the array — but it's extraneous,
        # just makes everything a bit uglier.
        n = len(nums)
        sum_nums = sum(nums)
        sum_gauss = (n)*(n+1)/2
        return sum_gauss - sum_nums


l1 = [0, 1, 3, 4]

my = Solution()
print(my.missingNumber(l1))
print(my.missingNumberGauss(l1))