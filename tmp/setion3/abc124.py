N = int(input())
H = list(map(int, input().split()))

count = 1
maxHeight = H[0]

for i in range(1, N):
    if H[i] >= maxHeight:
        count += 1
        maxHeight = H[i]

print(count)