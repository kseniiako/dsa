class Solution:
    def reverseBits(self, n):
        out = 0
        for pos in range(32):
            if n & 1:
                out |= (1 << (31 - pos) )
            n >>= 1
        return out
        

my = Solution()
print(bin(my.reverseBits(10)))