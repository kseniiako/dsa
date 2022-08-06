class Solution:
    def hammingWeight(self, n: int) -> int:
        # the commented-out solutuon takes too
        # much time -> let's try a different approach!
        # we know bitwise is faster than arithmetic
        """ out = 0
        while n > 0:
            if n % 2 == 1:
                out +=1
            n //= 2
        return out """
        out = 0
        while n!=0:
            n &= n-1
            out += 1
        return out

my = Solution()
print(my.hammingWeight(15))