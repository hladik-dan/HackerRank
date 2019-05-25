from collections import Counter
from math import floor

if __name__ == '__main__':
    n, ar = int(input().strip()), list(map(int, input().strip().split()))

    print(sum([floor(count/2) for value, count in Counter(ar).items()]))
