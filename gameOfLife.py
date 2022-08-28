# Game of Life (Leetcode 289)

# Rules:
# 1. Any live cell with fewer than 2 live neighbors dies.
# 2. Any live cell with 2-3 live neighbors lives on.
# 3. Any live cell with more than 3 live neighbors dies.
# 4. Any dead cell with exactly three live neighbors becomes live.

class Solution:
    def gameOfLifeHashmap(self, board):
        dirs = [[-1, -1], [-1, 0], [-1, 1], 
        [0, -1], [0, 1],
        [1, -1], [1, 0], [1, 1]]
        max_hor = len(board[0])
        max_vert = len(board)

        changed_values = {}
        for i in range(max_vert):
            for j in range(max_hor):
                cur = board[i][j]
                count = 0

                for i_dir, j_dir in dirs:
                    new_i_dir, new_j_dir = i+i_dir, j+j_dir
                    if (new_i_dir in range(max_vert) and \
                    new_j_dir in range(max_hor)):
                        count += board[new_i_dir][new_j_dir]
                
                if cur:
                    if count < 2 or count > 3:
                        changed_values[(i, j)] = 0
                elif count == 3:
                    changed_values[(i, j)] = 1
        
        for i, j in changed_values:
            board[i][j] = changed_values[(i, j)]

        return board

    def gameOfLifePlaceholders(self, board):
        dirs = [[-1, -1], [-1, 0], [-1, 1], 
        [0, -1], [0, 1],
        [1, -1], [1, 0], [1, 1]]
        max_hor = len(board[0])
        max_vert = len(board)

        # Convention: if cell goes from 1 to 0 -> set its value to 2
        # If cell goes from 0 to 1 -> set its value to 3

        for i in range(max_vert):
            for j in range(max_hor):
                cur = board[i][j]
                count = 0

                for i_dir, j_dir in dirs:
                    new_i_dir, new_j_dir = i+i_dir, j+j_dir
                    if (new_i_dir in range(max_vert) and \
                    new_j_dir in range(max_hor)):
                        if board[new_i_dir][new_j_dir] in {1, 2}:
                            count += 1
                
                if cur:
                    if count < 2 or count > 3:
                        board[i][j] = 2
                elif count == 3:
                    board[i][j] = 3
        
        for i in range(max_vert):
            for j in range(max_hor):
                if board[i][j] > 1:
                    board[i][j] -= 2

        return board

                    
if __name__ == "__main__":
    my = Solution()
    board1 = [[0,1,0],[0,0,1],[1,1,1],[0,0,0]]
    board2 = [[1,1],[1,0]]
    print(my.gameOfLifeHashmap(board1))
    print(my.gameOfLifeHashmap(board2))

    board1 = [[0,1,0],[0,0,1],[1,1,1],[0,0,0]]
    board2 = [[1,1],[1,0]]
    print(my.gameOfLifePlaceholders(board1))
    print(my.gameOfLifePlaceholders(board2))


