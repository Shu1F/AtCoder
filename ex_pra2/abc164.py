A, B, C, D = map(int, input().split())

while True:
    # 高橋の攻撃
    C -= B
    if C <= 0:
        print("Yes")
        break

    # 青木の攻撃
    A -= D
    if A <= 0:
        print("No")
        break

# 別解
import math

A, B, C, D = map(int, input().split())

takahashi = math.ceil(C / B)
aoki = math.ceil(A / D)

if takahashi <= aoki:
    print("Yes")
else:
    print("No")

