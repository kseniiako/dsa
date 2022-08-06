# reversing a sequence given as a list

def reverse(lst, start = 0, stop = False):
    """ Reverse a given list """
    
    # if stop == False, set stop to end of list
    if stop == False:
        stop = len(lst) - 1
    
    # is start == stop (0-element sequence),
    # or start == stop - 1 (1-element sequence),
    # the original list is already its own reverse
    if start == stop or start == stop - 1:
        return lst

    else:
        lst[start], lst[stop] = lst[stop], lst[start]
        return reverse(lst, start+1, stop-1)

if __name__ == "__main__":
    print(reverse([0, 1, 2, 3, 4, 5]))

# Takeaway: simultaneous assignment. 
# When using simultaneous assignment, all of the expressions
# are evaluated on the right-hand side before 
# any of the assignments are made to the left-hand variables. 
# This provides a way to quickly swap values without
# a temp variable. The unnamed tuple on the right-hand side
# implicitly serves as the temporary variable when
# performing such a swap. (We could also have an explicit tuple
# on that side).

