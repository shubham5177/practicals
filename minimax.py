board = [" "] * 9

def show():
    for i in range(0, 9, 3):
        print(board[i:i+3])

def win(p):
    w = [(0,1,2),(3,4,5),(6,7,8),
         (0,3,6),(1,4,7),(2,5,8),
         (0,4,8),(2,4,6)]

    return any(all(board[i] == p for i in x) for x in w)

def minimax(maxi):
    if win("Q"): return 1
    if win("X"): return -1
    if " " not in board: return 0

    score = []

    for i in range(9):
        if board[i] == " ":
            board[i] = "Q" if maxi else "X"
            score.append(minimax(not maxi))
            board[i] = " "

    return max(score) if maxi else min(score)

while True:
    show()
    m = int(input("Enter number between 1-9: ")) - 1

    if m not in range(9) or board[m] != " ":
        print("Invalid move")
        continue

    board[m] = "X"

    if win("X"):
        show()
        print("You win")
        break

    if " " not in board:
        show()
        print("Draw")
        break

    best, move = -2, -1

    for i in range(9):
        if board[i] == " ":
            board[i] = "Q"
            scores = minimax(False)
            board[i] = " "

            if scores > best:
                best, move = scores, i

    board[move] = "Q"

    if win("Q"):
        show()
        print("Computer wins")
        break

    if " " not in board:
        show()
        print("Draw")
        break
