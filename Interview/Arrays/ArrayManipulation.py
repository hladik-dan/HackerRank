from math import inf

if __name__ == '__main__':
    n, m = list(map(int, input().strip().split()))

    array, result = [0] * n, -inf
    for _ in range(m):
        a, b, k = list(map(int, input().strip().split()))

        array[a - 1] += k

        if b < n:
            array[b] += -k

    possible_result = 0
    for i in range(n):
        possible_result += array[i]

        if possible_result > result:
            result = possible_result

    print(result)
