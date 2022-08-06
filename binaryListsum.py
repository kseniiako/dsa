# Function that uses binary recursion to
# sum all the numbers in a list. By using binary
# instead of linear recrsion, we use less space:
# recusion depth is 1+log n vs 1+n. However,
# time comlexity stays the same.

# This is an implementation where we take stop=len(lst)-1 and
# add lst[stop] in the base case. It is less readable,
# longer, and slower than taking stop=len(lst) and adding
# lst[start] in each base case. I believe this asymmetry between
# two implementations arises because len(lst) provides
# a "natural" throwaway value. The point is, this function
# is implemented as it is for practice; for deployment, it 
# should be reimplemented the "natural" way, as god intended. 

def listSum(lst, start = 0, stop = False):

    # If not provided, set stop to the last element of list
    if stop == False:
        stop = len(lst)-1

    # If start > stop, there is nothing
    # in this slice
    if start > stop:
        return 0
    # Base case: 
    if start == stop-1:
        if lst[start] == lst[0]:
            return lst[stop]+lst[start]
        else:
            return lst[stop]
    
    # Recursive case:
    mid = (start+stop+1)//2
    return listSum(lst, start, mid) + listSum(lst, mid, stop)
    
if __name__ == "__main__":

    lst1 = [1, 2, 3, 4, 5]
    lst2 = [18, 2, 3, 4, 5]

    print(listSum(lst1))
    print(listSum(lst2))


# Takeaway: working with lists is tricky!

# We should define base cases so that every possible chain
# of recursive calls will eventually reach a base case, and
# the handling of each base case would not resort to recursion.

# It might be a good idea to reparameterize the function or
# change/strengthen the output expectation (e. g. two values
# instead of one.)

# Takeaway set 2:

# If working with an integer mean floor (or ceiling),
# make sure that you are progressing towards the base case
# in every recursive case! There is a risk of infinite
# recursion!

# Also, sketching out the recursive trace on paper
# helps so much!
