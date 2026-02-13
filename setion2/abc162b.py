N = int(input())
sum = 0
while N != 0:
    if N % 3 != 0 and N % 5 != 0:
        sum += N
        N -= 1
    else:
        N -= 1

print(sum)