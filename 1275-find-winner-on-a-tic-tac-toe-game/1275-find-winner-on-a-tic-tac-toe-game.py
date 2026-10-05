class Solution:
    def tictactoe(self, moves: list[list[int]]) -> str:
        n = 3
        rows, cols = [0] * n, [0] * n
        forward_diagonal = 0
        backward_diagonal = 0
        
        player1 = 'A'
        player2 = 'B'
        for x, y in moves:
            sign = 1 if player1 == 'A' else -1
            rows[x] += sign
            cols[y] += sign
            if x == y:
                forward_diagonal += sign
            if x + y == n - 1:
                backward_diagonal += sign

            if abs(rows[x]) == n or abs(cols[y]) == n or abs(forward_diagonal) == n or abs(backward_diagonal) == n:
                return player1
            
            player1, player2 = player2, player1
        return "Draw" if len(moves) == n * n else "Pending"

        