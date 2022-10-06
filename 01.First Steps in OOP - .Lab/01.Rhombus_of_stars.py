def printing_row(n,row):
    for space in range(n - row):
        print(" ", end="")
    for star in range(1, row):
        print("*", end=' ')
    print("*")


def print_up(n):
    for row in range(1, n + 1):
        printing_row(n,row)


def print_bott(n):
    for row in range(n - 1, 0, -1):
        printing_row(n,row)


def printing_rhombus(n):
    print_up(n)
    print_bott(n)


n = int(input())
printing_rhombus(n)