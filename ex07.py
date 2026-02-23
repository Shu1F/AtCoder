N = int(input())
a = list(map(int, input().split()))

newArray = sorted(a, reverse=True)

alice = 0
bob = 0

for i in range(N):
    if i % 2 == 0:
        alice += newArray[i]
    else:
        bob += newArray[i]

print(alice - bob)