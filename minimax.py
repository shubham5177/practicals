# Initialize the game board
board = [" "] * 9

# Display the board
def show():
    for i in range(0, 9, 3):
        print(board[i], "|", board[i+1], "|", board[i+2])
    print()

# Check for a winner
def winner(p):
    wins = [(0,1,2), (3,4,5), (6,7,8),
            (0,3,6), (1,4,7), (2,5,8),
            (0,4,8), (2,4,6)]
    return any(all(board[i] == p for i in w) for w in wins)

# Minimax algorithm
def minimax(is_max):
    if winner("O"):
        return 1
    if winner("X"):
        return -1
    if " " not in board:
        return 0

    scores = []
    for i in range(9):
        if board[i] == " ":
            board[i] = "O" if is_max else "X"
            scores.append(minimax(not is_max))
            board[i] = " "

    return max(scores) if is_max else min(scores)

# Play the game
while True:
    show()

    # Human move
    move = int(input("Enter position (1-9): ")) - 1
    if move not in range(9) or board[move] != " ":
        print("Invalid move!")
        continue
    board[move] = "X"

    if winner("X"):
        show()
        print("You win!")
        break
    if " " not in board:
        show()
        print("Draw!")
        break

    # Computer chooses the best move
    best_score = -float("inf")
    best_move = -1

    for i in range(9):
        if board[i] == " ":
            board[i] = "O"
            score = minimax(False)
            board[i] = " "

            if score > best_score:
                best_score = score
                best_move = i

    board[best_move] = "O"

    if winner("O"):
        show()
        print("Computer wins!")
        break
    if " " not in board:
        show()
        print("Draw!")
        break