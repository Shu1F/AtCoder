A, B = map(int, input().split())

for x in range(1, 2000):
    if (x * 8) // 100 == A and (x * 10) // 100 == B:
        print(x)
        break
else:
    print(-1)
