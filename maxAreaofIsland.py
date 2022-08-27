# Max Area of Island (Leetcode 695)

# You are given a m x n binary matrix grid. An island is a group of 1s
# connected 4-directionally (horizontal or vertical). You may assume
# all four edges of the grid are surrounded by water.

# The area of an island is the number of cells with value 1 in an island.

# Return max area of island in a grid. If there is no island, return 0.

from collections import deque

class Solution:
    def maxAreaOfIsland(self, grid):
        max_num = cur_num = 0

        max_row = len(grid)
        max_col = len(grid[0])

        visited = set()

        q = deque([])

        directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]

        for i in range(max_row):
            for j in range(max_col):

                if ((i, j) not in visited) and grid[i][j]:

                    q.append((i, j))

                    while q:
                        row, col = q.popleft()
                        if (row in range(max_row) and \
                        col in range(max_col) and \
                        (row, col) not in visited and \
                        grid[row][col]):
                            cur_num += 1
                            visited.add((row, col))

                            for row_dir, col_dir in directions:
                                q.append((row + row_dir, col + col_dir))

                    max_num, cur_num = max(max_num, cur_num), 0

        return max_num

if __name__ == "__main__":
    my = Solution()
    grid1 = [[0,0,1,0,0,0,0,1,0,0,0,0,0],[0,0,0,0,0,0,0,1,1,1,0,0,0],
    [0,1,1,0,1,0,0,0,0,0,0,0,0],[0,1,0,0,1,1,0,0,1,0,1,0,0],
    [0,1,0,0,1,1,0,0,1,1,1,0,0],[0,0,0,0,0,0,0,0,0,0,1,0,0],
    [0,0,0,0,0,0,0,1,1,1,0,0,0],[0,0,0,0,0,0,0,1,1,0,0,0,0]]
        
    print(my.maxAreaOfIsland(grid1))



