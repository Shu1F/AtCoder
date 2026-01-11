P = int(input())

coins = []
fact = 1

for i in range(1, 11):
    fact *= i
    coins.append(fact)

ans = 0

for coin in reversed(coins):
    use = min(100, P // coin)
    ans += use
    P -= use * coin
print(ans)