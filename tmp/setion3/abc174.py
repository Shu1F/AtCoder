N, D = map(int, input().split())
D2 = D * D
count = 0

for _ in range(N):
    X, Y = map(int, input().split())
    if X * X + Y * Y <= D2:
        count += 1

print(count)