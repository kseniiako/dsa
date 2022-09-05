# Surrounded Regions (Leetcode 130)

# Given an m x n matrix containing "X" and "O", capture
# all the regions that are 4-directionally surrounded by "X".

# A region is captured by flipping all "O"'s into "X"'s in that
# surrounded region.

# Notice that an "O" can't be flipped if either of the following
# is satisfied:
# - It is on the border;
# - It is adjacent to an "O" that should not be flipped.

from collections import deque

class Solution:
    def solve(self, board):
        # Idea: iterate through the grid. Save all "O"'s in a set for easy access. 
        # The set designates nodes to be flipped. Save all border "O"'s in a second
        # set: these are the possible starting points to find islands that should not
        # be flipped.
        # Perform BFS around "O"'s that are on the borders. Delete all
        # "O"'s belonging to these islands from the to_flip set (they should
        # not be flipped). 
        # Flip all the "O"'s remaining in the set!
        # Yes, we do need extra space to store the two sets (both sets max out at size n*m),
        # but we gain an advantage in terms of time complexity since we never have to
        # look at "X" nodes during breadth-first search. Moreover, looking up an element
        # in a set or removing it are both O(1) time — very convenient.
        max_vert = len(board)
        max_hor = len(board[0])
        to_flip = set()
        on_borders = set()

        dirs = [[0, 1], [0, -1], [1, 0], [-1, 0]]

        def bfs(r, c):

            if (r, c) not in to_flip:
                return
            
            q = deque([(r, c)])
            while q:
                row, col = q.popleft()
                if row in range(max_vert) and \
                col in range(max_hor) and \
                (row, col) in to_flip:
                    to_flip.remove((row, col))
                    for r_dir, c_dir in dirs:
                        new_row, new_col = row + r_dir, col + c_dir
                        q.append((new_row, new_col))

        for r in range(max_vert):
            for c in range(max_hor):
                if board[r][c] == "O":
                    to_flip.add((r,c))
                    if r == 0 or c == 0 or r == max_vert-1 or c == max_hor-1:
                        on_borders.add((r, c))
        
        for r, c in on_borders:
            bfs(r, c)

        for r, c in to_flip:
            board[r][c] = "X"
        
        print(board)
        return

        # Where n and m are the grid dimensions,
        # - time complexity is O(n*m) to iterate through the whole grid +
        # perform manipulations with sets derived from the grid.
        # - space complexity is O(n*m). We need O(n*m) space for each of the
        # two sets and O(n*m) space for the queue used in breadth-first search.

if __name__ == "__main__":
    my = Solution()
    print(my.solve([["X","X","X","X"],["X","O","O","X"],["X","X","O","X"],["X","O","X","X"]]))
    print(my.solve([["X"]]))