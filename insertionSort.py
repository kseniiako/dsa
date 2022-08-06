# simple and inefficient sorting algorithm
# which inserts every next element in its correct
# place among the previous, already sorted elements.
# Returns list sorted from smallest to largest element.
def insertionSort(lst):
    """ Sorts a list from lowest to highest value
    using insertion sort """ 
    for i in range(len(lst)):
        while lst[i-1]>lst[i] and i != 0:
            lst[i-1], lst[i] = lst[i], lst[i-1]
            i = i-1

    print(lst)

if __name__ == "__main__":
    lst0 = [0, 1, 2, 5]
    lst1 = []
    lst2 = [0]
    lst3 = [1, 2]
    lst4 = [50, 60, 70]
    lst5 = [-15, 16, 45]
    lst6 = [9, 15, 4]

    insertionSort(lst0)
    insertionSort(lst1)
    insertionSort(lst2)
    insertionSort(lst3)
    insertionSort(lst4)
    insertionSort(lst5)
    insertionSort(lst6)

