N = int(input())

if N % 1000 == 0:
    print(0)
else:
    m = N // 1000 + 1
    print(1000 * m - N)
