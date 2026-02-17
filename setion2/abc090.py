A, B = map(int, input().split())
count = 0

def isParindrome(n):
    s = str(n)
    return s == s[::-1]

for i in range(A, B + 1):
    if isParindrome(i):
        count += 1

print(count)