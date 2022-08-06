class Solution:
    def myPow(self, x: float, n: int) -> float:
        """if n == 0:
            return 1
        if n < 0:
            return 1/self.myPow(x, -n)
        else:
            if n % 2 == 0:
                prev_power = self.myPow(x, n/2)
                return prev_power * prev_power
            else:
                prev_power = self.myPow(x, n-1)
                return prev_power * x """
        # adjustment for negative exponent
        if n < 0:
            x = 1/x
            n = -n

        out = 1
        current = x
        i = n
        while i > 0:
            if i % 2 == 1:
                out *= current
            current *= current
            i //= 2
        return out


# import pdb; pdb.set_trace()

my = Solution()
print(my.myPow(2.0, 3))

# Takeaway: pdb rocks! This method is called fast power
# because we need at most O(log n) of O(1) computations to get to x^n

# It is worthwhile to compare the iterative and recursive 
# solutuons which technically use the same algorithm.
# In recursive approach, space complexity is O(log n), 
# in iterative, it is O(1) because we don't create log n function
# calls/activation records.

# Checks for n<=0 aqnd for n == 0 are needed, checks for n == 1,
# n == 2 are extraneous (always goes down to 0).