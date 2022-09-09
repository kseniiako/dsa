# Set Matrix Zeroes (Leetcode 73)

# Given an m x n integer matrix, if an element is 0, set
# its entire row and column to 0's. You must do this in place.

class Solution:
    def setZeroes(self, matrix):
        # My initial approach: save row and col numbers where elements have to be
        # set to 0 in two sets. Iterate through the whole grid and populate the sets
        # Iterate through the rows_to_zero set to change all eligible values to 0.
        # Iterate through the cols_to_zero set to change all eligible values to 0.
        rows_to_zero = set()
        cols_to_zero = set()
        max_vert = len(matrix)
        max_hor = len(matrix[0])

        for r in range(max_vert):
            for c in range(max_hor):
                    if matrix[r][c] == 0:
                        rows_to_zero.add(r)
                        cols_to_zero.add(c)
        
        for ind in rows_to_zero:
            for c in range(max_hor):
                matrix[ind][c] = 0
        
        for ind in cols_to_zero:
            for r in range(max_vert):
                matrix[r][ind] = 0
        
        # matrix should be updated in place
        print(matrix)
        return

        # O(m+n) = O(max(m, n)) space to store the two sets.
        # O(m*n) time for each of the three traversals.
        # In total, space complexity is O(max(m, n)), time complexity is O(m*n).

    def setZeroes2(self, matrix):
        # Note how in the previous approach we could have redundant operations
        # in the last two iterations. If a node had to be set to zero both because of
        # the row and the column value, we would set it to zero twice. To improve on that,
        # we can just iterate over the whole grid and set cell values to 0 where
        # either the row, or the column is in the zeros set. The or condition short-circuits,
        # so this could also save us some time. Time and space complexity stay the same.

        # This approach is faster than the previous one for matrices with a lot of zeroes, and more
        # precisely, where a lot of nodes have to be set to zero due to both row and column. However,
        # for matrices where zeros are sparce it is noticeably slower, because it goes through the whole
        # m*n grid, even the positions where the values don't need to be set to 0. This (second) approach
        # seems to perform worse on Leetcode test set.

        # Note that still have redundancy associated with "setting to 0" nodes that were already
        # zero-valued in the input.
        rows_to_zero = set()
        cols_to_zero = set()
        max_vert = len(matrix)
        max_hor = len(matrix[0])

        for r in range(max_vert):
            for c in range(max_hor):
                    if matrix[r][c] == 0:
                        rows_to_zero.add(r)
                        cols_to_zero.add(c)
        
        for r in range(max_vert):
            for c in range(max_hor):
                if r in rows_to_zero or c in cols_to_zero:
                    matrix[r][c] = 0

        # matrix should be updated in place
        print(matrix)
        return
    
    def setZeroesBetter(self, matrix):
        # An efficient solution: O(1) space use.
        # As posted on Leetcode.

        # Rather than using additional variables to keep track of
        # rows and columns to be reset, we use the matrix itself as a set of
        # indicators.
        # "The idea is to use the first cell of every row and column as a flag.
        # The flag would determine whether a row or column has been set to 0. This
        # means that for every cell, we may set the flag in two cells."

        # The first cell of row and column for the first row is the same. Hence,
        # we use an additional variable to tell us if the first column has been marked
        # or not, and the cell matrix[0][0] would be used to tell the same for the first row.

        # Since first cells in every row and column are used as marks, we delay possibly
        # setting the first row and column to 0 until we've traversed the rest of the grid
        # and set appropriate values to 0. (Without this safety measure, illegible rows/cols
        # would be set to 0 if first col/row respectively is 0.)

        # Space complexity: O(1). We only create a handful of extra variables, each one
        # takes up O(1) space. Most values are saved within the matrix itself (marks).
        # Time complexiy is O(n*m) for traversing the whole grid and setting values to 0 where
        # appropriate.

        firstCol = 1
        max_vert = len(matrix)
        max_hor = len(matrix[0])

        for r in range(max_vert):
            # perform a check to update the variable firstCol
            if matrix[r][0] == 0:
                firstCol = 0
            # perform all other checks to set marks in place
            for c in range(1, max_hor):
                if matrix[r][c] == 0:
                    matrix[r][0] = 0
                    matrix[0][c] = 0
        
        for r in range(1, max_vert):
            for c in range(1, max_hor):
                if (matrix[r][0] == 0) or (matrix[0][c] == 0):
                    matrix[r][c] = 0
        
        if not matrix[0][0]:
            for c in range(max_hor):
                matrix[0][c] = 0

        if not firstCol:
            for r in range(max_vert):
                matrix[r][0] = 0
        
        print(matrix)
        return

        # Note: initially I tried first checking the value of firstCol and possibly setting the whole 
        # first column to 0s, and then checking the value of matrix[0][0] and possibly setting the whole
        # first row to 0s. However, this resulted in mistakes because I flipped matrix[0][0] to 0 when
        # firstCol was equal to 0. So we need to either change the order of the two operations (which I 
        # did to make the solution correct), or iterate from 1 to max_vert (not from 0 to max_vert) when
        # setting the first column to 0, and handle setting matrix[0][0] to 0 at the very end of the program.

if __name__ == "__main__":
    my = Solution()

    matrix0 = [[1,1,1],[1,0,1],[1,1,1]]
    my.setZeroes(matrix0)

    matrix1 = [[0,1,2,0],[3,4,5,2],[1,3,1,5]]
    my.setZeroes(matrix1)

    matrix0 = [[1,1,1],[1,0,1],[1,1,1]]
    my.setZeroes2(matrix0)

    matrix1 = [[0,1,2,0],[3,4,5,2],[1,3,1,5]]
    my.setZeroes2(matrix1)

    matrix0 = [[1,1,1],[1,0,1],[1,1,1]]
    my.setZeroesBetter(matrix0)

    matrix1 = [[0,1,2,0],[3,4,5,2],[1,3,1,5]]
    my.setZeroesBetter(matrix1)
