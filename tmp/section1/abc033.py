H, W = map(int, input().split())

if H == 1 or W == 1:
    if (H * W) % 2 == 0:
        print((H * W) // 2)
    else:
        print((H * W) // 2 + 1)
else:
    if H % 2 == 0:
        height = H // 2
    else:
        height = (H + 1) // 2

    if W % 2 == 0:
        width = W // 2
    else:
        width = (W + 1) // 2

    print(height * width)