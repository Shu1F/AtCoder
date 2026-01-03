N = int(input())

totalSavings = 0
dayCount = 0
for i in range(1, N + 1) :
    totalSavings += i
    dayCount += 1
    if totalSavings >= N :
        print(dayCount)
        break