# Rotting Oranges (Leetcode 994)

# You are given an mxn grid where each cell can have one of three
# values. 0 represents an empty cell; 1 represents a fresh orange;
# 2 represents a rotten orange. Every minute, any fresh orange that
# is four-directionally adjacent to a rotten orange becomes rotten.

# Return the minimum number of minutes that must elapse until no cell
# has a fresh orange. If this is impossible, return -1.

class Solution:
    def orangesRotting(self, grid):
        max_vert = len(grid)
        max_hor = len(grid[0])
        rotten_set = set()
        fresh_set = set()
        
        for r in range(max_vert):
            for c in range(max_hor):
                if grid[r][c] == 2:
                    rotten_set.add((r, c))
                elif grid[r][c] == 1:
                    fresh_set.add((r, c))

        if not fresh_set:
            return 0
        
        dirs = [[0, 1], [0, -1], [1, 0], [-1, 0]]
        time = 1
        while fresh_set:

            new_rotten = set()

            for r, c in rotten_set:
                new_rotten.add((r, c))
                for r_dir, c_dir in dirs:
                    new_row, new_col = r + r_dir, c + c_dir
                    if (new_row, new_col) in fresh_set:
                        fresh_set.remove((new_row, new_col))
                        new_rotten.add((new_row, new_col))

            if not fresh_set:
                return time

            if len(rotten_set) == len(new_rotten):
                return -1

            rotten_set = new_rotten
            time += 1                

if __name__ == "__main__":
    my = Solution()
    print(my.orangesRotting([[2,1,1],[1,1,0],[0,1,1]]))
    print(my.orangesRotting([[2,1,1],[0,1,1],[1,0,1]]))
    print(my.orangesRotting([[0,2]]))
                    
