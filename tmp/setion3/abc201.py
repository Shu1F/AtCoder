N = int(input())
mountainsData = []
for _ in range(N):
    S, T = input().split()
    mountainsData.append([int(T), S])

mountainsData.sort()

print(mountainsData[-2][1])