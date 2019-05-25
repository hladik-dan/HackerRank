from math import floor

if __name__ == '__main__':
    s, n = input().strip(), int(input().strip())

    result = s.count("a") * floor(n/len(s)) + s[0:(n%len(s))].count("a")

    print(result)
