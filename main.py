def print_board(board):
    """Print the current state of the board."""
    for row in board:
        print(" | ".join(row))
        print("-" * 5)


def check_winner(board, player):
    """Check if the player has won."""
    # Check rows, columns, and diagonals
    for i in range(3):
        if all([spot == player for spot in board[i]]):  # Check rows
            return True
        if all([board[j][i] == player for j in range(3)]):  # Check columns
            return True
    if all([board[i][i] == player for i in range(3)]):  # Check main diagonal
        return True
    if all([board[i][2 - i] == player for i in range(3)]):  # Check anti-diagonal
        return True
    return False


def check_draw(board):
    """Check if the game is a draw."""
    return all([spot != ' ' for row in board for spot in row])


def get_valid_moves(board):
    """Get a list of valid moves."""
    return [(i, j) for i in range(3) for j in range(3) if board[i][j] == ' ']


def make_move(board, player, row, col):
    """Place a player's move on the board."""
    if board[row][col] == ' ':
        board[row][col] = player
        return True
    return False


def tic_tac_toe():
    """Main function to run the Tic Tac Toe game."""
    board = [[' ' for _ in range(3)] for _ in range(3)]
    current_player = 'X'

    while True:
        print_board(board)
        print(f"Player {current_player}'s turn")

        # Get player input
        try:
            row, col = map(int, input("Enter row and column (0, 1, or 2) separated by space: ").split())
        except ValueError:
            print("Invalid input. Please enter row and column as two integers separated by space.")
            continue

        # Make the move
        if row in range(3) and col in range(3):
            if make_move(board, current_player, row, col):
                if check_winner(board, current_player):
                    print_board(board)
                    print(f"Player {current_player} wins!")
                    break
                elif check_draw(board):
                    print_board(board)
                    print("The game is a draw!")
                    break
                current_player = 'O' if current_player == 'X' else 'X'
            else:
                print("This spot is already taken. Try again.")
        else:
            print("Invalid move. Row and column must be 0, 1, or 2. Try again.")

if __name__ == "__main__":
    tic_tac_toe()

