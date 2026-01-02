r, g, b = map(int, input().split())
num = 0
num += r * 100
num += g * 10
num += b

if num % 4 == 0 :
    print("YES")
else :
    print("NO")