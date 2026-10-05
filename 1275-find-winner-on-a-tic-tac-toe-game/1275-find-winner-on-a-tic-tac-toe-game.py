class Solution:
    def tictactoe(self, moves: list[list[int]]) -> str:
        grid = [[None] * 3 for _ in range(3)]
        
        player1 = 'A'
        player2 = 'B'
        for x, y in moves:
            grid[x][y] = player1
            
            # check if player 1 has won
            if all([grid[x][i] == player1 for i in range(3)]):
                return player1
            
            if all([grid[i][y] == player1 for i in range(3)]):
                return player1
            
            # check diagonals
            forward_diagonal = [(0, 0), (1, 1), (2, 2)]
            if (x, y) in forward_diagonal:
                if all([grid[p][q] == player1 for p, q in forward_diagonal]):
                    return player1
            
            backward_diagonal = [(2, 0), (1, 1), (0, 2)]
            if (x, y) in backward_diagonal:
                if all([grid[p][q] == player1 for p, q in backward_diagonal]):
                    return player1
            
            player1, player2 = player2, player1
        return "Draw" if len(moves) == 9 else "Pending"

        