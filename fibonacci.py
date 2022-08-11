# An efficient algorithm computing nth Fibonacci number
# using dynamic programming.
# LC 509

class Solution:
    def fib(self, n):
        def fib_help(n):
            if n == 0:
                return (0, 0)
            if n == 1:
                return (1, 0)

            (a, b) = fib_help(n-1)
            return (a+b, a)
        
        out = fib_help(n)
        return out[0]

        # this solution is not good enough: it is O(n) time —
        # good, but the function call stack takes up O(n) space,
        # which may cause stack overflow.

    def fibIter(self, n):
        # an iterative approach to avoid O(n) space.

        # let's create variables to hold F(n-1), F(n-2)
        # from F(n-1) and F(n-2), we can easily compute F(n).

        nMinusTwo = 0
        nMinusOne = 1  

        if n == 0:
            return nMinusTwo
        if n == 1:
            return nMinusOne

        for x in range(2, n):
            nMinusOne, nMinusTwo = nMinusOne + nMinusTwo, nMinusOne

        return nMinusOne + nMinusTwo



if __name__ == "__main__":

    my = Solution()

    print("Recursive Approach!")

    print(my.fib(0))
    print(my.fib(1))
    print(my.fib(2))
    print(my.fib(3))
    print(my.fib(4))
    print(my.fib(5))
    print(my.fib(6))
    print(my.fib(7))
    print(my.fib(8))
    print(my.fib(9))

    print("Iterative Approach!")

    print(my.fibIter(0))
    print(my.fibIter(1))
    print(my.fibIter(2))
    print(my.fibIter(3))
    print(my.fibIter(4))
    print(my.fibIter(5))
    print(my.fibIter(6))
    print(my.fibIter(7))
    print(my.fibIter(8))
    print(my.fibIter(9))

# Takeaway: make sure output types are consistent! E. g. it's not
# good to have tuples of unpredictable length or tuples mixed with
# integers if this is avoidable.



