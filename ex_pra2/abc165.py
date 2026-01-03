X = int(input())

money = 100
year = 0

while money < X:
    money += money // 100  # 1% 利子（切り捨て）
    year += 1

print(year)
