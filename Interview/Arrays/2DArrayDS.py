from math import inf

if __name__ == '__main__':
    size, matrix = 6, []

    for y in range(size):
        matrix.append(list(map(int, input().strip().split())))

    result = -inf
    for y in range(4):
        for x in range(4):
            sum = 0
            sum += matrix[y][x]
            sum += matrix[y][x + 1]
            sum += matrix[y][x + 2]
            sum += matrix[y + 1][x + 1]
            sum += matrix[y + 2][x]
            sum += matrix[y + 2][x + 1]
            sum += matrix[y + 2][x + 2]

            if sum > result:
                result = sum

    print(result)
