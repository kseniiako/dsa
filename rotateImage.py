# Leetcode 48 (Rotate Image)

# Given an n * n 2D matrix representing an image, rotate
# the image by 90 degrees (clockwise, in-place).

# From linear algebra, we know that rotating the matrix is the
# same as reversing it around the main diagonal (transposition), and
# then reversing it from left to right (reflection).

class Solution:
    def rotateImage(self, matrix):
        # Transpose and reflect!
        def transpose(matrix):
            for x in range(len(matrix[0])):
                for y in range(len(matrix)):
                    if x < y:
                        matrix[y][x], matrix[x][y] = matrix[x][y], matrix[y][x]
        
        def reflect(matrix):
            start = 0
            finish = len(matrix[0]) - 1
            while start < finish:
                for x in range(len(matrix)):
                    matrix[x][start], matrix[x][finish] = matrix[x][finish], matrix[x][start]
                start += 1
                finish -= 1
        transpose(matrix)
        reflect(matrix)
        
        print(matrix)
    
    # Where n is the number of cells in the matrix,
    # O(n) is the time complexity (for reversal and transposition)
    # and O(1) is the space complexity (we do not use any additional
    # data structures).
    
if __name__ == "__main__":
    my = Solution()
    print(my.rotateImage([[1,2,3],[4,5,6],[7,8,9]]))