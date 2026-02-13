# N = int(input())
# sum = 0
# while N != 0:
#     if N % 3 != 0 and N % 5 != 0:
#         sum += N
#         N -= 1
#     else:
#         N -= 1

# print(sum)

N = int(input())
total = 0

for i in range(1, N + 1):
    if i % 3 != 0 and i % 5 != 0:
        total += i

print(total)
