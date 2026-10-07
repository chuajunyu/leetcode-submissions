class Solution:
    def gameOfLife(self, board: list[list[int]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """

        # Maintain 2 copies of the board
        # Iterate through each cell in the current board, and infer it's next state
        # O(m x n) time for each iteration
        # O(m x n) space

        # m and n are > 0
        m = len(board)
        n = len(board[0])
        
        tmp_board = [list(row) for row in board]

        for i in range(m):
            for j in range(n):
                # check neighbours
                live_neighbours = 0
                for dx in range(-1, 2):
                    for dy in range(-1, 2):
                        x = i + dx
                        y = j + dy

                        if x < 0 or x >= m or y < 0 or y >= n:
                            continue
                        
                        if dx == 0 and dy == 0:
                            continue

                        if tmp_board[x][y]:
                            live_neighbours += 1
                
                # update the next state
                if tmp_board[i][j]:
                    if live_neighbours < 2:
                        board[i][j] = 0
                    elif live_neighbours > 3:
                        board[i][j] = 0
                else:
                    if live_neighbours == 3:
                        board[i][j] = 1
                
                live_neighbours = 0
        

