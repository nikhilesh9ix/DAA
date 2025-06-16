def solve(n, row=0, board=[]):
    if row == n:
        print(*[c+1 for c in board])
        return
    for col in range(n):
        if all(col != board[r] and abs(col-board[r]) != row-r for r in range(row)):
            solve(n, row+1, board+[col])

solve(int(input()))

########################################

def solve(n, row=0, board=[]):
    if row == n:
        # Print solution (1-indexed)
        print(*[c + 1 for c in board])
        return
    for col in range(n):
        # Check if placing at (row, col) is safe
        if all(col != board[r] and abs(col - board[r]) != row - r for r in range(row)):
            solve(n, row + 1, board + [col])

# Input
n = int(input("Enter the value of N: "))
solve(n)
