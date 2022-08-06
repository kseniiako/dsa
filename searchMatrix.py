# Search a 2D matrix! (LC 74)

# Write an efficient algorithm that searchs for a value target
# in a m x n integer matrix matrix. 

# Integers in each row are sorted from left to right
# The first integer of each row is greater than the last
# integer of the previous row. 

class Solution():
    def searchMx(self, matrix, target):


        # first let's search by rows

        start = 0
        finish = len(matrix) - 1

        while (start <= finish):

            mid = (start + finish) // 2

            if matrix[mid][0] == target:
                return True
            elif matrix[mid][0] < target:
                start = mid + 1
            elif matrix[mid][0] > target:
                finish = mid - 1
 
        row = start - 1

        
        # now let's search the selected row (variable row)

        start = 0
        finish = len(matrix[row]) - 1

        while (start <= finish):

            mid = (start + finish) // 2

            if matrix[row][mid] == target:

                return True
            if matrix[row][mid] < target:
                start = mid + 1
            elif matrix[row][mid] > target:
                finish = mid - 1
            
        return False

    def searchMatrix2(self, matrix, target):

        # in this variant of the solution, we perform
        # one binary search across the matrix as a "virtual
        # array" instead of two searches.

        row_len = len(matrix[0])

        start = 0
        finish = len(matrix) * len(matrix[0]) - 1

        while start <= finish:

            mid = start + ( (finish - start) // 2 )

            row, col = divmod(mid, row_len)

            if matrix[row][col] == target:
                return True
            if matrix[row][col] < target:
                start = mid + 1
            else:
                finish = mid - 1

        return False

# The one-array second solution looks cooler, but it 
# is a third or so slower due to divmod being an expensive ass
# operation!


matrix1 = [[1,3,5,7],[10,11,16,20],[23,30,34,60]]
target1 = 3    
target2 = 13

matrix2 = [[1], [3]]
my = Solution()
print(my.searchMx(matrix1, target1))
print(my.searchMx(matrix1, target2))
print(my.searchMx(matrix2, target1))

print(my.searchMatrix2(matrix1, target1))
print(my.searchMatrix2(matrix1, target2))
print(my.searchMatrix2(matrix2, target1))




