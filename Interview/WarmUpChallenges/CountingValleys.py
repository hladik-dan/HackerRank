if __name__ == '__main__':
    n, s = int(input().strip()), input().strip()

    level, count, result = 0, True, 0
    for x in list(s):
        if x == "D":
            level -= 1
        if x == "U":
            level += 1

        if level == 0:
            count = True

        if count and level < 0:
            result += 1
            count = False

    print(result)
