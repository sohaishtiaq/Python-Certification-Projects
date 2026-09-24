def dfs_n_queens(n):
    if n < 1:
        return []

    solutions = []
    board = []

    def is_valid(row, col):
        for prev_row in range(row):
            prev_col = board[prev_row]

            # Same column
            if prev_col == col:
                return False

            # Same diagonal
            if abs(prev_col - col) == abs(prev_row - row):
                return False

        return True

    def dfs(row):
        if row == n:
            solutions.append(board[:])
            return

        for col in range(n):
            if is_valid(row, col):
                board.append(col)
                dfs(row + 1)
                board.pop()

    dfs(0)
    return solutions
