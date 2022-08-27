# Number of Islands (Leetcode 200)

# Given an m x n 2D binary grid which represents a map of 1s (land)
# and 0s (water), return the number of islands.

# An island is surrounded by water and is formed by connecting
# adjacent lands horizontally or vertically. You may assume all
# four edges of the grid are surrounded by water.

from collections import deque

class Solution:
    def numIslands(self, grid):
        # Naive, really slow solution. I am wondering about ways to speed it up.
        count = 0
        
        i = 0
        j = 0

        max_hor = len(grid[0])
        max_vert = len(grid)

        next_to_visit = (max_vert, max_hor)

        visited = set()

        def move_right(i, j): return (i, j+1)
        def move_down(i, j): return (i+1, j)
        def move_left(i, j): return (i, j-1)
        def move_up(i, j): return (i-1, j)

        def bfs(row_col):
            row, col = row_col
            nonlocal next_to_visit

            if (row, col) not in visited:

                if grid[row][col] == "1":
                    visited.add((row, col))
                    if col < max_hor - 1:
                        bfs(move_right(row, col))
                    if col > 0:
                        bfs(move_left(row, col))
                    if row < max_vert - 1:
                        bfs(move_down(row, col))
                    if row > 0:
                        bfs(move_up(row, col))
            
                else:
                    next_row, next_col = next_to_visit
                    if row < next_row or (row == next_row and col < next_col):
                        next_to_visit = (row, col)            
 

        while i < max_vert and j < max_hor:
            if (i, j) in visited:
                if j < len(grid[0])-1:
                    j += 1
                else:
                    j = 0
                    i += 1

            else:

                if grid[i][j] == "1":
                    count += 1

                    bfs((i, j))
                
                visited.add((i, j))

                i, j = next_to_visit

        return count

    # Trying to analyze why my solution is so slow. Is this because
    # I was going through the same modes twice (only to discard them seeing that
    # they are present in the set visited) a lot? Yes, for sure. However, I also
    # created four functions for moving in four directions, and this must have really
    # hampered both speed and space usage.

    def numIslandsFast(self, grid):
        # This solution belongs to Neetcode.
        if not grid or not grid[0]:
            return 0
        
        count = 0
        visited = set()
        rows, cols = len(grid), len(grid[0])

        directions = [[0,1], [0, -1], [1, 0], [-1, 0]]

        def dfs(r, c):
            if (
                r not in range(rows) or \
                c not in range(cols) or \
                grid[r][c] == "0" or \
                (r, c) in visited
            ):
                return
            
            visited.add((r, c))
            nonlocal directions
            # using a list comprehension instead of calling four
            # full-blown functions to move in the four directions.
            # very time- and space-efficient.
            directions = [[0,1], [0, -1], [1, 0], [-1, 0]]
            for dir_row, dir_col in directions:
                dfs(r+dir_row, c+dir_col)
            
        # using for loops makes looping more concise than my
        # heavyweight while loops! We need to continuously increment
        # and traverse the whole grid -> of course the for loops are
        # good for that!
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == "1" and (r, c) not in visited:
                    count += 1
                    dfs(r, c)

        return count
    
    def numIslandsIter(self, grid):
        # Iterative solution
        if not grid[0] or not grid:
            return 0

        count = 0
        max_hor = len(grid[0])
        max_vert = len(grid)
        #print(max_vert, max_hor)

        visited = set()
        directions = [[0, 1], [0, -1], [1, 0], [-1, 0]]

        q = deque([])

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if (i, j) not in visited and grid[i][j] == "1":
                    count += 1
                    
                    q.append((i, j))

                    while q:
                        # This is breadth-first search (queue).
                        # We can also do depth-first (stack).
                        row, col = q.popleft()

                        if (row in range(max_vert) and \
                        col in range(max_hor) and \
                        grid[row][col] == "1" and \
                        (row, col) not in visited):
                            visited.add((row, col))

                            for dir_row, dir_col in directions:
                                q.append((row + dir_row, col + dir_col))
                        
        return count




if __name__ == "__main__":
    my = Solution()
    grid1 = [["1","1","1","1","0"],
  ["1","1","0","1","0"],
  ["1","1","0","0","0"],
  ["0","0","0","0","0"]]
    #print(my.numIslands(grid1))

    grid2 = [["1","1","0","0","0"],
  ["1","1","0","0","0"],
  ["0","0","1","0","0"],
  ["0","0","0","1","1"]]

    #print(my.numIslands(grid2))

    grid3 = [["1","1","1"],["0","1","0"],["1","1","1"]]

    #print(my.numIslands(grid3))

    grid4 = [["0","0","0","0","0","0","1"]]

    """print(my.numIslands(grid4))

    print("The second solution")
    print(my.numIslandsFast(grid1))
    print(my.numIslandsFast(grid2))
    print(my.numIslandsFast(grid3))"""

    print(my.numIslandsIter(grid1))
    print(my.numIslandsIter(grid2))
    print(my.numIslandsIter(grid3))



