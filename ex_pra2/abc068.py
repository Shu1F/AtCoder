N = int(input())

max_count = -1
answer = 1

for i in range(1, N + 1):
    x = i
    count = 0
    while x % 2 == 0:
        x //= 2
        count += 1

    if count > max_count:
        max_count = count
        answer = i

print(answer)