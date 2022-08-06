class Solution():
    def getSum(self, a, b):
        x, y = abs(a), abs(b)

        if x<y:
            return self.getSum(b, a)
        
        # since abs(a) >= abs(b), a determines the sign
        sign = 1 if a > 0 else -1

        if a * b >= 0:
            # We need to find sum of two positives
            while y:
                ans = x ^ y
                carryover = (x & y) << 1
                x, y = ans, carryover

        else:
            # We need to find difference of two positives
            # x - y
            while y:
                ans = x ^ y
                carryover = ((~x) & y) << 1
                x, y = ans, carryover

        return x * sign
    
    def getSum2(self, a, b):
        # this is a language-specific solution:
        # it explicitly deals with 32-bit integers.abs
        # this approach would look simpler in Java but since
        # python has automatic (re)typing we need to add
        # some masking manually. 

        # 32 1-bits
        mask = 0xFFFFFFFF

        while b != 0:

            # note how each masking ensures we have no more
            # than 32 set bits
            a, b = (a ^ b) & mask, ((a & b) << 1) & mask

        # max positive value available
        max_int = 0x7FFFFFFF

        # if a is overflowing (greater than max_int), we need to find
        # value of the positive int which is a
        # without the first bit
        return a if a < max_int else ~(a ^ mask)
