A, B, T = map(int, input().split())

maxTime = T + 0.5

allCookies = int(B * (maxTime // A))

print(allCookies)