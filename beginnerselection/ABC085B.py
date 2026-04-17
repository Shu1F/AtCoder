N = int(input())

arry = []

for i in range(N):
    d = int(input())
    arry.append(d)

newArry = set(arry)

print(len(newArry))