A, B = map(int, input().split())

for product in range(1, 10 * (B + 1)):
    if A == product * 8 // 100 and B == product * 10 // 100:
        print(product)
        break
else:
    print(-1)