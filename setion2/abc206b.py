N = int(input())

total = 0
i = 1
while True:
    total += i
    if total >= N:
        print(i)
        break
    i += 1