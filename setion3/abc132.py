N = int(input())
d = list(map(int, input().split()))

d.sort()

mid_right = d[N//2]        
mid_left  = d[N//2 - 1]   

print(mid_right - mid_left)