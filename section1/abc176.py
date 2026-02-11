N, X, T = map(int, input().split())
# 20 12 6
if X >= N:
    print(T)
elif N % X == 0:
    print(T * (N // X))
else:
    print(T * (N // X + 1))