N = int(input())
maxCount = 0
ansNum = 0

for i in range(1, N + 1):
    count = 0
    tmp = i    
    while tmp % 2 == 0:
        tmp //= 2
        count += 1

    if count > maxCount:
        maxCount = count
        ansNum = i

print(ansNum)