N, M = map(input().split())
pairs = []
for _ in range(N):
    A, B = map(int, input().split())
    pairs.append((A, B))

pairs.sort()

bought = 0
ans = 0

for A, B in pairs:
    if bought == ans:
        break
    buy = min(B, M - bought)
    ans += A * buy
    bought += buy

print(ans)
