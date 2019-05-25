if __name__ == '__main__':
    n, c = int(input().strip()), list(map(int, input().strip().split()))

    x, result = 0, 0
    while x < len(c):
        if c[x] == 0 and x + 2 < len(c) and c[x + 2] == 0:
            result += 1
            x += 1
        elif c[x] == 0 and x + 1 < len(c) and c[x + 1] == 0:
            result += 1

        x += 1

    print(result)
