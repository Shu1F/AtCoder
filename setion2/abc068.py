N = int(input())
maxCount = 0
ansNum = 0

for i in range(1, N + 1):
    count = 0
temp = i
while temp % 2 == 0:
    temp //= 2
    count += 1
        else:
            break
    if count > maxCount:
        maxCount = count
        ansNum = i

print(ansNum)