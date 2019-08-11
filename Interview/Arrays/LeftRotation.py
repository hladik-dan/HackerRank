from collections import deque

if __name__ == '__main__':
    n, d = list(map(int, input().strip().split()))
    a = deque(input().strip().split())

    a.rotate(-d)
    result = " ".join(a)

    print(result)
