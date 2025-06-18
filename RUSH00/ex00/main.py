if __name__ == "__main__":
    import sys
    board = []
    for line in sys.stdin:
        line = line.strip()
        if line:
            board.append(line)
    is_king_in_check(board)