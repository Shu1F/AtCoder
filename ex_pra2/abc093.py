A, B, K = map(int, input().split())

s = set()

for x in range(A, min(B, A + K - 1) + 1):
    s.add(x)

for y in range(max(A, B - K + 1), B + 1):
    s.add(y)

for z in sorted(s):
    print(z)