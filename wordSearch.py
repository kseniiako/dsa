# Word Search (Leetcode 79)

# Given an m x n grid of characters, return True if word exists
# in the grid.

# The word can be constructed from letters of sequentially adjacent
# cells, where adjacent cells are horizontally or vertically neighboring.
# The same letter cell may not be used more than once.

from collections import deque

class Solution:
    def exist(self, board, word):
        # My idea is to start only if we stumble upon
        # first letter of the word, but in other situations, it may be more efficient 
        # to start if we stumble upon any of the word's letters. It really depends
        # on what the grid looks like. (Seems random to me?)
        max_vert = len(board)
        max_hor = len(board[0])

        word_len = len(word)

        def construct(r, c, i):
            directions = [[0, 1], [0, -1], [1, 0], [-1, 0]]

            if i == len(word):
                return True
            
            for dirs_row, dirs_col in directions:
                new_row, new_col = r+dirs_row, c+dirs_col
                if (new_row in range(max_vert) and \
                new_col in range(max_hor) and \
                board[new_row][new_col] == word[i]):
                    board[new_row][new_col] = 0
                    if construct(new_row, new_col, i+1):
                        return True
                    board[new_row][new_col] = word[i]
                    

        for r in range(len(board)):
            for c in range(len(board[0])):
                if board[r][c] == word[0]:
                    board[r][c] = 0
                    if construct(r, c, 1):
                        return True
                    board[r][c] = word[0]
        
        return False
    
    def existFast(self, board, word):
        # The previous approach is pretty slow since it visits a lot of nodes twice:
        # even the clearly ineligible ones that contain letters that are not in our word.
        # Some hashing should solve this problem. Let's hash all letters in the word in a set. ->
        # Hash all eligible nodes (ones that contain letters from target word) in a dictionary where
        # key is (index tuple) and value is letter. -> Hash all index tuples that contain starting letter
        # in a "starting points" set. And we move from there :)
        letter_set = set(word)
        letter_dict = {}

        start_letter = word[0]
        start_pts = set()

        max_vert = len(board)
        max_hor = len(board[0])
        word_len = len(word)

        dirs = [[-1, 0], [1, 0], [0, -1], [0, 1]]

        def search(start, ind):
            
            if ind == word_len:
                return True
            if start in letter_dict and \
            letter_dict[start] == word[ind]:
                letter_dict[start] = [-1, -1]
                cur_row, cur_col = start
                for dir_row, dir_col in dirs:
                    if search((cur_row + dir_row, cur_col + dir_col), ind+1):
                        return True
                letter_dict[start] = word[ind]
            
            return False
            

        for r in range(max_vert):
            for c in range(max_hor):
                if board[r][c] in letter_set:
                    letter_dict[(r, c)] = board[r][c]
                    if board[r][c] == start_letter:
                        start_pts.add((r, c))

        if len(letter_dict) < len(word) or not start_pts:
            return False
        else:
            for start in start_pts:
                if search(start, 0):
                    return True
        return False

# Space complexity: O(m*n), where m and n are dimensions of the board (think storing
# the dictionary with all eligible nodes), as well as the size of the function call stack for
# the recursive search. Because the function call stack can reack O(n*m) size in approach 1 as well,
# the space complexity is the same for the hashing and no-hash approaches.

# Time complexity: O(cell_count * 3^word_length), where cell_count is the number of cells on the
# board, and word_length is the length of the target word. To quote the article on Leetcode:

# "For the backtracking function, initially we could have at most 4 directions
# to explore, but further the choices are reduced into 3 (since we won't go back
# to where we come from). As a result, the execution trace after the first step could
# be visualized as a 3-ary tree, each of the branches represent a potential
# exploration in the corresponding direction. Therefore, in the worst case,
# the total number of invocations would be the number of nodes in a full 3-nary tree,
# which is about 3^L."

# "We iterate through the board for backtracking, i. e. there could be N times invocation
# for the backtracking function in the worst case."

if __name__ == "__main__":
    my = Solution()
    board0 = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]]
    word0 = "ABCCED"
    word1 = "SEE"
    word2 = "ABCB"

    board1 = [["C","A","A"],["A","A","A"],["B","C","D"]]
    word3 = "AAB"
    print("""Please note that since the input board is modified in both 
    approaches, tests should be isolated from each other to return
    the correct output (i. e. don't run multiple tests on the same input
    one after another).""")
    # Approach 1
    #print(my.exist(board0, word0))
    #print(my.exist(board0, word1))
    #print(my.exist(board0, word2))

    #print(my.exist(board1, word3))

    # Approach 2
    print(my.existFast(board0, word0))
    #print(my.existFast(board0, word1))
    #print(my.existFast(board0, word2))

    print(my.existFast(board1, word3))
