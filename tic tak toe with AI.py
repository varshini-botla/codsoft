# Initial board setup
EMPTY = '-'
AI_PLAYER = 'O'
HUMAN_PLAYER = 'X'

def print_board(board):
    """ Print the current state of the board """
    for row in board:
        print(' '.join(row))
    print()

def check_winner(board):
    """ Check if there is a winner or if the board is full (tie) """
    for row in board:
        if row.count(row[0]) == len(row) and row[0] != EMPTY:
            return row[0]  # Row winner
    for col in range(len(board[0])):
        if all(board[row][col] == board[0][col] and board[row][col] != EMPTY for row in range(len(board))):
            return board[0][col]  # Column winner
    if all(board[i][i] == board[0][0] and board[i][i] != EMPTY for i in range(len(board))) or \
       all(board[i][len(board)-1-i] == board[0][len(board)-1] and board[i][len(board)-1-i] != EMPTY for i in range(len(board))):
        return board[0][0]  # Diagonal winner
    if all(all(cell != EMPTY for cell in row) for row in board):
        return 'Tie'  # Board full, tie game
    return None  # No winner yet

def minimax(board, depth, maximizing_player):
    """ Minimax algorithm with alpha-beta pruning """
    winner = check_winner(board)
    if winner == AI_PLAYER:
        return 1
    elif winner == HUMAN_PLAYER:
        return -1
    elif winner == 'Tie':
        return 0

    if maximizing_player:
        max_eval = float('-inf')
        for row in range(len(board)):
            for col in range(len(board[0])):
                if board[row][col] == EMPTY:
                    board[row][col] = AI_PLAYER
                    eval = minimax(board, depth + 1, False)
                    board[row][col] = EMPTY
                    max_eval = max(max_eval, eval)
        return max_eval
    else:
        min_eval = float('inf')
        for row in range(len(board)):
            for col in range(len(board[0])):
                if board[row][col] == EMPTY:
                    board[row][col] = HUMAN_PLAYER
                    eval = minimax(board, depth + 1, True)
                    board[row][col] = EMPTY
                    min_eval = min(min_eval, eval)
        return min_eval

def best_move(board):
    """ Determine the best move using minimax algorithm with alpha-beta pruning """
    best_eval = float('-inf')
    best_move = None
    for row in range(len(board)):
        for col in range(len(board[0])):
            if board[row][col] == EMPTY:
                board[row][col] = AI_PLAYER
                eval = minimax(board, 0, False)
                board[row][col] = EMPTY
                if eval > best_eval:
                    best_eval = eval
                    best_move = (row, col)
    return best_move

def main():
    board = [
        [EMPTY, EMPTY, EMPTY],
        [EMPTY, EMPTY, EMPTY],
        [EMPTY, EMPTY, EMPTY]
    ]
    
    current_player = HUMAN_PLAYER
    
    while True:
        print_board(board)
        
        if current_player == HUMAN_PLAYER:
            while True:
                try:
                    row = int(input("Enter row (0, 1, 2): "))
                    col = int(input("Enter column (0, 1, 2): "))
                    if board[row][col] == EMPTY:
                        board[row][col] = current_player
                        break
                    else:
                        print("That spot is taken! Try again.")
                except ValueError:
                    print("Invalid input! Please enter a number.")
                except IndexError:
                    print("Invalid input! Please enter a number within range.")
        else:
            row, col = best_move(board)
            print(f"AI plays at row {row}, column {col}.")
            board[row][col] = AI_PLAYER
        
        winner = check_winner(board)
        if winner is not None:
            print_board(board)
            if winner == 'Tie':
                print("It's a tie!")
            else:
                print(f"{winner} wins!")
            break
        
        current_player = HUMAN_PLAYER if current_player == AI_PLAYER else AI_PLAYER

if __name__ == "__main__":
    main()
