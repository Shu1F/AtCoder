import numpy as np

N, K = input().split()

for i in range(K):
    num9 = np.base_repr(int(N, 8), 9)   
    num9 = num9.replace("8", "5")
    N = num9
