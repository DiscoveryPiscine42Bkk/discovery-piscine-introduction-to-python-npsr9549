def is_king_in_check(board):
    n = len(board)
    king_pos = None

    for i in range(n):
        for j in range(n):
            if board[i][j] == 'K':
                king_pos = (i, j)
                break
        if king_pos:
            break
    if not king_pos:
        return

    x, y = king_pos

    def in_bounds(i, j):
        return 0 <= i < n and 0 <= j < n

    for dx, dy in [(-1, -1), (-1, 1)]:
        ni, nj = x + dx, y + dy
        if in_bounds(ni, nj) and board[ni][nj] == 'p':
            print("Success")
            return

    knight_moves = [(-2, -1), (-2, 1), (-1, -2), (-1, 2),
                    (1, -2), (1, 2), (2, -1), (2, 1)]
    for dx, dy in knight_moves:
        ni, nj = x + dx, y + dy
        if in_bounds(ni, nj) and board[ni][nj] == 'n':
            print("Success")
            return

    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    for dx, dy in directions:
        ni, nj = x + dx, y + dy
        while in_bounds(ni, nj):
            piece = board[ni][nj]
            if piece == '.':
                ni += dx
                nj += dy
                continue
            if piece in ('r', 'q'):
                print("Success")
                return
            break

    diagonals = [(-1, -1), (-1, 1), (1, -1), (1, 1)]
    for dx, dy in diagonals:
        ni, nj = x + dx, y + dy
        while in_bounds(ni, nj):
            piece = board[ni][nj]
            if piece == '.':
                ni += dx
                nj += dy
                continue
            if piece in ('b', 'q'):
                print("Success")
                return
            break

    print("Fail")


board = [
"X . . X . . X",
". X . X . X .",
". . X X X . .",
"X X X Q X X X",
". . X X X . .",
". X . X . X .",
"X . . X . . X"
]

is_king_in_check(board)