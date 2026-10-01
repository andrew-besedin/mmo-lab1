def make_board(n, m):
    board = []
    for i in range(n):
        row = []
        for j in range(m):
            if (i + j) % 2 == 0:
                row.append(".")
            else:
                row.append("*")
        board.append(row)
    return board


def main():
    n = int(input("Enter n: "))
    m = int(input("Enter m: "))
    board = make_board(n, m)
    for row in board:
        print(" ".join(row))


main()
