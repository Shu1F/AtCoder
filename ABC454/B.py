N, M = map(int, input().split())
F = list(map(int, input().split()))

s = set(F)

if len(s) == N:
    print("Yes")
else:
    print("No")

if len(s) == M:
    print("Yes")
else:
    print("No")