N, K = map(int, input().split())

count = 0
while(count < K) :
    if N % 200 == 0 :
        N //= 200
        count += 1
    else :
        N = int(str(N) + "200")
        count += 1
print(N)