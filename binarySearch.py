
def binarySearch(lst, elem, start = 0, end = False):
    """ Implementation of binary search
    (over a sorted list) """

    # if end not given, assume end is the end of list
    if end == False:
        end = len(lst)-1
    
    # if start > end, no data can be found
    if start > end:
        return False

    # find midpoint index
    mid = (end + start) // 2

    if lst[mid] == elem:
        return True
    if lst[mid] > elem:
        return binarySearch(lst, elem, start, mid-1)
    if lst[mid] < elem:
        return binarySearch(lst, elem, mid+1)


if __name__ == "__main__":
    lst = [0, 1, 2, 3, 4, 5, 6, 75, 78, 79, 80, 81, 82]
    binarySearch(lst, 0)
    binarySearch(lst, 82)
    binarySearch(lst, 83)
    binarySearch(lst, -85)
    binarySearch(lst, 76)
    binarySearch(lst, 6)
    binarySearch(lst, 4)
    binarySearch(lst, 79)
    binarySearch(lst, 81)

# key takeaway: it might happen because we increment mid/
# change values of start and end that start becomes 
# larger than end. We gotta avoid this!

