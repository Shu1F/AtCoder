N, X, T = map(int, input().split())

if N % X == 0 :
    num = N // X
    print(T * num)
elif N % X >= 1 :
    num = (N // X) + 1
    print(T * num)
else :
    print(T)