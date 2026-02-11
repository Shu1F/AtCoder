H, W = map(int, input().split())

if H == 1 or W == 1:
    if (H * W) % 2 == 0:
        print((H * W) // 2)
    else:
        print((H * W) // 2 + 1)
elif H >= 2 and W >= 2:
    if H % 2 == 0:
        height = H // 2
    else:
        height = H // 2 + 1

    if W % 2 == 0:
        width = W // 2
    else:
        width = W // 2 + 1

    print(height * width)