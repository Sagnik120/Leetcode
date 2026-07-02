class Solution:
    def tictactoe(self, moves: List[List[int]]) -> str:
        board = [[""] * 3 for _ in range(3)]

        for i, (r, c) in enumerate(moves):
            if i % 2 == 0:
                board[r][c] = "X"
            else:
                board[r][c] = "O"

        def win(ch):
            # Rows
            for i in range(3):
                if all(board[i][j] == ch for j in range(3)):
                    return True

            # Columns
            for j in range(3):
                if all(board[i][j] == ch for i in range(3)):
                    return True

            # Diagonals
            if all(board[i][i] == ch for i in range(3)):
                return True

            if all(board[i][2 - i] == ch for i in range(3)):
                return True

            return False

        if win("X"):
            return "A"
        if win("O"):
            return "B"

        if len(moves) == 9:
            return "Draw"

        return "Pending"