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

    def setZeroesBetter(self, matrix):
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

if __name__ == "__main__":
    my = Solution()

    matrix0 = [[1,1,1],[1,0,1],[1,1,1]]
    my.setZeroes(matrix0)

    matrix1 = [[0,1,2,0],[3,4,5,2],[1,3,1,5]]
    my.setZeroes(matrix1)

    matrix0 = [[1,1,1],[1,0,1],[1,1,1]]
    my.setZeroesBetter(matrix0)

    matrix1 = [[0,1,2,0],[3,4,5,2],[1,3,1,5]]
    my.setZeroesBetter(matrix1)
