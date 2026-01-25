N, X = map(int, input().split())
L = list(map(int, input().split()))

pos = 0
count = 1

for l in L:
    pos += l
    if pos <= X:
        count += 1
    else :
        break

print(count)