N, K = map(int, input().split())
l =list(map(int, input().split()))
length = 0
l.sort(reverse=True)

for i in range(K):
    length += l[i]