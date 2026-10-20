
# Create an empty chessboard
N = 8
board = [-1] * N

# Check whether a queen can be placed safely
def safe(row, col):
    for r in range(row):
        # Check same column and diagonal
        if board[r] == col or abs(board[r] - col) == abs(r - row):
            return False
    return True

# Solve using backtracking
def solve(row):
    # All queens are placed
    if row == N:
        return True

    # Try each column
    for col in range(N):
        if safe(row, col):
            board[row] = col

            # Place queen in next row
            if solve(row + 1):
                return True

            # Backtrack if placement fails
            board[row] = -1

    return False

# Run the program
if solve(0):
    for row in range(N):
        for col in range(N):
            if board[row] == col:
                print("Q", end=" ")
            else:
                print(".", end=" ")
        print()
else:
    print("No solution found")

