class Solution:
    def countBits1(self, n: int) -> list[int]:
        # basic solution based on
        # hamming weight algorithm
        out = []
        for x in range(n+1):
            val = 0
            while x != 0:
                x &= x-1
                val += 1
            out.append(val)
        return out

    def countBits2(self, n: int) -> list[int]:
        # solution exploiting the fact
        # that consecutive integers which need
        # n bits to be represented have the
        # same represenatation as an integer
        # that is 2**n bits smaller + a leading
        # set bit
        ans = [0] * (n+1)
        x = 0
        b = 1

        # [0, b) is calculated
        while b <= n:
            # generate [b, 2b) or [b, n) from [0, b)
            while x < b and x + b <= n:
                ans[x+b] = ans[x] + 1
                x += 1
            x = 0
            b <<= 1 # b *= 2

        return ans
    
    def countBits3(self, n: int) -> list[int]:
        ans = [0] * (n+1)
        ans[1] = 1
        for x in range(2, n+1):
            ans[x] = ans[x >> 1] + (x & 1)
        return ans

    def countBits4(self, n: int) -> list[int]:
        ans = [0] * (n+1)
        for x in range(1, n+1):
            ans[x] = ans[x & (x - 1)] + 1
        return ans



# testing
my = Solution()
print(my.countBits1(15))
print(my.countBits2(15))
print(my.countBits3(15))
print(my.countBits4(15))
                