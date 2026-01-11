A, B, K = map(int, input().split())

nums = []

for i in range(A, B + 1):
    if (A <= i and i <= A + K - 1) or (B - K + 1 <= i and i <= B):
        print(i)
