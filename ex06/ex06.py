def all_even(A):
    for x in A:
        if x % 2 != 0:
            return False
    return True

N = int(input())

A = list(map(int, input().split()))

count = 0
while all_even(A):
    for i in range(N):
        A[i] //= 2
    count += 1

print(count)