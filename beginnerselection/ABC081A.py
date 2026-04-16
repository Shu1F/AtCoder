s = list(map(int, input().split()))

count = 0
for i in s:
    if i == 1:
        count += 1

print(count)

# print(s.count(1))