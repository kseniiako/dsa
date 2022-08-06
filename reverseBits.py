class Solution:
    def reverseBits0(self, n: int) -> int:
        # primitive solution to reverse bits:
        # transform int into a string representing
        # binary number, reverse everhythin, and
        # add missing zeros!
        bin_st = list(bin(n)[2:])
        count = len(bin_st) - 1
        for x in range(len(bin_st)//2):
            bin_st[x], bin_st[count - x] = bin_st[count - x], bin_st[x]
        
        # now add missing trailing (formerly front) zeros
        zeros = 0
        if count < 31:
            zeros = 31 - count
        zeros_lst = ["0"] * zeros
        ans = "".join(bin_st)
        zeros = "".join(zeros_lst)
        return int(ans + zeros, 2)

my = Solution()
my.reverseBits0(13)

# Takeaway: sometimes I can come up with not-the-most-elegant
# approach which is still a working approach! Later I can
# study some more elegant/efficient approaches and add them
# to my arsenal. This is a way to develop new skills AND 
# practice old ones instead of getting stuck if new skills are lacking.