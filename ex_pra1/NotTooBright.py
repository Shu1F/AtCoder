H, W = map(int, input().split())
if H == 1 :
    print(W)
elif W == 1 :
    print(H)
elif H >=2 and W >= 2 :
    print(((H + 1) // 2) * ((W + 1) // 2))