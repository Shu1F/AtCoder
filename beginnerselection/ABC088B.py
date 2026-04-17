N = int(input())
a = list(map(int, input().split()))

a.sort(reverse=True)

aliceNum = 0
bobNum = 0

for i in range(N):
    if i % 2 == 0:
        aliceNum += a[i]
    else:
        bobNum += a[i]

print(aliceNum - bobNum)