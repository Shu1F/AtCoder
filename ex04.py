# K = int(input())
# A, B = map(int, input().split())
# i = 1

# while True:
#     num = K * i
#     if num > B:
#         print("NG")
#         break

#     if A <= num <= B:
#         print("OK")
#         break

#     i += 1

# 別解

import math

K = int(input())
A, B = map(int, input().split())

num = math.ceil(A / K) * K

if num > B:
    print("NG")
else:
    print("OK")