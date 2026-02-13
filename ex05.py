N, A, B = map(int, input().split())

ans = 0
while N != 0:
    num = N
    sum = 0

    while num != 0:
        sum += num % 10
        num //= 10

    if A <= sum <= B:
        ans += N

    N -= 1

print(ans)