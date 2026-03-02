N = int(input())
T, A = map(int, input().split())
H = list(map(int, input().split()))
tmpList = []

for i in range(N):
    avgTmp = T - H[i] * 0.006
    tmpList.append([abs(A - avgTmp), i+1])

tmpList.sort()

print(tmpList[0][1])