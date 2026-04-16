N = int(input())
A = list(map(int, input().split()))

operationCount = 0

while True:
    for num in A:
        if num % 2 == 1:
            print(operationCount)
            exit()

    A = [num // 2 for num in A]
    operationCount += 1