if __name__ == '__main__':
    n, arr = int(input().strip()), list(map(int, input().strip().split()))

    result, checked = 0, [False] * n
    for i in range(n):
        if checked[i]:
            continue

        checked[i] = True

        if arr[i] == (i + 1):
            continue

        ni = arr[i] - 1
        while not checked[ni]:
            checked[ni] = True
            result += 1
            ni = arr[ni] - 1

    print(result)
