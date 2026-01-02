N = int(input())

if N % 1000 == 0 :
    num = (N // 1000)
    print((num * 1000) - N)
else :
    num = (N // 1000) + 1
    print((num * 1000) - N)

