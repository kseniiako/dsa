# Efficient algorithm for computing powers
# that uses squaring technique

def power(x, n):
    """ Compute x**n. Works with natural n. """
    
    # Base cases:
    if n < 0:
        return "Please input n >= 0"
    if n == 0:
        return 1
    
    # Recursive cases:
    prev = power(x, n//2)
    if n%2 == 0:
        return prev*prev
    else: 
       return x*prev*prev

if __name__ == "__main__":
    print(power(2, 5))
    print(power(2, 10))
    print(power(3, 5))
    print(power(4, 2))
    print(power(3, 1))
    print(power(0, 0))
    print(power(2, 13))

# The number of times we can divide n in half before
# getting to one or less is O(log n).

# Takeaway: cut down the number of recursive calls!
# (It is often very useful to minimize the
# number of recursion calls.) Besides improving runtime, 
# this strategy might reduce memory usage: no redundant
# activation records are stored.

# Because the recursive depth of this version is O(log n),
# memory usage is O(log n) as well. 

