# Goodrich et. al. discuss different implementations
# of a function that, given n, returns nth number
# of fibonacci sequence. One is inefficient and runs
# in exponential time. Another one runs in O(n).
# Here's the linear (O(n)) time implementation. 

# This function is so efficient because it keeps
# track not just of nth Fibonacci element, but also
# of (n-1)th element. (The latter is needed to 
# compute nth element.)
def goodFib(n):
    """ Returns pair of Fibonacci numbers:
    ( F(n), F(n-1) ). n must be >= 0 """

    # Base cases:
    # we consider 0 to be the 0th element of
    # the Fibonacci sequence, 1 — the 1st, etc.
    if n == 0:
        return(0)
    if n == 1:
        return(1, 0)


    else:
        (a, b) = goodFib(n-1)
        return (a+b, a)
    
# Takeaway: sometimes binary recursion
# means you would have to calculate the same
# thing twice or 2**n times: inefficiency!

if __name__ == "__main__":
    print(goodFib(0))
    print(goodFib(1))
    print(goodFib(2))
    print(goodFib(3))
    print(goodFib(4))
    print(goodFib(5))
    print(goodFib(6))
    print(goodFib(7))
    print(goodFib(8))
    print(goodFib(9))

