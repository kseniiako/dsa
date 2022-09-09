# Walls and Gates (Leetcode 286)

# You are given an m x n grid rooms initialized with three
# possible values.
# -1: A wall or an obstacle.
# 0: A gate
# INF: Infinity means an empty room. We use the value (2^31)-1 =
# 2147483647 to represent INF as you may assume that the distance to a
# gate is less than 2147483647.

# Fill each empty room with the distance to its nearest gate. If
# it is impossible to reach a gate, it should be filled wih INF.

# Let's designate gates as our starting points. The empty cells around each
# gate (there can be up to four of them) will have distance to nearest gate
# equal to one. Now we set starting points to be these cells (empty cells around 
# a gate). For each starting point, we check whether in its surroundings there are
# eligible cells: that is, empty cells for which distance to gate is yet unknown or
# the current distance to gate is greater than 1+(distance value at starting point).
# For every eligible cell, we set its distance value to 1+(distance value at 
# starting point), and the eligible cells become new starting points. Repeat this process
# recursively. At some point, we will run out of eligible cells (all reachable empty
# cells will have smallest distance already inserted). Notice that unreachable cells
# need to stay at their initial value (INF). We keep the current starting cells in a set
# called cur_starts. It is updated to be a newly populated set new_starts with each
# iteration of the algorithm (to keep track of new starting points). Alternatively, instead
# of two sets interchanging places, a queue could be used. 

from collections import deque

class Solution:
    def wallsAndGates(self, grid):
        max_vert = len(grid)
        max_hor = len(grid[0])
        cur_starts = set()
        dirs = [[0, 1], [0, -1], [1, 0], [-1, 0]]

        # find all initial starting points (gates)
        for r in range(max_vert):
            for c in range(max_hor):
                if grid[r][c] == 0:
                    cur_starts.add((r, c))

        # main loop: runs while there are new starting points to explore
        while cur_starts:
            # set new_starts will collect new starting points
            new_starts = set()

            # For every starting point, check all directions for eligible cells.
            # Eligible cells must be not walls, not gates, and their current distance value
            # must be greater than the new distance value we are suggesting. Notice that
            # if current distance value is smaller than the new one, there is no need exploring
            # this cell as a starting point: all values we'll suggest in this exploration will be greater 
            # than the already existing ones.
            for r, c in cur_starts:
                for r_dir, c_dir in dirs:
                    new_r, new_c = r + r_dir, c + c_dir
                    if new_r in range(max_vert) and \
                    new_c in range(max_hor) and \
                    grid[new_r][new_c] > 0:
                        new_min = grid[r][c] + 1
                        if grid[new_r][new_c] > new_min:
                            grid[new_r][new_c] = new_min
                            new_starts.add((new_r, new_c))

            # reassign cur_stats to contain new starting points
            cur_starts = new_starts

        
        print(grid)
        # grid should be updated in place
        return

# O(m*n) time to find all gates. O(m*n) time to set all the distance values. Total time
# complexity: O(m*n).
# O(m*n) space to keep the starting_points set. Other space "expenditures" are constant-space.
# Total space complexity: O(m*n).

    def wallsAndGatesQueue(self, grid):
        # version that uses a queue insteasd of two sets
        max_vert = len(grid)
        max_hor = len(grid[0])
        dirs = [[0, 1], [0, -1], [1, 0], [-1, 0]]
        q = deque([])

        for r in range(max_vert):
            for c in range(max_hor):
                if grid[r][c] == 0:
                    q.append((r, c))

        while q:
            r, c = q.popleft()
            for r_dir, c_dir in dirs:
                new_r, new_c = r + r_dir, c + c_dir
                if new_r in range(max_vert) and \
                new_c in range(max_hor) and \
                grid[new_r][new_c] > 0:
                    new_min = grid[r][c] + 1
                    if grid[new_r][new_c] > new_min:
                        grid[new_r][new_c] = new_min
                        q.append((new_r, new_c))

        print(grid)

        return

        # O(m*n) time complexity, O(m*n) space complexity (for the stack).

# Idea: keep a set of visited nodes to avoid visiting a node twice. Since we are
# doing breadth-first search starting at the gates, the first time an empty node is visited,
# we will set the node's distance to the min possible value. (Other distance values that 
# it could be compared against in the future will be at least as big). Instead of keeping a set,
# in the solutions above we are running distance comparisons for each node, which may be more time-consuming. 
# Therefore, the visited set may improve time use at the expense of space use (although the asymptotic values 
# would stay the same).

if __name__ == "__main__":
    my = Solution()

    rooms0 = [[2147483647,-1,0,2147483647],
    [2147483647,2147483647,2147483647,-1],
    [2147483647,-1,2147483647,-1],
    [0,-1,2147483647,2147483647]]

    rooms1 = [[2147483647,-1,0,2147483647],
    [2147483647,2147483647,2147483647,-1],
    [2147483647,-1,2147483647,-1],
    [0,-1,2147483647,2147483647]]

    print(my.wallsAndGates(rooms0))
    print(my.wallsAndGates([[-1]]))

    print(my.wallsAndGatesQueue(rooms1))
    print(my.wallsAndGatesQueue([[-1]]))

