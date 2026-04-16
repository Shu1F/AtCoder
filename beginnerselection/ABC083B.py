N, A, B = map(int, input().split())
count = 0

def calc_sum(total):
    sum = 0
    while total > 0:
        sum += total % 10
        total //= 10
    return sum

for i in range(1, N + 1):
    if B >= calc_sum(i) >= A:
        count += i

print(count)

## 別解

# N, A, B = map(int, input().split())
# answer = 0

# for i in range(1, N + 1):
#     if A <= sum(map(int, str(i))) <= B:
#         answer += i

# print(answer)