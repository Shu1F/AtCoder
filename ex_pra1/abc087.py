X = int(input()) # 全体のお金
A = int(input()) # ケーキ代
B = int(input()) # ドーナツ代

result = (X - A) - (((X - A) // B) * B)

print(result)
