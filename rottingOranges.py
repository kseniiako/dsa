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
            init_length_of_fresh_set = len(fresh_set)

            for r, c in rotten_set:
                for r_dir, c_dir in dirs:
                    new_row, new_col = r + r_dir, c + c_dir
                    if (new_row, new_col) in fresh_set:
                        fresh_set.remove((new_row, new_col))
                        new_rotten.add((new_row, new_col))

            if not fresh_set:
                return time

            if len(fresh_set) == init_length_of_fresh_set:
                return -1

            rotten_set = new_rotten
            time += 1  

    # This solution takes an approach similar to the one I chose for Surrounded
    # Regions (another graph problem in this repo). I put the relevant index tuples
    # into sets to avoid ever having to check and re-check irrelevant indices (empty
    # cells). Idea: initially I wanted to add all "rotten" indices (both pre-existing
    # ones and the ones that became rotten during the last step) to the new version of
    # rotten_set (called new_rotten). However, I realized that old rotten oranges
    # already "rottified" everything they could reach in the first step of their existence.
    # Therefore, we can throw them out for the sake of time and space efficiency and proceed
    # with just the newly "rotted" oranges in the new set. It is interesting how the two sets 
    # (old and new one) act analogously to a queue (as used in breadth-first search) in this 
    # solution.

    # Assume m and n are dimensions of the grid.
    # Time complexity: O(m*n). We need O(m*n) time to traverse the grid and find all 
    # non-empty cells in the first loop. And O(m*n) time to recursively turn to rotten all 
    # the oranges that are fresh.
    # Space complexity: O(m*n) to hold the three sets: fresh_set, rotten_set, and new_rotten. 
    # Total: O(m*n).

if __name__ == "__main__":
    my = Solution()
    print(my.orangesRotting([[2,1,1],[1,1,0],[0,1,1]]))
    print(my.orangesRotting([[2,1,1],[0,1,1],[1,0,1]]))
    print(my.orangesRotting([[0,2]]))
                    
