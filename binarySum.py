# Note: this is a question about summing two integers
# without using + or - (that is, with binary operations and
# god's help). There is also a leetcode question about summing
# two integers represented as binary strings. The latter one accepts a
# solution that the first one regects. Oh well. Question names and #'s
# are, respectively, 

class Solution:
    def addTwo(self, a, b):
        while b:
            add = a ^ b
            carryover = (a & b) << 1
            a, b = add, carryover
        return a

my = Solution()
print(my.addTwo(1, 2))
print(my.addTwo(3, 5))
print(my.addTwo(0, -1))

import pdb; pdb.set_trace()

print(my.addTwo(1, -1))