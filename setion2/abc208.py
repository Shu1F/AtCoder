import math

P = int(input())
count = 0

for num in range(10, 0, -1):
    fac = math.factorial(num)
    use = min(100, P // fac)
    count += use
    P -= use * fac

print(count)