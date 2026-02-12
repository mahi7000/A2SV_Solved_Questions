if __name__ == "__main__":
    for i in range(5):
        row = list(map(int, input().split()))
        if 1 in row:
            row1 = i
            col1 = row.index(1)
            break

    print(abs(2 - row1) + abs(2 - col1))
