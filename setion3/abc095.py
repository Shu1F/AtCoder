N, X = map(int, input().split())
m = list(map(int, input().split()))


for i in range(m[i]):
    X -= m[i]
min_amount = min(m)

print(X//min_amount + len(m))