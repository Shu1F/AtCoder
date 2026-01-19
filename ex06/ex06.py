N = int(input())

A = list(map(int, input().split()))

def all_even(A):
    for x in A:
        if x % 2 != 0:
            return False
    return True

count = 0
sign = 0
for i in range(N):
    if A[i] % 2 == 0:
        A[i] //= 2
        sign += 1
        if i == N and sign == N:
            count += 1
            i = 0
            sign = 0
    else:
        print(count)