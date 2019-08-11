if __name__ == '__main__':
    t = int(input().strip())

    for _ in range(t):
        n, q = int(input().strip()), list(map(int, input().strip().split()))

        result = 0
        for i, x in enumerate(q):
            if x - (i + 1) > 2:
                result = "Too chaotic"
                break

            for y in q[max(0, x - 2):i]:
                if y > x:
                    result += 1

        print(result)
